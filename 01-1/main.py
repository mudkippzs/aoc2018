#!/usr/bin/python

input_file = "input.txt"
checksum = 0 # set 

with open(input_file, "r+") as f:
	input_string = f.readlines()

# remove whitespaces/newlines
input_string = [x.strip().replace("\n","") for x in input_string] 

for num in input_string: # Sum checksum
	checksum += int(num)

print 'Checksum:\t %s' % (checksum)

