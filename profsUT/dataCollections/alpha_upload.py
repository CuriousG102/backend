import copytext
import pytz
import requests

from dataCollections.models import Instructor, Course, CourseTime
from profsUT import settings

from datetime import time
import os

# known problems: 
# - when a course time is changed, the new course time will be
# added to the course but the old one will also remain
# - when a course is cancelled it will not be deleted from the database
# - we are not taking cross listings into account
# - we nwo have info on building and room number and we may want to use that
def tableToDatabase(inFileURL):
    pathForFile = os.path.join(settings.BASE_DIR, 'csvToDatabaseTemp.csv')
    r = requests.get(inFileURL)
    with open(pathForFile, 'wb') as f:
        f.write(r.content)

    copy = copytext.Copy(pathForFile)
    sheet = copy['courses']
    for row in sheet:
        # we only want Journalism for now
        if row['Dept'] != 'J' or len(row['Instructor']) == 0: continue 

        # We don't currently have a use for courses without instructors
        if len(row['Instructor']) == 0: continue

        instructorLastName = row['Instructor'].split(', ')[0]
        instructorFirstName = row['Instructor'].split(', ')[1]

        instructor, created = Instructor.objects.get_or_create(last=instructorLastName, 
                                         first = instructorFirstName)

        uniqueNo = row['Unique']
        number_season_mappings = { # numbers in the data dumps we get to seasons
            2:'SP',
            6:'SU',
            9:'FA',
        }
        semesterSeason = number_season_mappings[int(row['Semester'])]
        semesterYear = int(row['Year'])
        course, created = Course.objects.get_or_create(uniqueNo=uniqueNo, 
                                     semesterSeason=semesterSeason,
                                     semesterYear=semesterYear,
                                     defaults={'courseName': row['Title'],
                                               'courseID': ' '.join((row['Dept'], row['Course Nbr'])),
                                               'uniqueNo': row['Unique'],
                                               'instructor': instructor})
        timezone = pytz.timezone('US/Central')

        startTime = timezone.localize(datetime.strptime(row['From'], '%H\%M').time())
        endTime = timezone.localize(datetime.strptime(row['To'], '%H\%M').time())

        dayStringNeeded = row['Days']
        SuBool, SBool, FBool, ThBool, WBool, TBool, MBool = False, False, False, False, False, False, False

        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'U':
            SuBool = True
            dayStringNeeded = dayStringNeeded[:-2]
        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'S':
            SBool = True
            dayStringNeeded = dayStringNeeded[:-1]
        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'F':
            Fbool = True
            dayStringNeeded = dayStringNeeded[:-1]
        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'H':
            ThBool = True
            dayStringNeeded = dayStringNeeded[:-2]
        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'W':
            WBool = True
            dayStringNeeded = dayStringNeeded[:-1]
        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'T':
            TBool = True
            dayStringNeeded = dayStringNeeded[:-1]
        if len(dayStringNeeded) > 0 and dayStringNeeded[-1] == 'M':
            MBool = True
            dayStringNeeded = dayStringNeeded[:-1]

        courseTime, created = CourseTime.objects.create(course = course,
                                                        time  = timeObjBegin,
                                                        endTime  = timeObjEnd,
                                                        m = MBool,
                                                        t = TBool,
                                                        w = WBool,
                                                        th = ThBool,
                                                        f = FBool,
                                                        s = SBool,
                                                        su = SuBool)


    os.remove(pathForFile)