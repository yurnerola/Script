#!/bin/bash
for dir in `ls -t`;do
	echo $dir;
	for file in `ls -t $dir|grep xsh`;do
		echo $file|sed 's/.xsh//g';
	done;
done;
