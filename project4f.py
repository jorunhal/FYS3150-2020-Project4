import numpy as np
import statmech as sm
import metropolis as met
import matplotlib.pyplot as plt

# Define arrays of temperature points and lattice sizes
T1 = 2.0
T2 = 2.3
dT = 0.05
t = int((T2 - T1)/dT)
T_arr = np.linspace(T1, T2, t + 1)

L_arr = np.array([40, 60, 80, 100], dtype=int)
l = len(L_arr)

# Define arrays to store computed values
E_avg_arrs = np.zeros((l, t + 1))
M_abs_avg_arrs = np.zeros((l, t + 1))
Cv_arrs = np.zeros((l, t + 1))
X_arrs = np.zeros((l, t + 1))

# Loop through lattice sizes
for i in range(l):
	L = L_arr[i]

	# Loop through temperatures
	for j in range(t):
		T = T_arr[j]
		E, M, cycles, accepted = met.Metropolis_Ising2D(L, T, max=10**6)

		# Compute quantities
		E_avg_arrs[i, j] = np.average(E)
		M_abs_avg_arrs[i, j] = np.average(abs(M))
		Cv_arrs[i, j] = np.var(E)/T**2.0
		X_arrs[i, j] = np.var(abs(M))/T

# Plot the mean energies

for E_arr in E_avg_arrs:
	plt.plot(T_arr, E_arr)
plt.title("Mean energies vs. temperature")
plt.xlabel("$T$")
plt.ylabel("$\\langle E \\rangle$")
plt.show()

# Plot the mean magnetizations

for M_arr in M_abs_avg_arrs:
	plt.plot(T_arr, M_arr)
plt.title("Mean magnetizations vs. temperature")
plt.xlabel("$T$")
plt.ylabel("$|M|$")
plt.show()

# Plot the specific heats

for Cv_arr in Cv_arrs:
	plt.plot(T_arr, Cv_arr)
plt.title("Heat capacities vs. temperature")
plt.xlabel("$T$")
plt.ylabel("$C_V$")
plt.show()

# Plot the susceptibilities

for X_arr in X_arrs:
	plt.plot(T_arr, X_arr)
plt.title("Susceptiblities vs. temperature")
plt.xlabel("$T$")
plt.ylabel("$\chi$")
plt.show()