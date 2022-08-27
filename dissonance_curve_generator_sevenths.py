import numpy as np
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools
from itertools import permutations
from sklearn import preprocessing

def dissmeasure(fvec, amp, model='min'):
    """
    Given a list of partials in fvec, with amplitudes in amp, this routine
    calculates the dissonance by summing the roughness of every sine pair
    based on a model of Plomp-Levelt's roughness curve.
    The older model (model='product') was based on the product of the two
    amplitudes, but the newer model (model='min') is based on the minimum
    of the two amplitudes, since this matches the beat frequency amplitude.
    """
    # Sort by frequency
    sort_idx = np.argsort(fvec)
    am_sorted = np.asarray(amp)[sort_idx]
    fr_sorted = np.asarray(fvec)[sort_idx]

    # Used to stretch dissonance curve for different freqs:
    Dstar = 0.24  # Point of maximum dissonance
    S1 = 0.0207
    S2 = 18.96

    C1 = 5
    C2 = -5

    # Plomp-Levelt roughness curve:
    A1 = -3.51
    A2 = -5.75

    # Generate all combinations of frequency components
    idx = np.transpose(np.triu_indices(len(fr_sorted), 1))
    fr_pairs = fr_sorted[idx]
    am_pairs = am_sorted[idx]

    Fmin = fr_pairs[:, 0]
    S = Dstar / (S1 * Fmin + S2)
    Fdif = fr_pairs[:, 1] - fr_pairs[:, 0]

    if model == 'min':
        a = np.amin(am_pairs, axis=1)
    elif model == 'product':
        a = np.prod(am_pairs, axis=1)  # Older model
    else:
        raise ValueError('model should be "min" or "product"')
    SFdif = S * Fdif
    D = np.sum(a * (C1 * np.exp(A1 * SFdif) + C2 * np.exp(A2 * SFdif)))

    return D
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def column(matrix, i):
    return [row[i] for row in matrix]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def chord_ratio(num_one, denom_one, num_two, denom_two):
    # Find the common denominator
    common_denom = denom_one * denom_two
    new_num_one = num_one * denom_two
    new_num_two = num_two * denom_one
    red_num = new_num_one / common_denom
    red_denom = new_num_two / common_denom
    return [red_num, red_denom] , red_num / red_denom
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
diss_vec = dissonance vector of values representing the dissonances across a spectrum
diss_vec_unit = sample size of the dissonance vector above
ratio = what is the ratio of the interval of concern as a decimal
'''
def diss_value(diss_vec, diss_vec_unit, interval_ratio):

    counter = 0
    for i in linspace(1, 2.3, 1000):
        for j in linspace(1, 2.3, 1000):
            if i == interval_ratio[0] and j == interval_ratio[1]:
                break
        counter = counter + 1
            
            
    SAMPLE_SIZE = diss_vec_unit
    trans_interv_ratio = (interval_ratio * SAMPLE_SIZE) #transformed interval for dissonance vector

    modulo_interval = trans_interv_ratio % 1
    # This will push either to the nearest integer for better
    if modulo_interval > 0.5:
        trans_interv_ratio = math.ceil(trans_interv_ratio)
    elif modulo_interval < 0.5:
        trans_interv_ratio = math.floor(trans_interv_ratio)

    dissonance_value = diss_vec[trans_interv_ratio]
    return dissonance_value
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    
    """
    Reproduce Sethares Figure 3
    http://sethares.engr.wisc.edu/consemi.html#anchor15619672
    """

    freq =  261.63 * array([1, 2, 3, 4, 5, 6])
    amp = 0.88**array([0, 1, 2, 3, 4, 5])
    r_low = 1
    alpharange = 4.0
    method = 'product'

    n = 100
    Ratios = linspace(r_low, alpharange, n)
    diss = empty(n**3)

    a = concatenate((amp, amp, amp, amp))
    index = 0
    counter = 0
    for alpha in Ratios:
        for beta in Ratios:
            for delta in Ratios:
                f = concatenate((freq, freq * alpha, freq * alpha * beta, freq * alpha * beta * delta))
                d = dissmeasure(f, a, method)
                diss[index] = d
                index += 1
                counter += 1
        if counter / 1000:
            print("Iteration: ", counter)

    diss = preprocessing.normalize([diss])
    print(diss)
            
    np.savetxt('dissonance_curve_sevenths_C.csv', diss, delimiter=',')

    master_list_xy = list(itertools.product(linspace(r_low, alpharange, n), repeat=3))
    
    x = column(master_list_xy, 0)
    y = column(master_list_xy, 1)
    z = column(master_list_xy, 2)

    
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    pnt3d = ax.scatter(x, y, z, c = diss)
    
    cbar = plt.colorbar(pnt3d)
    cbar.set_label("Sensory Dissonance Spectrum")
    # plt.show()
