# Christian's Java Scripting program

## So, How do I use this?

### Setting up dependencies

The two dependencies for this script are bash and expect.

#### For mac users, go into a terminal and type:
```
brew install bash

brew install expect

brew install unzip
```

#### as for linux:

```
sudo apt-get install expect

sudo apt install bash

sudo apt-get install unzip
```

### Getting the Student's files

Firstly, you must download all students folders with their projects and unzip the folders with their java programs. (support for auto-unzipping coming soon)

Some students tend to put their java files within subdirectories within their zipped folders, so you must fix that.

the folders for each student should end up somewhat like this if they follow the correct protocol: LastnameFirstname_1234567 or something along those lines.

and inside that folder should be their .java and .class files. The .class files are not necessary, as this script compiles regardless due to possible java version mismatch

### Setting up the directory paths

Now within your folder where you download this repository, you should create a folder, and name it "Data".

Inside this folder, you should put each of the directories where each of the students .java files are.

The path to each .java file should look something like this: ./Data/LastnameFirstname_1234567/runme.java

I have added an example "Data" directory for reference

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

