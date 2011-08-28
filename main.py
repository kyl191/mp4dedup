import hash, os, sys, re
from os.path import join

def hashAndAdd(file):
	# Check if it's a valid MP3 file first by trying to get the ID3 info
	try:
		title, artist, album = mp3.getid3(file)
	except Exception as e:
		# So far the only exception is an invalid ID3 header found, so not much to grab
		print(e)
		return
	# Gets back a tuple with (count of rows, mtime)
	# Check if the file has already been hashed
	if exists > 0:
		# If the file hasn't been modified since it was checked, don't bother hashing it
		if dbmtime >= mtime:
			return
		else:
			# Need to come up with an update statement...
			print("Updating", file)
			update = True
	
	tempfile = mp3.stripid3(file)
	hashresult = hash.sha512file(tempfile[1])
	os.close(tempfile[0])
	os.remove(tempfile[1])
	
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
			# If is does, hash & add it to the db
			hashAndAdd(os.path.abspath(join(root,filename)))
