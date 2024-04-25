# adaptive_basis
Training data and scripts for adaptive Pople basis sets

Optimal scaling factors obtained via L-BFGS minimization (2500 molecules from QM9) of Hartree-Fock total energies for the STO-3G, 3-21G, 6-31G, 6-31G* basis sets are available in the `training_data_all.npz` file.
Atomic numbers and positions for each molecule are present in the `charges` and `coordinates` arrays respectively in the same order. Scaling factors for each molecule are reported as N,(n+1) matrices for each molecule where N is the number of atoms and n is the number of scaling factors per atom (1 for STO-3G, 2 for 3-21G & 6-31G and 3 for 6-31G*). Each row of the matrix contains the atomic number, inner valence, outer valence and polarization function scaling factors respectively.  
