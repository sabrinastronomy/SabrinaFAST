import multiprocessing
import os
import subprocess
import numpy as np
import argparse


class multibeamFRBFinder:
    def __init__(self, FRB_cand_filename, origin, parallel, dm_min, dm_max, dm_tol, rfi_tol,
                 boxcar_max, snr_cut, filter_cut, max_cands_per_sec, nbeams_cut):
        self.FRB_cand_filename = FRB_cand_filename
        self.origin = origin
        self.destination = os.getcwd() + "/" + FRB_cand_filename + "_candidates"
        self.parallel = parallel  # 0 for false and 1 for true
        self.dm_min = dm_min
        self.dm_max = dm_max
        self.dm_tol = dm_tol
        self.rfi_tol = rfi_tol
        self.boxcar_max = boxcar_max

        self.snr_cut = snr_cut
        self.filter_cut = filter_cut
        self.max_cands_per_sec = max_cands_per_sec
        self.nbeams_cut = nbeams_cut

    @staticmethod
    def run_heimdall(input_file, output_directory, dm_min, dm_max, dm_tol, rfi_tol, boxcar_max):
        subprocess.call("heimdall -f %s -output_dir %s -dm %d %d -dm_tol %f -rfi_tol %f -boxcar_max %d" % (input_file, output_directory, dm_min, dm_max, dm_tol, rfi_tol, boxcar_max), shell=True)

    @staticmethod
    def coincidencer():
        subprocess.call("coincidencer *.cand", shell=True)

    def run_heimdall_on_directory(self):
        beams = os.listdir(self.origin)
        subprocess.call("mkdir " + self.destination, shell=True)
        i = 0
        if self.parallel:
            procs = []
            for beam in beams:
                proc = multiprocessing.Process(target=self.run_heimdall, args=(
                    self.origin + beam, self.destination, self.dm_min, self.dm_max, self.dm_tol, self.rfi_tol,
                    self.boxcar_max))
                procs.append(proc)
                proc.start()
                print("Beam " + str(i) + " initiated.")
                i += 1
            for proc in procs:
                proc.join()
        else:
            for beam in beams:
                self.run_heimdall(self.origin + beam, self.destination, self.dm_min, self.dm_max, self.dm_tol,
                                  self.rfi_tol, self.boxcar_max)
                print("Beam " + str(i) + " initiated.")
                i += 1

    def FRB_detector(self):
        # TODO missing beam mask, potentially add later
        current_directory = os.getcwd()
        os.chdir(self.destination)
        self.coincidencer()
        subprocess.call("/home/sabrinaberger/FAST/frb_detector.py -cands_file *_all.cand -snr_cut %f -filter_cut %d -nbeams_cut %d -max_cands_per_sec %f -verbose" % (self.snr_cut, self.filter_cut, self.nbeams_cut, self.max_cands_per_sec), shell=True)
        subprocess.call("/home/sabrinaberger/FAST/frb_detector.py -cands_file *_all.cand -snr_cut %f -filter_cut %d -nbeams_cut %d -max_cands_per_sec %f > %s" % (self.snr_cut, self.filter_cut, self.nbeams_cut, self.max_cands_per_sec, self.FRB_cand_filename), shell=True)
        os.chdir(current_directory)

    def multibeam(self):
        self.run_heimdall_on_directory()
        self.coincidencer()
        self.FRB_detector()



class FRBs(multibeamFRBFinder):
    def __init__(self, FRB_cand_filename, origin, parallel, dm_min, dm_max, dm_tol=1.01, rfi_tol=3,
                 boxcar_max=16, snr_cut=6, filter_cut=16, max_cands_per_sec=5, nbeams_cut=4):
        multibeamFRBFinder.__init__(self, FRB_cand_filename, origin, parallel, dm_min, dm_max, dm_tol, rfi_tol,
                                   boxcar_max, snr_cut, filter_cut, max_cands_per_sec, nbeams_cut)
        self.multibeam()
        if os.stat(self.destination + "/" + self.FRB_cand_filename).st_size is not 0:  # st_size: size of file, in bytes
            self.frb_cands = np.loadtxt(self.destination + "/" + self.FRB_cand_filename,
                                        dtype={'names': ('snr', 'time', 'samp_idx', 'dm', 'filter', 'prim_beam'),
                                               'formats': ('f4', 'f4', 'i4', 'f4', 'i4', 'i4')})
        else:
            self.frb_cands = []
            print("No FRB candidates found.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get directory information and FRB candidate search parameters')

    parser.add_argument('-FRB_file', type=str, help='Specify where FRB candidate files will be located')
    parser.add_argument('-d', type=str, help='directory where beam files are located')
    parser.add_argument('-parallel', type=int, help='Heimdall: enable parallel processing')
    parser.add_argument('-dm_min', type=int, help='Heimdall: minimum DM')
    parser.add_argument('-dm_max', type=int, help='Heimdall: maximum DM')

    #TODO increase number of parameters specifiable
    # parser.add_argument('-snr_cut', type=float, help='Post Heimdall: SNR cut for candidate selection (Default: 10.0)', const=10.0)
    # parser.add_argument('-filter_cut', type=int, help='Post Heimdall: Window size or filter cut for candidate selection (Default: 16.0)', const=16.0)
    # parser.add_argument('-max_cands_per_sec', type=float, help='Post Heimdall: Maximum allowed candidate per sec (Default: 1.0)', const=1.0)

    args = parser.parse_args()

    destination = args.FRB_file
    origin = args.d
    parallel = args.parallel

    dm_min = args.dm_min
    dm_max = args.dm_max

    # snr_cut = args.snr_cut
    # filter_cut = args.filter_cut
    # max_cands_per_sec = args.max_cands_per_sec

    FRBs(destination, origin, parallel, dm_min, dm_max)

