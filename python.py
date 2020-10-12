#!/usr/bin/python
import os, sys, base64, uuid, string


number_of_folders	= int(sys.argv[1])
number_of_files		= int(sys.argv[2])

#	makes the folders with random uuid4 names. 
for i in range(number_of_folders):
	foldername = str(uuid.uuid4())
	os.mkdir(foldername)
#	makes the files inside the folders with random uuid4 names.
	for i in range(number_of_files):
		filename = str(uuid.uuid4())
		f = open(foldername + '/' + filename, 'w+')
		random_base64 = base64.b64encode(str(uuid.uuid4()))
		f.write(random_base64 + random_base64)  #	writes random b64 string into the files twise.
#twise to make it easier to find hidden messages because of the repetition.
		f.close
 

