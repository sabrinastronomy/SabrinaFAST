#!/usr/bin/python

import os
import subprocess

# Change when you have information about where filterbank/candidate files will be stored for each beam
data_directory_default = '/home/sabrinaberger/FAST/test_candidates/'
plot_directory_default = '/home/sabrinaberger/FAST/CandidatePlots/'


class plot:
  def __init__(self, all_cands_file="*_all.cand", nbeams=19, snr_cut=6, beam_mask=65536, nbeams_cut=4, filter_cut=16,
               multibeam=False, data_directory=data_directory_default, plot_directory=plot_directory_default):

    """
      Parameters taken by trans_gen_overview.py (if included *):
      *-cands_file CANDS_FILE
      *-nbeams NBEAMS
      *-snr_cut SNR_CUT
      *-beam_mask BEAM_MASK
      *-nbeams_cut NBEAMS_CUT
      -members_cut MEMBERS_CUT
      -dm_cut DM_CUT
      *-filter_cut FILTER_CUT
      -filter_max FILTER_MAX
      -min_bins MIN_BINS
      -resolution RESOLUTION
      -std_out
      -skip_rows SKIP_ROWS
      -just_time_dm
      -cand_list_xml
      -max_cands MAX_CANDS
      -no_plot
      -interactive
      -verbose
    """
    print("Initializing plotting instance...")
    self.all_cands_file = all_cands_file
    self.nbeams = nbeams
    self.snr_cut = snr_cut
    self.beam_mask = beam_mask
    self.nbeams_cut = nbeams_cut
    self.filter_cut = filter_cut
    self.multibeam = multibeam
    self.data_directory = data_directory
    self.plot_directory = plot_directory

  def make_overview_plot(self):
    # Directory already exists
    if (os.path.isdir(self.plot_directory)):
      subprocess.call('cd ' + self.plot_directory, shell=True)

    else:
        # Make directory to save plots to
      subprocess.call('mkdir CandidatePlots', shell=True)
      subprocess.call('cd CandidatePlots', shell=True)

    # TO DO make this better string
    # Make overview plot - input: *all.cand file
    nplot_call = 'python /home/sabrinaberger/FAST/plotting_scripts/trans_gen_overview.py -cands_file ' + self.all_cands_file + ' -nbeam ' +  str(self.nbeams) + ' -snr_cut ' + str(self.snr_cut) + ' -beam_mask ' + str(self.beam_mask) + ' -nbeams_cut ' + str(self.nbeams_cut) + ' -filter_cut ' + str(self.filter_cut)
    subprocess.call(nplot_call, shell=True)


if __name__ == "__main__":
  testing_plot = plot()
  testing_plot.make_overview_plot()



# Make filterbank plot - input: .fil tile
# subprocess.call('python trans_cand_server.py ' + data_directory + '', shell=True)
