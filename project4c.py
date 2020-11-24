# Script to employ the Metropolis algorithm to compute the mean energy, 
# the mean absolute magnetization, the specific heat and the magnetic 
# susceptivity of a 2 x 2 Ising model, at a temperature T = 1.0 in units 
# of KT/J. The function Metropolis_Ising2D() returns arrays with energies 
# and magnetizations, from which mean values and variances are computed.

import numpy as np
import metropolis as met

L = 2
T = 1.0

# Call function to run algorithm
E, M, cycles, accepted = met.Metropolis_Ising2D(L, T, max=10**7)

# Compute thermodynamic quantities
E_avg = np.average(E)
M_abs_avg = np.average(abs(M))
Cv = np.var(E)/T**2.0
X = np.var(abs(M))/T

# Output results
print("Dimensions: " + str(L) + " x " + str(L))
print("Mean energy: " + str(E_avg))
print("Mean absolute magnetization: " + str(M_abs_avg))
print("Specific heat: " + str(Cv))
print("Susceptibility: " + str(X))
print("Number of cycles: " + str(cycles))
print("Number of accepted states: " + str(accepted))


# Dimensions: 2 x 2
# Mean energy: -7.98420960157904
# Mean absolute magnetization: 3.994740000526
# Specific heat: 0.12609945068282824
# Susceptibility: 0.015743530828413642
# Number of cycles: 10000000
# Number of accepted states: 19759