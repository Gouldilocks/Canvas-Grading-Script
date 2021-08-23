# Christian's Java Grading Script

## So, How do I use this?

### Setting up dependencies

The three dependencies for this script are bash, expect, and unzip. To be added is support for .rar files, but that will be in a future update, as very few students use .rar files

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

#### And if you use Windows, you are dead to me. Figure it out with powershell or something.

### Getting the Student's files and setting up the script environment

Within your folder where you download this repository, you should create a folder, and name it "Data".

Now that support for the unzipping of files has been added, all you must do is copy the .zip folders of the students you wish to grade into the folder labeled "Data"

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

