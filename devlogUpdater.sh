#!/bin/bash

git pull

timestamp()
{
	time=$(date +%T)
}

# User input for first name
echo "Enter your first name:"
read first

if [ ! $first ]
then
	echo "Please provide an input"
	exit
fi

# User input for last name
echo "Enter your last name:"
read last

if [ ! $last ]
then
	echo "Please provide an input"
	exit
fi

# User input for update section
echo "Enter your update:"
read update

if [ ! $update ]
then
	echo "Please provide an input"
	exit
fi

# Convert last name to all lowercase
last="$( echo $last | tr '[:upper:]' '[:lower:]')"
# Convert firstname to all uppercase
first="$( echo $first | tr '[:lower:]' '[:upper:]')"
timestamp
header="$last${first:0:1} -- $time"

echo $header >> devlog.txt
echo $update >> devlog.txt
echo  >> devlog.txt

git add devlog.txt
git commit -m "Updated devlog"
git push