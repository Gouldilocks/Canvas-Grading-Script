# Christian's Java Scripting program

## So, How do I use this?

### Getting the Student's files

Firstly, you must download all students folders with their projects and unzip the folders with their java programs.

Some students tend to put their java files within subdirectories within their zipped folders, so you must fix that.

the folders for each student should end up somewhat like this if they follow the correct protocol: LastnameFirstname_1234567 or something along those lines.

and inside that folder should be their .java and .class files. The .class files are not necessary, as this script compiles regardless due to possible java version mismatch

### Setting up the directory paths

Now within your folder where you download this repository, you should create a folder, and name it "Data".

Inside this folder, you should put each of the directories where each of the students .java files are.

The path to each .java file should look something like this: ./Data/LastnameFirstname_1234567/runme.java

### giving the scripts permissions to run

Now, in order to run any bash and expect scripts, you must give your computer permission to run them. This is for security purposes, and I promise I'm not giving you malware :)

to do this, run these commands while in the directory where you downloaded this repo:

```
chmod +x ./myscript.sh
chmod +x ./script.exp
```

Now, to run the script, simply execute:
```
./myscript.sh
```

## How to get the output?

outputs are put in a text file named output.txt.

Each output for each student is put into their respective directory. Here is an example path:

./Data/LastnameFirstname_1234567/output.txt

You will notice that at the bottom of the text file there is a lot of unnecessary 'l's and 'h's, which is because I have the expect

script run 100 of them, in order to confirm that the game would have ended. simply scroll up and you have your output!

