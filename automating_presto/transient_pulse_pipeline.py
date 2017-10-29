import argparse
from subprocess import call
import time

parser = argparse.ArgumentParser(description='Input filterbank file to search for transient pulse.')
parser.add_argument('-file', type=str, help='Filterbank File')

parser.add_argument('-dmstep', type=float, help='DM Step Size')
parser.add_argument('-foldername', type=str, help='Relevant files to analysis held here')

args = parser.parse_args()
fil_file = args[0]
lodm = args[1]
dmstep = args[2]
foldername = args[3]

def go(fil_file, lodm, dmstep, foldername):
    call(["rfifind", "-time", "2.0", "-o", "Lband", fil_file])
    call(["prepsubband", "-nsub", "32", "-lodm", lodm, "-dmstep", dmstep, "-numdms", "24", "-numout", "132500", "-downsamp", "4", "-mask", "Lband_rfifind.mask", "-runavg", "-o", fil_file])
    call(["mkdir", foldername])
    initial_time = time.clock()
    call(["single_pulse_search.py", "-t", "2000", "*.dat"])
    call(["mv", "Lband*", "foldername"])
    final_time = time.clock() - initial_time
    print "Total Time for Transient Pulse Search: " + final_time
    call(["evince", foldername + "/Lband_singlepulse.ps"])

