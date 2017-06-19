import multiprocessing
import os
import argparse
import subprocess
import numpy as np

def candplots(path_directory, filter_cut, snr_cut=10, max_cands_per_sec=1, nbeams_cut=1):
    # missing beam mask, potentially add later
    os.chdir(path_directory)
    subprocess.call(
        "/home/sabrinaberger/FAST/frb_detector.py -cands_file *_all.cand -snr_cut %f -filter_cut %d -nbeams_cut %d -max_cands_per_sec %f -verbose" % (
        snr_cut, filter_cut, nbeams_cut, max_cands_per_sec), shell = True)
    subprocess.call(
        "/home/sabrinaberger/FAST/frb_detector.py -cands_file *_all.cand -snr_cut %f -filter_cut %d -nbeams_cut %d -max_cands_per_sec %f > FRBcand" % (snr_cut, filter_cut, nbeams_cut, max_cands_per_sec), shell = True)
    if (os.stat("FRBcand").st_size is not 0):
        frb_cands = np.loadtxt("FRBcand", dtype={'names': ('snr', 'time', 'samp_idx', 'dm', 'filter', 'prim_beam'),
                                                'formats': ('f4', 'f4', 'i4', 'f4', 'i4', 'i4')})
        print("'snr', 'time', 'samp_idx', 'dm', 'filter', 'prim_beam'")
	print(frb_cands)
    else:
        print
    "No candidate found"
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='FRB_candidate parameters')
    
    parser.add_argument('-path_directory', type=str, help='Specify all_cands file location')
    parser.add_argument('-filter_cut', type=int,
                        help='Post Heimdall: Window size or filter cut for candidate selection (Default: 16.0)')
    parser.add_argument('-snr_cut', type=float, help='Post Heimdall: SNR cut for candidate selection (Default: 10.0)')
    parser.add_argument('-max_cands_per_sec', type=float,
                        help='Post Heimdall: Maximum allowed candidate per sec (Default: 1.0)')

    args = parser.parse_args()

    path_directory = args.path_directory
    filter_cut = args.filter_cut
    snr_cut = args.snr_cut
    max_cands_per_sec = args.max_cands_per_sec

    candplots(path_directory, filter_cut, snr_cut, max_cands_per_sec)
