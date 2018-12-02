#!/usr/bin/python


input_file = "input.txt"
total = 0
runningTotal = []

reccurantFreqTrigger = False

with open(input_file, "r+") as f:
	input_string = f.readlines()

# remove whitespaces/newlines
input_string = [x.strip().replace("\n","") for x in input_string] 

while reccurantFreqTrigger == False:
	for num in input_string:
		print("Current freq\t" + str(total) + ", change of [" + str(num) + "]")
		if total in runningTotal:
			reccurantFreqTrigger = True
			print("Found recurrant freq:\t" + str(total))
			exit()
		runningTotal.append(total)
		total += int(num)		
		print ("Resulting Frequency\t" + str(total) + "\n")
		
	
	

print("Total:\t" + str(total))

