#!/bin/bash
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
pushd ./Data/
	for zip in *.zip
	do
	  dirname=`echo $zip | sed 's/\.zip$//'`
	  if mkdir "$dirname"
	  then
	    if cd "$dirname"
	    then
	      unzip ../"$zip"
	      cd ..
	      rm -f $zip # Uncomment to delete the original zip file
	    else
	      echo "Could not unpack $zip - cd failed"
	    fi
	  else
	    echo "Could not unpack $zip - mkdir failed"
	  fi
	done		
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

	
