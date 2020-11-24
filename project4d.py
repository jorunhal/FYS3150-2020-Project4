import numpy as np
import metropolis as met
import matplotlib.pyplot as plt
import statmech as sm

L = 20
T_arr = np.array([1.0, 2.4])
n_arr = np.linspace(4.0, 7.0, 16)
k = len(n_arr)

E_avg_arr = np.zeros(len(n_arr))
M_abs_avg_arr = np.zeros(len(n_arr))
num_acc_arr = np.zeros(len(n_arr))

# Ordered spin lattice

# Loop through temperatures
for T in T_arr:
	# Loop through number of cycles
	for i in range(k):
		n = int(n_arr[i])

		lattice = np.zeros((L, L)) + 1.0
		E, M, cycles, accepted = met.Metropolis_Ising2D_init(lattice, 1.0, max=10**n)
		E_avg_arr[i] = np.average(E)
		M_abs_avg_arr[i] = np.average(abs(M))
		num_acc_arr[i] = np.log(accepted)/np.log(10.0)

	plt.plot(n_arr, E_avg_arr)
	plt.title("Average energy vs. time, $T = " + str(T) + "$, ordered spins")
	plt.xlabel("# of cycles, powers of $10$")
	plt.ylabel("$\\langle E \\rangle$")
	plt.show()

	plt.plot(n_arr, M_abs_avg_arr)
	plt.title("Average magnetization vs. time, $T = " + str(T) + "$, ordered spins")
	plt.xlabel("# of cycles, powers of $10$")
	plt.ylabel("$|M|$")
	plt.show()

	plt.plot(n_arr, num_acc_arr)
	plt.title("Accepted configurations vs. time, $T = " + str(T) + "$, ordered spins")
	plt.xlabel("# of cycles, powers of $10$")
	plt.ylabel("# of accepted configurations, powers of $10$")
	plt.show()

# Randomly arranged spin lattice

# Loop through temperatures
for T in T_arr:
	# Loop through number of cycles
	for i in range(k):
		n = int(n_arr[i])

		lattice = sm.rand_spin_lattice(L)
		E, M, cycles, accepted = met.Metropolis_Ising2D_init(lattice, 1.0, max=10**n)
		E_avg_arr[i] = np.average(E)
		M_abs_avg_arr[i] = np.average(abs(M))
		num_acc_arr[i] = np.log(accepted)/np.log(10.0)

	plt.plot(n_arr, E_avg_arr)
	plt.title("Average energy vs. time, $T = " + str(T) + "$, disordered spins")
	plt.xlabel("# of cycles, powers of $10$")
	plt.ylabel("$\\langle E \\rangle$")
	plt.show()

	plt.plot(n_arr, M_abs_avg_arr)
	plt.title("Average magnetization vs. time, $T = " + str(T) + "$, disordered spins")
	plt.xlabel("# of cycles, powers of $10$")
	plt.ylabel("$|M|$")
	plt.show()

	plt.plot(n_arr, num_acc_arr)
	plt.title("Accepted configurations vs. time, $T = " + str(T) + "$, ordered spins")
	plt.xlabel("# of cycles, powers of $10$")
	plt.ylabel("# of accepted configurations, powers of $10$")
	plt.show()