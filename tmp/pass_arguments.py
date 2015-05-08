#!/usr/bin/env python

# This is a test on passing arguments to our python scripts.

import sys, getopt

# print 'Num of args :: ', len(sys.argv)
# print 'Argument List :: ', str(sys.argv)
# print 'Argument List :: ', sys.argv
# print type(sys.argv[1])
# 
# # For now I will use it as is. For further info one can visit :: 
# # http://www.tutorialspoint.com/python/python_command_line_arguments.htm

def help_message(scripts_name):
	# print "Input function was called."
	print scripts_name, ' -i <inputfile> -o <outputfile>'

def input(argv, inputFile, outputFile):
	inputFile = ''
	outputFile = ''

	try:
		opts, args = getopt.getopt(argv[1:],"hi:o:",["help","input=","output="])
	except getopt.GetoptError:
		print help_message(argv[0])
		sys.exit(2)

 	for opt, arg in opts:
 		if opt in ("-h", "--help"):
 			help_message(argv[0])
 			sys.exit()
 		elif opt in ("-i", "--input"):
 			inputFile = arg
 		elif opt in ("-o", "--output"):
 			outputFile = arg

def main(argv):
# 	inputFile = None
# 	outputFile = None

	input(argv, inputFile, outputFile)
	print 'Input file is ', inputFile
	print 'Output file is ', outputFile


if __name__ == "__main__":
	main(sys.argv)
