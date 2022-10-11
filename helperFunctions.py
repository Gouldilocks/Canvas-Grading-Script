import os

def get_courses_to_grade_names():
  return ['CS1340-801-1227', 'CS1340-802-1227']


def get_assignment_to_grade():
   return 'Lab 2'


def get_courses(courses_to_grade_names, canvas):
  courses = []
  possible_courses = canvas.get_courses()

  for course in possible_courses:
    if course.name in courses_to_grade_names:
      courses.append(course)
  return courses


def unzipAllFiles(dir_name, extension):
  print(os.listdir(dir_name))
  for item in os.listdir(dir_name):  # loop through items in dir
    if item.endswith(extension):  # check for ".zip" extension
        file_name = dir_name + '/' + item  # get full path of files
        print("file name is: " + file_name)
        zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
        zip_ref.extractall(dir_name)  # extract file to dir
        zip_ref.close()  # close file
        os.remove(file_name)  # delete zipped file


def get_student_name(filename):
  split_by_slash = filename.split('/')
  last_string = split_by_slash[len(split_by_slash) - 1]
  split_by_dot = last_string.split('.')
  return split_by_dot[0]

def changeToRealPath(filepath):
  return filepath.replace(' ', '\ ').replace('(', '\(').replace(')', '\)')

# Runs all the python programs in the given directory
def run_all_python_in_directory(filepath):
  for filename in os.listdir(filepath):
    # print('filename: ' + filename)
    if filename.endswith(".py"):
      print("Running: " + filename)
      os.system("python3 " + changeToRealPath(filepath + filename))
      print("Finished running: " + filename)
      print("")

# call run_all_python_in_directory on all subdirectories
def run_all_programs(filepath):
  for filename in os.listdir(filepath):
      if filename.endswith(".py"):
        print("Running: " + filename)
        os.system("python3 " + changeToRealPath(filepath + filename))
        print("Finished running: " + filename)
        print("")
      if os.path.isdir(filepath + filename):
        # print('running all programs in: ' + filepath + filename)
        run_all_python_in_directory(filepath + filename + '/')
        run_all_programs(filepath + filename + '/')

# run_all_programs('Data/CristinaFerman/')