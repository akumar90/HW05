#!/usr/bin/env python
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the 
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def read_file(name):
	"""This method reads a file, splits each line to get the words.
		Then prints each word with more than 20 characters"""

	f = open(name, 'r')
	
	for line in f:  # Navigating through each line
		words = line.split() # Splitting each sentence into words

		for i in words:  # Looping through each word
			if(len(i.strip()) > 20):
				print (i.strip())



##############################################################################
def main():
    
    read_file("words.txt")
    
if __name__ == '__main__':
    main()
