# gets titles from files and assigns them to a new file.

# format titles to all lowercase with underscore seperation.




from pyPdf import PdfFileReader
import os

directory = os.listdir('/home/matt/Desktop/new/')



full = []

for d in directory:
	full.append('/home/matt/Desktop/new/' + d)

for f in full:
	f = f.lower()
	f = f.replace(" ","_")
	f = f.replace("-","_")
	print(f)

for filename in full:
	input1 = PdfFileReader(file(filename, 'rb'))
	title = input1.getDocumentInfo().title
	print title

for f in full:
    print(os.path.basename(f[:-4]))



>>> myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
>>> for filename in myFiles:
        print(os.path.join('C:\\Users\\asweigart', filename))

path = 
for f in full:

    filename = "myfile.txt"
    path_to_file = pjoin("C:", "foo", "bar", "baz", filename)
    FILE = open(path_to_file, "w")


from pyPdf import PdfFileReader

# p = '/home/matt/Desktop/new/The_Warren_Buffett_Way.pdf'
p = '/home/matt/Desktop/new/the_mckinsey_way.pdf'

pdf = PdfFileReader(file(p, 'rb'))
if pdf.isEncrypted:
    pdf.decrypt('')
pdf.documentInfo
pdf.getNumPages()
267
info = pdf.getDocumentInfo()

info.author
info.title


p = '/home/matt/Desktop/new/The_McKinsey_Way.pdf'

pdf = PdfFileReader(file(p, 'rb'))
if pdf.isEncrypted:
	try:
	    pdf.decrypt('')
	    print 'File Decrypted (PyPDF2)'
	    info = pdf.getDocumentInfo()
	except:
		info = pdf.getDocumentInfo()


import os
for filename in os.listdir('/home/matt/Desktop/new/'):
    info = os.stat(filename)
    print info


from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

import os
for filename in os.listdir('/home/matt/Desktop/new/'):
	fp = open('/home/matt/Desktop/new/'+filename, 'rb')
	parser = PDFParser(fp)
	doc = PDFDocument(parser)

	print doc.info  # The "Info" metadata
	print();

from os.path import join as pjoin
filename = "myfile.txt"
path_to_file = pjoin("C:", "foo", "bar", "baz", filename)
FILE = open(path_to_file, "w")

# loop over files in directory
import os

directory = os.listdir('/home/matt/Desktop/new/')



full = []

for d in directory:
	current_path = '/home/matt/Desktop/new/' + d
	full.append(current_path)

# for f in full:
# 	f = f.lower()
# 	f = f.replace(" ","_")
# 	f = f.replace("-","_")
# 	print(f)

for f in full:
	# do something

	new_destination='/home/matt/Desktop/new/new_folder/'
	# FILE = open(path_to_file+d, "w")
	new_destination = new_destination+d.lower()
	# current = f
	print(f)
	print(new_destination)
	# print(current_path);

	shutil.move(f, new_destination)