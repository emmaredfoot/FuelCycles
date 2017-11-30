import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import sys
import csv
import pylab

#Given and precalculated values
P_f = 0.9889
p=.7725
cross_25 =55.6E-24
cross_28 = 2.23E-24
cross_49 = 1618.23E-24
cross_40 = 2616.8E-24
epsilon = 1.0476
cross_41 = 1567.3E-24
cross_42 = 381E-24
eta_25 = 1.96
eta_28 = 2.3432
eta_49 = 1.86
eta_41 = 3.06

#Useful in this graph:
C_1 = 5.9727E23
C_2 = 2.5126E23
flux = 3.5E13
gamma = .5606


N=C_1*(1-np.exp(-a/cross_49*gamma*flux*t))+C_2*(np.exp(-cross_25*flux*t))-np.exp(-a/cross_49*gamma*flux*t)
