from multibeam_heimdall import run_heimdall_on_directory
import subprocess

if __name__ == "__main__":
    parkes_FRBs = ["FRB010125", "FRB010724", "FRB110626", "FRB120127", "FRB010621", "FRB110220", "FRB110703"]
    one = ["FRB010125"]
    for FRB in one:
        subprocess.call("python multibeam.py -FRB_file " + FRB +  " -d /mnt_bls0/datax/users/Sabrina/" + FRB + "/ " + " -parallel 1 -dm_min 0 -dm_max 1000", shell=True)

