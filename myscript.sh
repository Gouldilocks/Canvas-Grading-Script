#!/bin/bash
for dire in ./Data/*/; do
	echo "student dir: $dire"
	for filename in $(realpath -s $dire)/*.java; do
		echo "trimmed: $(realpath -s $filename)"
		echo "compiling $(realpath -s $filename)" >> output.txt
		javac $(realpath -s $filename)
		echo "
		      ***********
		      ***********
		      RUNNING
		      ***********
		      ***********"
		      #script.exp >> output.txt
		java $(realpath -s $filename) >> output.txt
   
	done
done

	
