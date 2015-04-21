import copytext
import requests

from dataCollections.models import Instructor, CIS
from profsUT import settings

import os

class RowHelper:
    def __init__(self, row):
        self.row = row

    def __getitem__(self, key):
        return self.row[key].strip()

def tableToDatabase(inFileURL):
    if settings.AWS_ENVIRONMENT:
        pathForFile = os.path.join(settings.BASE_DIR, 'csvToDatabaseTemp.xlsx')
        r = requests.get(inFileURL)
        with open(pathForFile, 'wb') as f:
            f.write(r.content)
    else:
        pathForFile = os.path.join(settings.PROJECT_DIR, inFileURL[1:])

    copy = copytext.Copy(pathForFile)
    sheet = copy['results']
    for row in sheet:
        rHelper = RowHelper(row)
        # we only want Journalism for now
        if rHelper['college_school'] != 'Communication' or rHelper['organization'] != 'Journalism':
            continue

        instructorLastName = rHelper['instructor'].split(', ')[0].upper()
        instructorFirstName = rHelper['instructor'].split(', ')[1].upper()

        try:
            instructor = Instructor.objects.get(last=instructorLastName,
                                                first=instructorFirstName)
        except Instructor.DoesNotExist:
            continue # if the instructor referenced in the CIS doesn't exist
                     # in our database there's no point in using the CIS

        cisConstructorDict = {'instructor': instructor,
                              'course': rHelper['course_and_unique_num']}

        toAdd = ('organization', 'college_school', 'semester')

        for name in toAdd:
            cisConstructorDict[name] = rHelper[name]

        toAdd = ('forms_distributed', 'forms_returned')

        for name in toAdd:
            cisConstructorDict[name] = int(rHelper[name])

        criteria = ('_was_num_respondents', '_was_average',
                 '_was_org_average', '_was_college_school_average',
                 '_was_uni_average')

        toAdd = ['instructor' + x for x in criteria]
        toAdd.extend(['course' + x for x in criteria])

        for name in toAdd:
            cisConstructorDict[name] = float(rHelper[name])

        CIS.objects.create(**cisConstructorDict)

    if settings.AWS_ENVIRONMENT:
        os.remove(pathForFile)