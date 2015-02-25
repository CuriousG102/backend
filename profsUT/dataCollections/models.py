import os
from datetime import date

from django.db import models

# Create your models here.
class Instructor(models.Model):
    last = models.CharField(max_length=50)
    first = models.CharField(max_length=50)
    bio = models.TextField(verbose_name='Short biography of the professor', 
                           null=True)

class Course(models.Model):
    courseName = models.CharField(max_length=50)
    uniqueNo = models.IntegerField(verbose_name="Course Unique Number")

    #only PDFs will be allowed
    syllabus = models.FileField(upload_to='syllabi', null=True)
                                  
    instructor = models.ForeignKey('Instructor')
    inst_provided_description = models.TextField(verbose_name='Instructor Provided Description',
                             help_text="Description for the course provided by the Instructor", 
                             null=True)
    reg_provided_description = models.TextField(verbose_name='Registrar Provided Description',
                                    help_text="Description (text) provided by registrar",
                                    null=True)
  
    FALL = 'FA'
    SPRING = 'SP'
    SUMMER = 'SU'
    
    SEMESTER_CHOICES = (
        (FALL, 'Fall'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
    )

    endYear = date.today().year + 1
    YEAR_CHOICES = []
    for year in range(2008, endYear):
        YEAR_CHOICES.append((year, year)) 
    
    semesterSeason = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    semesterYear = models.IntegerField(max_length=4, choices=YEAR_CHOICES,
                                       default=date.today().year)

class CourseTime(models.Model):
    course = models.ForeignKey('Course')

    m = models.BooleanField(verbose_name='Monday', default=False)
    t = models.BooleanField(verbose_name='Tuesday', default=False)
    w = models.BooleanField(verbose_name='Wednesday', default=False)
    th = models.BooleanField(verbose_name='Thursday', default=False)
    f = models.BooleanField(verbose_name='Friday', default=False)
    s = models.BooleanField(verbose_name='Saturday', default=False)
    su = models.BooleanField(verbose_name='Sunday', default=False)

    time = models.TimeField(verbose_name='Course Time')

class Question(models.Model):
    text = models.TextField(verbose_name="Question text")

class Response(models.Model):
    question = models.ForeignKey(Question)
    instructor = models.ForeignKey(Instructor)
    text = models.TextField(verbose_name="Response text")


