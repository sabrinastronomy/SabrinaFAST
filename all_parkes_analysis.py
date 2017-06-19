from multibeam_heimdall import run_heimdall_on_directory
import subprocess

if __name__ == "__main__":
   parkes_FRBs = ["FRB010125", "FRB010724", "FRB110626", "FRB120127", "FRB010621", "FRB110220", "FRB110703"]
   for FRB in parkes_FRBs:
      subprocess.call("python multibeam_heimdall.py -d " + "/mnt_bls0/datax/users/Sabrina/" + FRB + "/ " + "-name " + FRB + " -dm_min 0 -dm_max 1000 -parallel 0", shell=True)
      subprocess.call("rm -r *_candidates", shell=True)
      subprocess.call("python multibeam_heimdall.py -d " + "/mnt_bls0/datax/users/Sabrina/" + FRB + "/ " + "-name " + FRB + " -dm_min 0 -dm_max 1000 -parallel 1", shell=True)

