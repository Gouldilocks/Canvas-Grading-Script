# Christian's Java Grading Script

## Recent Updates
The most recent update adds support for Lab 2 for the fall semester.

The thing to look out for is that, because students will change the .java file names, there can be no assumptions made.

This means that all of the expect scripts are run on all of the java files. It should be easy to decipher which one is meant to be done, so just look for the one valid output in "output.txt".

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

outputs are sent to a text file named output.txt.

Each output for each student is put into their respective directory. Here is an example path:

./Data/LastnameFirstname_1234567/output.txt

