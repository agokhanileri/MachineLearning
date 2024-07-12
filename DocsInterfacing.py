# import x
# import pyautogui   --> after setting Ctrl+L to clear all in preferences
# pyautogui.hotkey('command', 'l')

import os
# import numpy as np\
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlrd

os.chdir("../input")\
# pwd
# a = 5  --> how to echo a? 
# make % also comment

# Import from CSV
students = pd.read_csv("mydata.csv")   # direct read, assumes the header

# Import from Excel
students = pd.read_excel('./mydata.xlsx', sheetname='Sheet1')  # direct read
r, c = students.shape
                          # alternative

# with XLRD
wb = xlrd.open_workbook("./mydata.xlsx")   # open the work book
sheet = wb.sheet_by_index(0)        # get the sheet
sheet.cell_value(1, 0)              #
sheet.row_values(1)                 # doesn't assume the header


students['Name'] = students['Name'].str.lower()
students.head()

students['Role'].value_counts()     # show

students['Role'].value_counts().to_frame()


###
book = xlrd.open_workbook('excelfile.xls')
print(book.sheet_names())

for sheet in book.sheets():
   print(sheet.name, sheet.nrows, sheet.ncols)
   
   for irow in range(sheet.nrows):
       
      for icol in range(sheet.ncols):
         print(irow, icol, sheet.cell(irow, icol).value)
         
sheet = book.sheet_by_index(2)
sheet = book.sheet_by_name('sheet 1')