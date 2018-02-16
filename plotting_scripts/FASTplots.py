#!/usr/bin/python

import subprocess
import os

data_directory = '/home/sabrinaberger/test_files/'

# Make directory to save plots to 
subprocess.call('mkdir CandidatePlots', shell=True)
subprocess.call('cd CandidatePlots', shell=True)

# Make overview plot - input: *all.cand file
subprocess.call('python trans_gen_overview.py ' + data_directory + '', shell=True)

# Make filterbank plot - input: .fil tile
subprocess.call('python trans_cand_server.py ' + data_directory + '', shell=True)


