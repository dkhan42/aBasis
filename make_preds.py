import numpy as np
from ase.io import read
from cMBDF import generate_mbdf
from scipy.spatial.distance import euclidean

def get_preds(xyz,basis):
    atoms = read(xyz)
    q, r = atoms.get_atomic_numbers(), atoms.get_positions()
    reptest = np.concatenate(generate_mbdf(np.array([q]), np.array([r]), rcut=6.0, pad=None))
    data = np.load('trained_models.npz',allow_pickle=True)
    xtrain, Hinds, Cinds, Ninds, Oinds, Finds = data['xtrain'], data['Hinds'], data['Cinds'], data['Ninds'], data['Oinds'], data['Finds']

    if basis in ['sto-3g', 'STO-3G', 'sto3g']:
        model = data['models_sto3g']
        n = 1
    elif basis in ['3-21g', '3-21G', '321g']:
        model = data['models_321g']
        n = 2
    elif basis in ['6-31g', '6-31G', '631g']:
        model = data['models_631g']
        n = 2
    elif basis in ['6-31gs', '6-31g*', '6-31Gs', '631G*', '631-G*']:
        model = data['models_631gs']
        n = 3
    
    preds = np.zeros((len(q),n))
    preds[:,0] = q
    for i in range(1,n):
        if i<3:
            for j,inds,elem in zip(range(5),[Hinds, Cinds, Ninds, Oinds, Finds],[1,6,7,8,9]):
                xtest = reptest[eleminds]
                eleminds = np.array(q==elem)
                dist = euclidean(xtrain[inds], xtest)
                alpha, sigma = model[i][j][:-1], model[i][j][-1]
                k = dist/sigma
                preds[eleminds,i] = np.dot(k.T,alpha)
        else:
            for j,inds,elem in zip(range(5),[Hinds, Cinds, Ninds, Oinds, Finds],[1,6,7,8,9]):
                if j!=0:
                    xtest = reptest[eleminds]
                    eleminds = np.array(q==elem)
                    dist = euclidean(xtrain[inds], xtest)
                    alpha, sigma = model[i][j][:-1], model[i][j][-1]
                    k = dist/sigma
                    preds[eleminds,i] = np.dot(k.T,alpha)

    return preds