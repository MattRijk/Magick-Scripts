import os
# '/home/matt/Desktop/all_finance_ebooks/'
# 
directory = os.listdir('/media/matt/B149-6D09/all_finance_ebooks/')


full = []

for d in directory:
	full.append('/media/matt/B149-6D09/all_finance_ebooks/' + d)



for f in full:
	base = os.path.basename(f.lower())

	new = '/media/matt/B149-6D09/all_finance_ebooks/' + base.replace(" ","_")
	new = '/media/matt/B149-6D09/all_finance_ebooks/' + base.replace("-","_")
	new = '/media/matt/B149-6D09/all_finance_ebooks/' + base.replace(",", "")
	new = '/media/matt/B149-6D09/all_finance_ebooks/' + base.replace(",_", "_")
	new = '/media/matt/B149-6D09/all_finance_ebooks/' + base.replace("_,", "_")
	new = '/media/matt/B149-6D09/all_finance_ebooks/' + base.replace("__", "_")
	# do stuff


	# new = new.
	# new = new.replace("-","_")
	# new = new.replace(",", "")
	# new = new.replace(",_", "_")
	# new = new.replace("__", "_")

	x = os.rename(f, new)
	# print(x)
	# print(f)
	# print(new)
	# print(os.path.basename(f.lower()))

print('finished')