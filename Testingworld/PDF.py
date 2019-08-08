import PyPDF2

file = open('C:\\Users\\Bilal\\PycharmProjects\\TestingAutomation\\PDF\\Testcases.pdf','rb')

pdfreader = PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())

pageobj = pdfreader.getPage(0)
print(pageobj.extractText())

file.close()

