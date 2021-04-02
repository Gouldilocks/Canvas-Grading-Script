#!/bin/bash
for dire in $(find ./Data/ -mindepth 1 -maxdepth 1 -type d); do
	fullDir=$PWD
  	cd $(realpath -s $dire)
	for filename in $(ls *.java); do
		echo "compiling $(realpath -s $filename)" >> output.txt
		javac $(realpath -s $filename) >> output.txt
		echo "
		      ***********
		      ***********
		      RUNNING $dire
		      ***********
		      ***********"
			y=${filename%.java}  
			$fullDir/script.exp $y >> output.txt 
	done
	cd ..
	cd ..
done

	
