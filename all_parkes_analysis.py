from multibeam_heimdall import run_heimdall_on_directory

if __name__ == "__main__":
   parkes_FRBs = ["FRB010125", "FRB010724", "FRB110626", "FRB120127", "FRB010621", "FRB110220", "FRB110703"]
   for FRB in parkes_FRBs:
      run_heimdall_on_directory("/mnt_bls0/datax/users/Sabrina/" + FRB + "/", FRB)

