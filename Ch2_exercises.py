from __future__ import division
import math
import numpy
import matplotlib.pyplot as plt
import subsignal_generator as haar

#2.1.A: Calculating the first level Haar transform of signal
f_21A = [2,2,2,4,4,4]
a_21A, d_21A = haar.generate_fluctuation_trend_subsignals(f_21A, 1)

#Example2.1.D: Computing first trend subsignal and first fluctuations for the following signals
f_21D_a = [2,4,6,6,4,2]
f_21D_b = [-1,1,2,-2,4,-4,2,2]
f_21D_c = [1,2,3,3,2,2,1,1]
f_21D_d = [2,2,4,4,6,6,8,8]



