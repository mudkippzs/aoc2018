#!/usr/bin/python

input_file = "input.txt"
total = 0
runningTotal = []

reccurantFreqTrigger = False

with open(input_file, "r+") as f:
	input_string = f.readlines()

# remove whitespaces/newlines
input_string = [x.strip().replace("\n","") for x in input_string] 

while reccurantFreqTrigger == False: # keep iterating until we trigger this flag
	for num in input_string: # iterate the inputs
		if total in runningTotal: 
			reccurantFreqTrigger = True
			exit()
		runningTotal.append(total) # increase the running total
		total += int(num) # increase the total

print 'Total:\t %s' % (total)

