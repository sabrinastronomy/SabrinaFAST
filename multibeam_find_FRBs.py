import multiprocessing
import os
import argparse
import subprocess

def canplots(filter_cut, snr_cut = 10, max_cands_per_sec = 1, nbeams_cut = 1):
	# missing beam mask, potentially add later
	subprocess.call("rm *_all.cand")
	subprocess.call("rm *.ar")
	subprocess.call("coincidencer *.cand")	
	subprocess.call("trans_gen_overview.py -cands_file *_all.cand")
	# subprocess.call("mv overview_1024x768.tmp.png %s.overview.png" % (source_name))
	subprocess.call("frb_detector.py -cands_file *_all.cand -snr_cut %f -filter_cut %d -nbeams_cut %d -max_cands_per_sec %f -verbose" % (snr_cut, filter_cut, nbeams_cut, max_cands_per_sec,minMem))
	subprocess.call("frb_detector.py -cands_file *_all.cand -snr_cut %f -filter_cut %d -nbeams_cut %d -max_cands_per_sec %f > FRBcand" % (snr_cut, max_cands_per_sec,minMem))
	

	if(os.stat("FRBcand").st_size is not 0):
		frb_cands = np.loadtxt("FRBcand",dtype={'names': ('snr','time','samp_idx','dm','filter','prim_beam'),'formats': ('f4', 'f4', 'i4','f4','i4','i4')})
	else:
		print "No candidate found"
		return

if name == "__main__":

	parser = argparse.ArgumentParser(description='FRB_candidate parameters')
	parser.add_argument('-filter_cut', type=int, help='Post Heimdall: Window size or filter cut for candidate selection (Default: 16.0)')
	parser.add_argument('-snr_cut', type=float, help='Post Heimdall: SNR cut for candidate selection (Default: 10.0)')
	parser.add_argument('-max_cands_per_sec', type=float, help='Post Heimdall: Maximum allowed candidate per sec (Default: 1.0)')

	args = parser.parse_args()

	filter_cut = args.filter_cut
	snr_cut = args.snr_cut
	max_cands_per_sec = args.max_cands_per_sec

	candplots(filter_cut, snr_cut, max_cands_per_sec)


	#plotting stuff
	# extime = 1.0
	
	# if(noplot is not True):
	# 	if(frb_cands.size > 1):
	# 		frb_cands = np.sort(frb_cands)	
	# 		frb_cands[:] = frb_cands[::-1]	
	# 		for indx,frb in enumerate(frb_cands):
	# 			time = frb['time']
	# 			dm = frb['dm']
	# 			stime = time-(extime/2)
	# 			if(stime<0): stime = 0
	# 			#if(any(l<=stime<=u for (l,u) in kill_time_ranges)):
	# 			if(any(l<=time<=u for (l,u) in kill_time_range)):
	# 				print "Candidate inside bad-time range"
	# 			else:
	# 				os.system("dspsrfil -S %f -c %f -T %f -t 12 -D %f  -O %04d_%fsec_DM%f -e ar %s" % (stime,extime,extime,dm,indx,time,dm,fil_file))
	# 	elif(frb_cands.size):
	# 		time = float(frb_cands['time'])
	# 		dm = float(frb_cands['dm'])
	# 		stime = time-(extime/2)
 #                        if(stime<0): stime = 0
	# 		if(any(l<=time<=u for (l,u) in kill_time_range)):
	# 			print "Candidate inside bad-time range"
	# 		else:
	# 			os.system("dspsrfil -cepoch=start -S %f -c %f -T %f -t 12 -D %f  -O 0000_%fsec_DM%f -e ar %s" % (stime,extime,extime,dm,time,dm,fil_file))		
	# 	else:
	# 		print "No candidate found"
	# 		return

	# 	os.system("psrplot -p F -j 'D, F 32, B 128' -D %s_frb_cand.ps/cps *.ar" % (source_name))
		

