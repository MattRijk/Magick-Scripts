import os
# '/home/matt/Desktop/all_finance_ebooks/'
directory = os.listdir('/home/matt/Desktop/ebooks/')

full = []

for d in directory:
	full.append('/home/matt/Desktop/ebooks/' + d)


for f in full:
	new = '/home/matt/Desktop/ebooks/' + os.path.basename(f.lower())
	new = new.replace(" ","_")
	new = new.replace("-","_")
	# new = 
	x = os.rename(f, new)
	# print(x)
	print(f)
	print(new)
	print(os.path.basename(f.lower()))