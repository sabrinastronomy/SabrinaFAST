def canplo:wq!:ts(fil_file,source_name,snr_cut,filter_cut,maxCandSec,noplot,minMem,kill_chans,kill_time_range):
	#os.chdir(basedir)
	#os.system("cd %s" % (basedir))
	#print "Inside : %s" % (basedir) 
	os.system("rm *_all.cand")
	os.system("rm *.ar")
	os.system("coincidencer *.cand")	
	os.system("trans_gen_overview.py -cands_file *_all.cand")
	os.system("mv overview_1024x768.tmp.png %s.overview.png" % (source_name))
	os.system("frb_detector_bl.py -cands_file *_all.cand -filter_cut %d -snr_cut %f -max_cands_per_sec %f -min_members_cut %f -verbose" % (filter_cut,snr_cut,maxCandSec,minMem))
	os.system("frb_detector_bl.py -cands_file *_all.cand -filter_cut %d -snr_cut %f -max_cands_per_sec %f -min_members_cut %f  > FRBcand" % (filter_cut,snr_cut,maxCandSec,minMem))
	if(os.stat("FRBcand").st_size is not 0):
		frb_cands = np.loadtxt("FRBcand",dtype={'names': ('snr','time','samp_idx','dm','filter','prim_beam'),'formats': ('f4', 'f4', 'i4','f4','i4','i4')})
	else:
		print "No candidate found"
		return
	#print frb_cands['time'],frb_cands['dm']

	#Extract block to plot in seconds
	extime = 1.0
	
	if(noplot is not True):
		if(frb_cands.size > 1):
			frb_cands = np.sort(frb_cands)	
			frb_cands[:] = frb_cands[::-1]	
			for indx,frb in enumerate(frb_cands):
				time = frb['time']
				dm = frb['dm']
				stime = time-(extime/2)
				if(stime<0): stime = 0
				#if(any(l<=stime<=u for (l,u) in kill_time_ranges)):
				if(any(l<=time<=u for (l,u) in kill_time_range)):
					print "Candidate inside bad-time range"
				else:
					os.system("dspsrfil -S %f -c %f -T %f -t 12 -D %f  -O %04d_%fsec_DM%f -e ar %s" % (stime,extime,extime,dm,indx,time,dm,fil_file))
		elif(frb_cands.size):
			time = float(frb_cands['time'])
			dm = float(frb_cands['dm'])
			stime = time-(extime/2)
                        if(stime<0): stime = 0
			if(any(l<=time<=u for (l,u) in kill_time_range)):
				print "Candidate inside bad-time range"
			else:
				os.system("dspsrfil -cepoch=start -S %f -c %f -T %f -t 12 -D %f  -O 0000_%fsec_DM%f -e ar %s" % (stime,extime,extime,dm,time,dm,fil_file))		
		else:
			print "No candidate found"
			return
		# If no kill_chans, do an automatic smoothing
		temp = ""
		#os.system("paz -r -b -L -m *.ar")
		if kill_chans: 	
			for k in kill_chans: temp = temp +" "+str(k)
			temp = "paz -z \"" + temp	+ "\" -m *.ar"
			print temp
			os.system(temp)	
		#os.system()
		#os.system("paz -r -b -L -m *.ar")
		#os.system("paz -Z '1775 1942' -m *.ar")
		os.system("psrplot -p F -j 'D, F 32, B 128' -D %s_frb_cand.ps/cps *.ar" % (source_name))
		

