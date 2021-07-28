#!/usr/bin/env python

import numpy as np 
import time

# Define the training data as two classes

plus = [ [0,1.8] , [2,0.6] ]
minus =  [ [-1.2,1.4] , [0.4,-1] ]


def perceptron(plus,minus):

    w = [1.0 ,1.0 ] #Intialize weight vector
    itr = 0 # Initialize weight change iterations as zero

    # Initialize list of dot products
    p_value = [None] * len(plus)
    n_value = [None] * len(minus)

    while True:
        for i in range(len(plus)):
            p_value[i] = np.dot(w , plus[i])
            if p_value[i] <= 0:
                w = [a+b for a,b in zip(w,plus[i])]
                itr = itr + 1 
                #print('Weight vector is changed to : {} '. format(w))
                
            
        for i in range(len(minus)):
            n_value[i] = np.dot(w , minus[i])
            if n_value[i] > 0:
                w = [a-b for a,b in zip(w,minus[i])]
                itr = itr + 1
                #print('Weight vector is changed to : {} '. format(w))
                
        p_compare = np.array(p_value) > 0
        n_compare = np.array(n_value) <= 0

        # If all data points are correctly classified, then stop and give weight vector
        if p_compare.all() == True and n_compare.all() == True:
            print('Final Weight vector: {}'.format(w))
            print('Total iterations: {}'.format(itr))
            quit()
        
        
# Run function
perceptron(plus,minus)