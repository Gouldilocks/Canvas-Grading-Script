#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
# use the directory stack to get to ./Data/
pushd ./Data/
	# for all .zip files in the current directory
	for zip in *.zip
	do
	  # set the directory name to be used
	  dirname=`echo $zip | sed 's/\.zip$//'`
	  # make the directory with the proper name if possible
	  if mkdir "$dirname"
	  then
	    # change directories to the new directory where the files will be unzipped into
	    if cd "$dirname"
	    then
	      # unzip the file and then leave the directory it zips to
	      unzip ../"$zip"
	      cd ..
	      # delete the old .zip file just to save space on user's computer
	      rm -f $zip
	    else
	      # error message for unzipping file
	      echo "Could not unpack $zip - cd failed"
	    fi
	  else
	    # error message for making a new directory
	    echo "Could not unpack $zip - mkdir failed"
	  fi
	done
	
	# do the same for .rar files
	# for all .zip files in the current directory
	for rar in *.rar
	do
	  # set the directory name to be used
	  dirname=`echo $rar | sed 's/\.rar$//'`
	  # make the directory with the proper name if possible
	  if mkdir "$dirname"
	  then
	    # change directories to the new directory where the files will be unzipped into
	    if cd "$dirname"
	    then
	      # unzip the file and then leave the directory it zips to
	      unrar e ../"$rar"
	      cd ..
	      # delete the old .zip file just to save space on user's computer
	      rm -f $rar
	    else
	      # error message for unzipping file
	      echo "Could not unpack $rar - cd failed"
	    fi
	  else
	    # error message for making a new directory
	    echo "Could not unpack $rar - mkdir failed"
	  fi
	done
		
# pop ./Data/ off the directory stack
popd

# loop over all subdirectories
for dire in $(find ./Data*/ -mindepth 1 -maxdepth 1 -type d); do

	# save the home directory in order to access exp script later
	fullDir=$PWD
	
	# cd into the student's directory
  	cd $(realpath -s $dire)
  	echo "cd into $dire"
  	
  	rm *.class
  	# loop over all launcher .java file
	for filename in $(ls *.java); do
	
		# put name of student to output file
		echo "compiling $(realpath -s $filename)" >> output.txt
		
		# compile java program
		javac $(realpath -s $filename)
		
		# print to console which student program is running
		echo "RUNNING $dire"
		
			# remove all exterior except class name (i.e. turn "./Grade.java" to "Grade")
			y=${filename%.java}  
			# run the expect script and output to file in subdirectory
			$fullDir/script.exp $y >> output.txt 
			
	done # end inner for loop
	
	# get out of the subdirectory and go back to home directory
	cd ..
	cd ..
done # end outer for loop

	
