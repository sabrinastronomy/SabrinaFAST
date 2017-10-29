# FAST Multibeam FRB Search Pipeline

This is a pipeline developed for deployment at the FAST radio telescope in the Guizhou Province in China. It uses the GPU based Heimdall code to search for transient signals 

## How to run 

multibeam.py takes input from the command line.
Here are the parameters that must be specified for each group of beam files: 

* -FRB_file FRB_FILE  Specify where FRB candidate files will be located
*  -d D                directory where beam files are located
*  -parallel PARALLEL  Heimdall: enable parallel processing
*  -dm_min DM_MIN      Heimdall: minimum DM
*  -dm_max DM_MAX      Heimdall: maximum DM
