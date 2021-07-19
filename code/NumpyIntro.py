import numpy as np

# liste in array wandeln mit numpy
noten_list = [100, 89, 44, 78, 45, 24, 18]
noten_np_array = np.array(noten_list, dtype=np.int8)

# max und min
noten_max = np.max(noten_np_array)
noten_min = np.min(noten_np_array)

# argmax git den index zurück
#  0    1   2   3   4   5   6
# [100, 89, 44, 78, 45, 24, 18]
noten_arg_max = np.argmax(noten_np_array)
noten_arg_min = np.argmin(noten_np_array)

#
noten_mean = np.mean(noten_np_array)
noten_median = np.median(noten_np_array)
