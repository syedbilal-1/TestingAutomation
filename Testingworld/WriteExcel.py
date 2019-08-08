import openpyxl

wk = openpyxl.Workbook()
sh = wk.active
sh.title = 'Test'

print(sh.title)
sh['A3'].value= "Testing.com"

#Second sheet is created
wk.create_sheet(title="Testing")
sh1 = wk['Testing']
sh1  ['A3'] = '9988776654'

#saving
wk.save('D:\\Writefile.xlsx')