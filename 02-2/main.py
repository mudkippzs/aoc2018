#!/usr/bin/python
import collections

input_file = "input.txt"

with open(input_file, "r+") as f:
	input_data = f.readlines() # Read lines into list

found = 0

def diff_count(a, b):
	return sum(x!=y for x,y in zip(a,b))

for string1 in input_data: # iterate through input strings
	for string2 in input_data:
		if diff_count(string1, string2) == 1:
			found = 1
			print 'Strings with 1 diff: %s and %s' % (string1, string2)
			break
		
	if found > 0: 
			break