#!/usr/bin/env python
# This is a tutorial on how to create an xlsx Workbook using the Openpyxl library.
from openpyxl import Workbook

# Let's create a Workbook.
wb = Workbook()

# Let's grab the active Worksheet.
ws = wb.active
ws['A1'] = 42
ws.append([1,2,3])
ws1 = wb.create_sheet(0, 'tmp')
wb.get_sheet_names()
wb.save("tmp.xlsx")

