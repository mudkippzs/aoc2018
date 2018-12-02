#!/usr/bin/python


input_file = "input.txt"
total = 0

with open(input_file, "r+") as f:
	input_string = f.readlines()

# remove whitespaces/newlines
input_string = [x.strip().replace("\n","") for x in input_string] 

for num in input_string:
	total += int(num)

print("Total:\t" + str(total))

