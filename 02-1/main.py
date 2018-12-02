#!/usr/bin/python
import collections

input_file = "input.txt"

with open(input_file, "r+") as f:
	input_data = f.readlines() # Read lines into list

d_count = 0 # count occurance of doubles
t_count = 0 # count occurance of triples

for string in input_data: # iterate through input strings	
	d = collections.defaultdict(int) # build alphabet dict
	for c in string.replace("\n",""): # iterate letters in string
		d[c] += 1 # count the hits
	
	for c in sorted(d, key=d.get, reverse=True): # checking for doubles
		if d[c] == 2: # if any letter has a count of 2
			d_count += 1 # count the occurance
			break # ignore more than one 'double'

	for c in sorted(d, key=d.get, reverse=True):
		if d[c] == 3:
			t_count += 1
			break

checksum = d_count * t_count # calculate the checksum

print '%d Doubles, %d Triples' % (d_count,t_count)
print 'Checksum:\t %s' % (checksum)