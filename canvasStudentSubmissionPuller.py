from canvasapi import Canvas, account
import requests
import urllib.request;
import wget
import json
from types import SimpleNamespace
import os
# set the canvas url and key
API_URL = 'https://smu.instructure.com/'

keyfile = open('apiKey.txt', 'r')
API_KEY = keyfile.readline()

logfile = open("logs.txt", "w")
logfile.write("Starting Script Now")
 
if not os.path.isdir('./Data'):
 os.mkdir('./Data')
 
assignmentids = open("dontEditMe.txt", "w")

students = []
 # Change student names here. Names must be capitalized first and last with space betweein like so:
studentFile = open('students.txt', 'r')
for line in studentFile:
  line = line.rstrip('\n')
  students.append(line)
print("grading these students:")
print("-----------------------")
for i in students:
  print(i)
assignmentToGrade = 'Lab 3'

# Create a canvas object
canvas = Canvas(API_URL, API_KEY)
 
# Create a user object
account = canvas.get_current_user()
 
# Print out all the users
courses =  [canvas.get_course(88098),canvas.get_course(88136),canvas.get_course(88117),canvas.get_course(88140)]
for course in courses:
 users = course.get_users(enrollment_type=['student'])
 assignments = course.get_assignments()
 for assignment in assignments:
   assignmentIndex = str(assignment).find('(')
   assignmentID = str(assignment)[assignmentIndex+1: assignmentIndex + 6]
   assignmentNAME = str(assignment)[0:assignmentIndex-1]
 
   if assignmentNAME == assignmentToGrade:
     assignmentids.write(str(assignment.id) + "\n")
     submissions = assignment.get_submissions()
     for submission in submissions:
       for user in users:
         # If the user id matches the submission
         if user.id == submission.user_id:
           # If it is a student that I grade
           if user.name in students:
             assignmentids.write(str(user.id) + "\n")
             logfile.write("student name: " + str(user.name) + "\n")
             print("user id: " + str(submission.user_id))
             print("student name: " + str(user.name))
             print("submission id: " + str(submission.user_id))
             # Get the url from the submission json (Which for some reason won't parse into a json.... thus the weird method)
             try:
               # If the student does what they are supposed to, and makes a single zip
               if len(submission.attachments) == 1:
                 filepath = './Data/' + user.name.replace(" ", "") + '.zip'
                 if not os.path.isfile(filepath):
                   for item in submission.attachments:
                     index = str(item).find('\'url\':')
                     index2 = str(item)[index + 10 : len(str(item))].find(',')
                     url = str(item)[index + 8 : index2 + index + 9]
                     logfile.write("url: " + url + "\n")
                     print("url: " + url)
                     wget.download(url, filepath)
               else:
                 filepath = './Data/' + user.name.replace(" ", "") + 'TOO_MANY_FILES'
                 if not os.path.isdir(filepath):
                   os.mkdir(filepath)
                   for item in submission.attachments:
                     index = str(item).find('\'url\':')
                     index2 = str(item)[index + 10 : len(str(item))].find(',')
                     url = str(item)[index + 8 : index2 + index + 9]
                     logfile.write("url: " + url + "\n")
                     print("url: " + url)
                     wget.download(url, filepath)
 
             except Exception as e:
               print(e)
               # If the student has no submission
               logfile.write("There were no submissions found for " + str(user.name) + "\n")
               print("there were no submissions found") 
 assignmentids.write("*\n")

