#!/bin/bash
for dire in $(find ./Data/ -mindepth 1 -maxdepth 1 -type d); do
#for dire in ./Data/*/; do
	echo "student dir: $dire"
	#cd $(realpath -s $dire)
	for filename in $(realpath -s $dire)/*.java; do
	#for filename in *.java; do
		echo "trimmed: $(realpath -s $filename)"
		echo "compiling $(realpath -s $filename)" >> output.txt
		javac $(realpath -s $filename) >> output.txt
		echo "
		      ***********
		      ***********
		      RUNNING
		      ***********
		      ***********"
		      /home/christian/Desktop/JavaTASpring2021/scripting/javaScripting $(realpath -s $filename)
   
	done
	cd ..
done

	
