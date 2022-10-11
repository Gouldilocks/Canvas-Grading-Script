import os

# Run all the canvas pieces in order
os.system("python3 canvasStudentSubmissionPuller.py")
os.system("./cleanupData.sh")
os.system("python3 studentGrader.py")