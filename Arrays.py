import numpy as np

def arraygen(min, max, steps, scale) :

    Pn_array = []

    if scale == 'Linear':

        for i in range(steps+1) :
            Pn_array.append(min + i*(max - min)/steps)

        return Pn_array,steps

    elif scale == 'Exponential':

        for i in range(steps+1):
            y = np.exp(np.log(min) + i*(np.log(max) - np.log(min))/steps)
            Pn_array.append(y)

        return Pn_array, steps