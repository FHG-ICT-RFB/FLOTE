import numpy as np
from datafile_Q_FINAL import SVF
import datafile_Q_FINAL
import Arrays
import sensitivity_plot
import pandas as pd

def MVF(Var1,min1,max1,steps1,scale1,Var2,min2,max2,steps2,scale2):

    array1, n1 = Arrays.arraygen(min1,max1,steps1,scale1)
    array2, n2 = Arrays.arraygen(min2,max2,steps2,scale2)

    print(array1)
    print(array1)

    Output = np.zeros((n1+1,n2+1))
    
    for i in array1 :
        x = array1.index(i)
        for j in array2 :
            y = array2.index(j)

            Output[x][y] = SVF(Var1, Var2, i, j)

            if datafile_Q_FINAL.eG16 < 0 or datafile_Q_FINAL.pH10 < 0 :
                Output[x][y] = None

    Output2 = Output.tolist()
    sensitivity_plot.plot_sense(array1, array2, Output2, scale1, scale2, Var1, Var2, 'Cost_Battery')

    Df_matrix = Output
    df = pd.DataFrame(Df_matrix)
    df.columns = array2
    df.index = array1
    df.to_excel(excel_writer = "D:/ACADEMICS/MS THESIS/Publication/SCALED DOWN/SENSITIVITY - Scaled Down/SENSITIVITY - Raw Data/Q_Conc_CD.xlsx")

    return Output2

MVF(
    'Concentration_pos',
    0.01,
    4,
    80,
    'Exponential',
    'Current_Density',
    1,
    500,
    300,
    'Exponential'
)