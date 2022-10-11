from canvasapi import Canvas, account
from helperFunctions import get_courses, get_courses_to_grade_names
# Script used to more quickly enter grades for students.
# Prints the user's output to the screen, takes input on grade and comments, and uploads them to canvas.

# Canvas setup
students = []
ungradedStudents = []
ungradedStudentNames = []
API_URL = 'https://smu.instructure.com/'
keyfile = open('apiKey.txt', 'r')
API_KEY = keyfile.readline()
canvas = Canvas(API_URL, API_KEY)
account = canvas.get_current_user()

assignmentFile = open('dontEditMe.txt','r')

courseNames = get_courses_to_grade_names()
courses = get_courses(courseNames, canvas)
# Get an assignment
studentName = None
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
          for x in users:
            if x.id == int(line):
              studentName = x.name
          # Print the student's output
          if submission.score is not None:
            print(studentName + "'s Project has already been graded. Skipping.")
            students.append(studentName + ' grade: ' + str(submission.score))
            continue
          # Run all the programs of that student
          filepath = './Data/' + studentName.replace(" ", "") # Path to the student's folder
          try:
            # Run the students programs
            run_all_programs(filepath)

            print("You are grading " + studentName)
            print("current grade is: " + str(submission.score))
            comment = input("What comment would you like to give? Type 'skip' to skip: ")
            if comment == 'skip':
              students.append(studentName + ' grade: ' + str(submission.score))
              continue
            else:
              fileP = './comment.txt'
              commentFile = open(fileP,'w')
              commentFile.write(comment)
              commentFile.close()
              submission.upload_comment('comment.txt')
            score = input("What score would you like to give this submission? or type 'skip' to skip grading: ")
            if score == 'skip':
              pass
            else:
              submission.edit(submission={'posted_grade':int(score)})
          except:
            print("student output was not found for " + studentName)
            ungradedStudents.append(submission)
            ungradedStudentNames.append(studentName)
          students.append(studentName + ' grade: ' + str(submission.score))


# Print out all the grades for the students
for student in students:
  print(student)

answer = input("would you like to grade students who do not have a grade? (y) or (n)")
if(answer == 'y'):
  for i in range(len(ungradedStudents)):
    answer = input('Would you like to grade ' + ungradedStudentNames[i] + "? (y) or (n)")
    if answer == 'y':
      comment = input("What would you like to comment? Type 'skip' to skip comment: ")
      if comment == 'skip':
        pass
      else:
        fileP = './comment.txt'
        commentFile = open(fileP,'w')
        commentFile.write(comment)
        commentFile.close()
        ungradedStudents[i].upload_comment('./comment.txt')
      grade = input("What would you lke to give as a grade? Type 'skip' to skip grade: ")
      if grade == 'skip':
        pass
      else:
        ungradedStudents[i].edit(submission={'posted_grade':int(grade)})
    else:
      continue