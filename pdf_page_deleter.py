import PyPDF2
pdf1File = open('sideways_markets.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)

output = PyPDF2.PdfFileWriter()


page_range = range(pdf1Reader.numPages)
no_first_page = page_range[1:]


for pageNum in no_first_page:
	pageObj = pdf1Reader.getPage(pageNum)
	output.addPage(pageObj)

	outputStream = file('output.pdf', "wb")
	output.write(outputStream)
	outputStream.close()

# Merge two PDFs
# from PyPDF2 import PdfFileReader, PdfFileWriter
 
# output = PdfFileWriter()
# pdfOne = PdfFileReader(file( "some\path\to\a\PDf", "rb"))
# pdfTwo = PdfFileReader(file("some\other\path\to\a\PDf", "rb"))
 
# output.addPage(pdfOne.getPage(0))
# output.addPage(pdfTwo.getPage(0))
 
# outputStream = file(r"output.pdf", "wb")
# output.write(outputStream)
# outputStream.close()