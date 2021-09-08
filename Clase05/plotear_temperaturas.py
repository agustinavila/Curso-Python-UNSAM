#%% 
import matplotlib.pyplot as plt
import numpy as np

#%%
# funcion para plotear

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=70)
    plt.show()
# %%
plotear_temperaturas()
# %%
