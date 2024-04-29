# adaptive_basis
Training data and scripts for adaptive Pople basis sets

Optimal scaling factors obtained via L-BFGS minimization (2500 molecules from QM9) of Hartree-Fock total energies for the STO-3G, 3-21G, 6-31G, 6-31G* basis sets are available in the `training_data_all.npz` file.
Atomic numbers and positions for each molecule are present in the `charges` and `coordinates` arrays respectively in the same order. Scaling factors for each molecule are reported as N,(n+1) matrices for each molecule where N is the number of atoms and n is the number of scaling factors per atom (1 for STO-3G, 2 for 3-21G & 6-31G and 3 for 6-31G*). Each row of the matrix contains the atomic number, inner valence, outer valence and polarization function scaling factors respectively.  

# Requirements
* Numpy
* ASE
* Scipy
* MBDF requirements : https://github.com/dkhan42/MBDF

Usage example : 
```
from make_preds import get_preds
preds_aspirin = get_preds('aspirin.xyz', basis = '3-21g')
print(preds_aspirin)

array([[6.        , 1.19370967, 1.44321491],
       [6.        , 1.05819632, 1.30450641],
       [8.        , 1.06031794, 1.06446145],
       [8.        , 1.10903102, 1.16866435],
       [6.        , 1.03541024, 1.1555785 ],
       [6.        , 1.09164018, 1.18772218],
       [6.        , 1.09838297, 1.22369577],
       [6.        , 1.09610592, 1.21186561],
       [6.        , 1.09866442, 1.2034165 ],
       [6.        , 1.06754291, 1.26645958],
       [6.        , 1.04482928, 1.23553173],
       [8.        , 1.07051877, 1.09283811],
       [8.        , 1.09209269, 1.10151506],
       [1.        , 1.04921652, 0.94288023],
       [1.        , 1.04872793, 0.93999871],
       [1.        , 1.01692561, 0.8732459 ],
       [1.        , 0.95398191, 0.79891441],
       [1.        , 1.01521225, 0.93555485],
       [1.        , 1.00953882, 0.91281355],
       [1.        , 0.9961436 , 0.87176338],
       [1.        , 1.08273148, 0.96821555]])
```

# References
Please consider citing the following work :

Khan, D., Ach, M. L., & von Lilienfeld, O. A. (2024). Adaptive atomic basis sets. arXiv preprint [arXiv:2402.14793](https://arxiv.org/abs/2404.16942).
