#!/usr/bin/python
import sys, random

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def read_this_line(fname, line_number):
	line_count = 0
	with open(fname) as f:
	        for i, l in enumerate(f):
	        	
	        	if line_count == line_number:
	        		return l
	        	else:
		        	line_count= line_count + 1
		        	pass


def get_random_color():
#	if len(sys.argv) > 1:
#		fname = sys.argv[1]
#	else:
#		fname = "none.txt"

	fname = "../lib/colors.txt"
	random_line = random.randrange(0,file_len(fname)-1)

	return  read_this_line(fname, random_line)


#print get_random_color()
