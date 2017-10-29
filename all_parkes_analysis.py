import subprocess

if __name__ == "__main__":
    #parkes_FRBs = ["FRB010125", "FRB010724", "FRB110626", "FRB120127", "FRB010621", "FRB110220", "FRB110703"]
    location = "/home/sabrinaberger/FRB_Parkes_data/"
    parkes_FRBs = ["FRB010125"]
    for FRB in parkes_FRBs:
        subprocess.call("python multibeam.py -FRB_file " + FRB +  " -d " + location + FRB + "/ " + " -parallel 1 -dm_min 0 -dm_max 9988", shell=True)

