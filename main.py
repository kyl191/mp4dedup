import hash, mp4, os, sys, re
from os.path import join

def hashMP4(filename):
	file = open(filename, 'r')
	try:
		mp4.isMP4(file)
	except Exception as e:
		# So far the only exception is an invalid MP4 header found, so not much to grab
		print(e)
		return
	tempfile = mp4.stripMetadata(file)
	#print os.path.exists(tempfile.name)
	hashresult = hash.sha512file(tempfile.name)
	#print tempfile
	tempfile.close()
	os.remove(tempfile.name)
	
# Initial setup of search path
os.chdir(sys.argv[1])
# End initial setup

# Walk the directory structure looking for MP4 files
for root, subfolders, files in os.walk('.'):
	# Mention what path we're working in.
	print("Working in", os.path.abspath(root))
	# Since root contains the working folder, and we'll move onto subfolders later, 
	# We only care about the filename
	for filename in files:
		# So, for each file, check if it has an MP4 extension
		if re.search(".mp4",filename,re.IGNORECASE):
			# If is does, check if it possibly has a naively named dup
			(filenameprefix, dot, filenamesuffix) = filename.rpartition(".")
			dup = filenameprefix + "_2." + filenamesuffix
			if os.path.exists(dup):
				hash1 = hashMP4(os.path.abspath(join(root,filename)))
				hash2 = hashMP4(dup)
				if hash1 == hash2:
					print "Removing " + dup + "!"
					#os.remove(dup)
