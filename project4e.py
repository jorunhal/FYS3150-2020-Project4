import numpy as np
import statmech as sm
import metropolis as met
import matplotlib.pyplot as plt

L = 20
n = 6

T_arr = np.array([1.0, 2.4])

for T in T_arr:
	E, M, cycles, accepted = met.Metropolis_Ising2D(L, T, max=10**n)
	sigma_E = int(np.sqrt(np.var(E)))

	values, freq = np.unique(E, return_counts=True)
	plt.plot(values, freq/10**n)
	plt.title("Probability distribution $P(E)$, $\sigma_E = " + str(sigma_E) + "$, $T = " + str(T) + "$")
	plt.xlabel("E")
	plt.ylabel("P(E)")
	if T == 1.0:
		plt.axis((-800.0, -700, 0.0, 0.8))
	plt.show()