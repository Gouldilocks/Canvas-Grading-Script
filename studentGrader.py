from canvasapi import Canvas, account
# Script used to more quickly enter grades for students.

# Canvas setup
API_URL = 'https://smu.instructure.com/'
keyfile = open('apiKey.txt', 'r')
API_KEY = keyfile.readline()
canvas = Canvas(API_URL, API_KEY)
account = canvas.get_current_user()

assignmentFile = open('dontEditMe.txt','r')

courses = [canvas.get_course(88098),canvas.get_course(88136),canvas.get_course(88117),canvas.get_course(88140)]
# Get an assignment
for course in courses: # loop over all 4 assignments from the 4 classes
  assignment = course.get_assignment(int(assignmentFile.readline()))
  print("assignment is: " + str(assignment))
  for line in assignmentFile:
        line = line.rstrip('\n')
        if line == '*':      
            break
        else:
          submission = assignment.get_submission(line) # get the submission of the student id specified
          users = course.get_users(enrollment_type=['student'])
          studentName = None
          for x in users:
            if x.id == int(line):
              studentName = x.name
          # Print the student's output
          filepath = './Data/' + studentName.replace(" ", "") + '/output.txt'
          output = open(filepath,'r')
          for l in output:
            l = l.rstrip('\n')
            print(l)
          score = input("What score would you like to give this submission?")
          submission.edit(submission={'posted_grade':int(score)})

# Student setup
students = []
studentFile = open('students.txt', 'r')
for line in studentFile:
  line = line.rstrip('\n')
  students.append(line)
print("grading these students:")
print("-----------------------")
for i in students:
  print(i)




