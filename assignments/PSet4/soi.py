##############################################################################c
# This is some beginning code for completing problem 3 from Problem Set #4
#  by: Kevin Goebbert
#
#
#
#
#
##############################################################################c
import numpy as np

#### BEGIN DO NOT CHANGE ANYTHING BETWEEN STATEMENTS ####
data = np.loadtxt('/archive/data_kevin/met330/soi.txt', skiprows=4)

years = data[:, 0]
soi_data = data[:,1:]

#### END OF DO NOT CHANGE ANYTHING BETWEEN STATEMENTS ####

print(soi_data)
