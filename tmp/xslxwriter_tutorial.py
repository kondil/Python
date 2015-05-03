#!/usr/bin/env python

# This is a starting tutorial on xslxwriter. I don't need to use it write now, so I will stay here.

import xlsxwriter

workbook = xlsxwriter.Workbook('report.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Hello world')
workbook.close()
