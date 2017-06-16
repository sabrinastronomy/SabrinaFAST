import os
import subprocess
import numpy as np
savedPath = os.getcwd()


def wget_folder(folder, files_wanted, website):	# Full output from monitoring file
	i = 1
	subprocess.call("mkdir " + folder, shell = True)
	os.chdir(folder)
	for file_name in files_wanted:
		print("wget " + website + folder + "/fil_files/" + file_name + " -O " + folder + "_" + str(i) + ".fil")
		subprocess.call("wget " + website + folder + "/fil_files/" + file_name + " -O " + folder + "_" + str(i) + ".fil", shell = True)
		i += 1
	os.chdir(savedPath)

if __name__ == "__main__":
	website = "http://supercomputing.swin.edu.au/datasharing/frb02/getfile.php?file=/"
	folders = ["FRB010125", "FRB010621", "FRB010724", "FRB110220", "FRB110626", "FRB110703", "FRB120127"]
	files_wanted_prefixes = ["BJ0009_025", "PM0141_017", "SMC021_008", "2011-02-20-01:52:19.fil", "2011-06-26-21:31:05.fil", "2011-07-03-18:57:42.fil", "2012-01-27-08:08:14.fil"]
	files_wanted_suffixes = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D"]
	files_wanted_folders = [[],[],[],[],[],[],[]]

	i = 0 
	while i!=len(folders):
		if i < 3:
			prefix = files_wanted_prefixes[i]
			for suffix in files_wanted_suffixes:
				filename = prefix + suffix + "1" + ".fil"
				files_wanted_folders[i].append(filename)
		else:
			suffix = files_wanted_prefixes[i]
			for j in range(1, 10):
				filename = "0" + str(j) + "/" + suffix
				files_wanted_folders[i].append(filename)
			for j in range(10, 14):
				filename = str(j) + "/" + suffix
				files_wanted_folders[i].append(filename)
		i+=1

	j = 0
	for folder in folders:
		print(folder)
		files = files_wanted_folders[j]
		wget_folder(folder, files, website)
		j+=1
