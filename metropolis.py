import numpy as np
import numpy.random as nprand
import statmech as sm

def Metropolis_Ising2D(L, T, max=10**5):
	# This function employs the Metropolis algorithm to compute 
	# a set of total energies and magnetizations of a square 
	# two-dimensional L x L Ising model of lattice spins.

	# Initialize spin lattice, and arrays to hold the total 
	# energies and magnetizations
	lattice = sm.rand_spin_lattice(L)
	E = np.zeros(max + 1)
	M = np.zeros(max + 1)
	E[0] = sm.energy(lattice)
	M[0] = np.sum(lattice)

	# Relative probabilities of states given by known possible energy 
	# differences
	w_arr = np.array([ np.exp((8.0 - 2.0*i)/T) for i in range(9) ])

	# Set counters and initiate algorithm
	accepted = 0
	cycles = 0
	for n in range(max):
		# Choose at random and flip a spin from the lattice, 
		# compute the change in energy and fetch the relative 
		# probability w
		i, j = nprand.choice(L, 2)
		dE = sm.flip_energy_shift(lattice, i, j)

		# Compute index of and fetch the relevant relative probability w, 
		# check whether transition will be accepted, by comparing 
		# w to a uniformly random number in the range [0.0, 1.0)
		w = w_arr[int((dE + 8.0)/2.0)]
		if w > nprand.sample():
			# Set the new microstate, adjust the energy and the
			# magnetization, and increase counter of accepted 
			# transitions
			lattice[i, j] = -lattice[i, j]
			E[n + 1] = E[n] + dE
			M[n + 1] = M[n] + 2.0*lattice[i, j]
			accepted = accepted + 1
		else:
			# Record the previous microstate again
			E[n + 1] = E[n]
			M[n + 1] = M[n]

		cycles = cycles + 1

	return E, M, cycles, accepted

def Metropolis_Ising2D_init(spin_lattice, T, max=10**5):
	# This function employs the Metropolis algorithm to compute 
	# a set of total energies and magnetizations of a square 
	# two-dimensional Ising model of lattice spins. The 
	# initial lattice is given as an argument.

	# Make a copy of the argument lattice, initialize dimension parameter 
	# L, and arrays to hold the total energies and magnetizations
	lattice = np.copy(spin_lattice)
	L = len(lattice)
	E = np.zeros(max + 1)
	M = np.zeros(max + 1)
	E[0] = sm.energy(lattice)
	M[0] = np.sum(lattice)

	# Relative probabilities of states given by known possible energy 
	# differences
	w_arr = np.array([ np.exp((8.0 - 2.0*i)/T) for i in range(9) ])

	# Set counters and initiate algorithm
	accepted = 0
	cycles = 0
	for n in range(max):
		# Choose at random and flip a spin from the lattice, 
		# compute the change in energy and fetch the relative 
		# probability w
		i, j = nprand.choice(L, 2)
		dE = sm.flip_energy_shift(lattice, i, j)

		# Compute index of and fetch the relevant relative probability w, 
		# check whether transition will be accepted, by comparing 
		# w to a uniformly random number in the range [0.0, 1.0)
		w = w_arr[int((dE + 8.0)/2.0)]
		if w > nprand.sample():
			# Set the new microstate, adjust the energy and the
			# magnetization, and increase counter of accepted 
			# transitions
			lattice[i, j] = -lattice[i, j]
			E[n + 1] = E[n] + dE
			M[n + 1] = M[n] + 2.0*lattice[i, j]
			accepted = accepted + 1
		else:
			# Record the previous microstate again
			E[n + 1] = E[n]
			M[n + 1] = M[n]

		cycles = cycles + 1

	return E, M, cycles, accepted