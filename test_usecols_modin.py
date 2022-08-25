import modin.pandas as mpd
import pandas as pd

# extract first 40 rows from file 
rows_to_skip = list(range(1, int(40)))

modin_frame = mpd.read_csv("/home/developer/Escritorio/CICD_long_records/"
                           "test_nav_313_NAVRecorder_2022-03-10-13-44-24Makefile_ANAVInternalData_A.txt_NAVPlayer.txt", sep=';',
                           usecols=['SIGNAL_SENDA_NAV_GNSS_SOL_QUALITY_UL'], skiprows=rows_to_skip)

pandas_frame = pd.read_csv("/home/developer/Escritorio/CICD_long_records/"
                           "test_nav_313_NAVRecorder_2022-03-10-13-44-24Makefile_ANAVInternalData_A.txt_NAVPlayer.txt", sep=';',
                           usecols=['SIGNAL_SENDA_NAV_GNSS_SOL_QUALITY_UL'], skiprows=rows_to_skip)

print("finished")
