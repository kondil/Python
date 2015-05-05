#!/usr/bin/env python

# This is a tutorial on how to create an xlsx Workbook using the Openpyxl library.

# How to create a new excel and write the data.

from openpyxl import Workbook

# Let's create a Workbook.
wb2 = Workbook()

# Let's grab the active Worksheet.
ws2 = wb2.active
ws2['A1'] = 42
ws2.append([1,2,3])
wb2.save("tmp.xlsx")

