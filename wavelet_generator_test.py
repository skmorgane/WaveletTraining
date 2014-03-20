from __future__ import division
import math
import numpy as np

def generate_signal_detail_subsignals(signal, level):
    level_subsignals = []
    level_details = []
    all_scalings = []
    all_wavelets = []    
    length = len(signal)
    level_counter = 1  
    signal = f  
    while level_counter <= level:
        a_k = []
        d_k = []    
        k_level_scaling = generate_mlevel_vectors(length, level_counter, 'a')
        k_level_wavelet = generate_mlevel_vectors(length, level_counter, 'd')
        all_scalings.append(k_level_scaling)
        all_wavelets.append(k_level_wavelet)
        length_level_wavelet = len(all_scalings[level_counter-1])
        for m in range(0, length_level_wavelet):
            V_k_m = all_scalings[level_counter-1][m]
            W_k_m = all_wavelets[level_counter-1][m]
            a = np.dot(f,V_k_m)
            d = np.dot(f,W_k_m)
            a_k.append(a)
            d_k.append(d)
        level_details.append(d_k) 
        level_subsignals.append(a_k)
        level_counter +=1        
    return level_subsignals, level_details

def generate_mlevel_vectors(length, kth_level, flavor):
    """Generates the m-level Haar wavelet/scaling vectors for a particular
    level of wavelet analysis. Takes info on length of the original signal
    the level of analysis to be conducted and whether the vector to be generated
    is the scaling signal (a) or the wavelets(d)"""
    m = int(length/2)
    m_vectors = []
    value = (1/math.sqrt(2)) ** kth_level  
    value_list = [value] * 2 **kth_level
    for i in range(0,int(m/kth_level)):
        m_vector = [0] * length
        if flavor == 'a':
            m_vector[2*kth_level*i:kth_level*2*i+len(value_list)] = value_list
        elif flavor == 'd':
            start_substitution = int(0.5*len(value_list))
            for index in range(start_substitution,len(value_list)):             
                value_list[index] = -value              
            m_vector[2*kth_level*i:kth_level*2*i+len(value_list)] = value_list                 
        m_vectors.append(m_vector)
    return m_vectors

"""main code"""    
f = [4,6,10,12,8,6,5,5]
levels = 3
subsignals, detail_signals = generate_signal_detail_subsignals(f,levels)


        