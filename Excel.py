# import x

book = xlrd.open_workbook('excelfile.xls')
print(book.sheet_names())

for sheet in book.sheets():
   print(sheet.name, sheet.nrows, sheet.ncols)
   
   for irow in range(sheet.nrows):
       
      for icol in range(sheet.ncols):
         print(irow, icol, sheet.cell(irow, icol).value)
         
sheet = book.sheet_by_index(2)
sheet = book.sheet_by_name('sheet 1')