import numpy as np
import numpy.random as nprand

def rand_spin_lattice(L):
	# Returns an L x L array of randomly generated values from the 
	# pair of numbers +1 and -1.

	return nprand.choice((1.0, -1.0), (L, L))

def energy(spin_lattice):
	# Computes the total energy of a two-dimensional L x L set of spins 
	# by summing scaled products of neighbouring spins. Periodic 
	# boundary conditions are assumed, and so when looping through 
	# each spin node in a left-to-right and downwards order, by 
	# computing the interaction energy of a given spin with the spins 
	# above and behind it, negative indexing can be employed to shorten 
	# the expression. The total number of vertices is then easily seen 
	# to be L x L.

	E = 0.0
	L = len(spin_lattice)

	for i in range(L):
		for j in range(L):
			E = E - spin_lattice[i, j]*spin_lattice[i - 1, j]
			E = E - spin_lattice[i, j]*spin_lattice[i, j - 1]
	return E

def flip_energy_shift(lattice, i, j):
	# Sums the values of adjacent spins of the given spin node 
	# (i, j), with care to periodic boundary conditions, and 
	# returns the corresponding energy shift when the spin (i, j) 
	# is flipped.

	L = len(lattice)
	sum_adj = lattice[i - 1, j] + lattice[i, j - 1]
	sum_adj = sum_adj + lattice[(i + 1) % L, j]
	sum_adj = sum_adj + lattice[i, (j + 1) % L]
	return 2.0*lattice[i, j]*sum_adj