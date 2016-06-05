import os
import PythonMagick

directory = os.listdir('/home/matt/Desktop/new/')
print(directory)
r = []
for d in directory:
	r.append('/home/matt/Desktop/new/' + d)

print(r)

n = 0
for filename in r:

	formatted_file = filename + "[0]"
	# newfile = "new_file%d" % (n)
	newfile = os.path.basename(filename.lower()[:-4])

	# print(formatted_file)
	# print(newfile)
	# print("/home/matt/Desktop/new/"+newfile+".png")
	img = PythonMagick.Image()
	img.density("300")

	# img.read("/home/matt/Desktop/Learning Raspbian.pdf[0]")
	# img.write("/home/matt/Desktop/New_Raspbian.png")

	img.read(formatted_file)
	img.write("/home/matt/Desktop/new_jpgs/"+newfile+".png")
	n+=1