# Christian's C++ Grading Script

## Recent Updates
### UPDATE VER 3.0 - FEBRUARY 2, 2022
- Focus moved to running c++ programs
### UPDATE VER 2.2 - NOVEMBER 8, 2021
- Update for support for Lab 5 grading

### UPDATE VER 2.1 - OCTOBER 25, 2021
- Update for support for Lab 4 grading
- Because students will name their files different things, this will run the inputs for magic 8 ball and for passrun on all 3 of the java files. This means some of the outputs will be weird, so simply look for when the expect script name lines up with the student's java file name, and skip over weird outputs.


### MAJOR UPDATE VER 2.0 - OCTOBER 7, 2021
- Update for support for Lab 3 grading
Currently, the update for canvas api integration has been added. If you choose not to use it, then ignore this and use the script like usual.
This is how to use the new update:
- You must get an api key from your canvas page. 
- Click your icon on your home page
- Go to settings
- Scroll down to approved integrations
- Click add a new access token
- Give it a purpose / expiration date
- Hit generate and copy the token to your clipboard
- Now enter the directory where you store javaGradingScript.sh
- edit the .txt file named: "apiKey.txt", and paste your access token and save
- Go into students.txt and edit the student names to be the names of your students
- edit assignmentToGrade to be the assignment you would like to grade
- now run the script and wait.
- NOTE: there is not edge-case support for students that do not follow the format of putting all their .java files into a SINGLE zipped folder. That will come soon.
- If your students do not follow that process, run canvasStudentSubmissionPuller.py and then fix their directories. Then remove this from javaGradingScript.sh:
```
# call the python canvas puller
python3 canvasStudentSubmissionPuller.py
```

New dependencies for the script are for python if you choose to use the canvas api portion. To install them, use these commands:
```
pip install wget
```
```
pip install canvasapi
```

### UPDATE 1.9 - SEPTEMBER 20, 2021
The most recent update adds support for Lab 2 for the fall semester.

The thing to look out for is that, because students will change the .java file names, there can be no assumptions made.

This means that all of the expect scripts are run on all of the java files. It should be easy to decipher which one is meant to be done, so just look for the one valid output in "output.txt". There will be 12 different attempts at running the program all put to the same output.txt, and 3 will be valid, assuming the student coded it correctly. This is because, though the students are SUPPOSED to name their java files the way we tell them to, inevitably they will not. So, because looking through a text file a little longer is more time-efficient than re-running a program, this is how it will be done.

## So, How do I use this?

### Setting up dependencies

The three dependencies for this script are bash, expect, unzip, and unrar.

#### For mac users, go into a terminal and type:
```
brew install bash
```
```
brew install expect
```
```
brew install unzip
```
```
brew install unrar
```

#### as for linux:
```
sudo apt install bash
```
```
sudo apt-get install expect
```
```
sudo apt-get install unzip
```
```
sudo apt install unrar
```

#### And if you use Windows, you are dead to me. Figure it out with powershell or something.

### Getting the Student's files and setting up the script environment

Within your folder where you download this repository, you should create a folder, and name it "Data".

Since support for the unzipping / unraring of files has been added, all you must do is copy the .zip and .rar files of the students you wish to grade into the folder labeled "Data"

### giving the scripts permissions to run

Now, in order to run any bash and expect scripts, you must give your computer permission to run them. This is for security purposes, and I promise I'm not giving you malware :)

to do this, run these commands while in the repo's directory:

```
chmod +x ./drivingcost.exp
chmod +x ./gradecalculator.exp
chmod +x ./ruleof72.exp
chmod +x ./javaGradingScript.sh
```

Now, to run the script, simply execute:
```
./javaGradingScript.sh
```

## How to get the output?

outputs are sent to a text file named output.txt.

Each output for each student is put into their respective directory. Here is an example path:

./Data/LastnameFirstname_1234567/output.txt

