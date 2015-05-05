#!/usr/bin/env python

# This is a tutorial on how to read an xlsx Workbook using the Openpyxl library.

# Let's read from a current excel file.
# - For this we will need to load 'load_workbook' from openpyxl.

from openpyxl import load_workbook

wb1 = load_workbook(filename='Nov.xlsx', read_only=True)

# In order to discover more info on the module, classes and objects we have loaded 
# we can use the commands dir() and help() like the next examples.
# dir(wb1)
# help(wb1)
# help(wb1.get_active_sheet)


# ws1 = wb1['Nov.csv']
# The following command will get us the active sheet of the workbook.
ws1 = wb1.get_active_sheet()

# print ws1.rows1
print ws1.dimensions
print ws1.max_column
print ws1.max_row

for row in ws1.rows1:
	print "=======================================\nNext Entry\n======================================="
	for cell in row:
		print cell.value
	print "=======================================\n"


