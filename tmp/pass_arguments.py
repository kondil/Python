#!/usr/bin/env python

# This is a test on passing arguments to our python scripts.

import sys, getopt

print 'Num of args :: ', len(sys.argv)
print 'Argument List :: ', str(sys.argv)
print 'Argument List :: ', sys.argv
print type(sys.argv[1])

# For now I will use it as is. For further info one can visit :: 
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm


def input(argv):

	print "Input function was called."

	inputFile = ''
	outputFile = ''

	try:
		opts, args = getopt.getopt(argv,"hi:o:",["help","input=","output="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		sys.exit(2)

 	for opt, arg in opts:
 		if opt in ("-h", "--help"):
 			print 'test.py -i <inputfile> -o <outputfile>'
 			sys.exit()
 		elif opt in ("-i", "--input"):
 			inputFile = arg
 		elif opt in ("-o", "--output"):
 			outputFile = arg
 			print 'Input file is "', inputFile
 			print 'Output file is "', outputFile


input(sys.argv[1:])
