#%%
import random
import numpy as np

#%% 
# funcion para simular medicion de temp con desviacion estandar

def medir_temp(n):
    mediciones = np.empty(n)
    for i in range(n):
        mediciones[i] = random.normalvariate(37.5,0.2)
    np.save('../Data/temperaturas', mediciones)
    return mediciones
# %%

medir_temp(999)
# %%
