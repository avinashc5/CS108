#!/usr/bin/env bash

ls -R $1 | grep -E "^.*\.py" > output.txt
ls -R $1 | grep -c -E "^.*\.py"

rm -f log.txt

while IFS= read -r line
do
	echo "Deleted $line" >> log.txt
done < output.txt

echo -n "" >> log.txt

rm -f output.txt
rm -f testfolder/*.py
