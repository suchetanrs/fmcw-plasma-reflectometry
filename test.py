import numpy as np
import os

home=os.getenv('HOME')
wall_data_path=os.path.join(home,'SOP_3_2/Wall_data_files/shtt601')
print(wall_data_path)

curr_file=os.path.join(wall_data_path,'tIQ_t601_1.dat')
print(curr_file)

# ch1_data=np.fromfile(ch1 = np.fromfile(file=curr_file, dtype=np.double, sep=""))
t, I, Q = np.loadtxt(curr_file)
print(len(I))
# print(ch1_data)
# print(signal)