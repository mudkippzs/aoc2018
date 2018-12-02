#!/usr/bin/python
import collections

input_file = "input.txt"

with open(input_file, "r+") as f:
	input_data = f.readlines() # Read lines into list

found = 0 # exit flag

# remove whitespaces/newlines
input_data = [x.strip().replace("\n","") for x in input_data] 

def diff_count(a, b): # easy way to count the differences between strings
	return sum(x!=y for x,y in zip(a,b)) # sum totals the results of the list comprehension compairing a and b

for string1 in input_data: # iterate through input strings
	for string2 in input_data:
		if diff_count(string1, string2) == 1: # if our difference is exactly 1, we have the correct 'set' of box IDs
			found = 1 # trigger the exit condition
			print 'Strings with 1 diff: %s and %s' % (string1, string2) # print out the differing strings
			break
		
	if found > 0: # check exit flag for loop
			break