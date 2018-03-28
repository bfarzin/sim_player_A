import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import ipdb


X = np.array([list(i) for i in itertools.product([0,1],repeat=4)])
y = X.sum(axis=1)

alpha = 1.
beta  = 1.

def return_E_R1(alpha,beta,X,y):
    y_1 = (alpha*X[:,:2]).sum(axis=1)
    e_1 = y - y_1
    
    y_2 = (beta*X[:,1:]).sum(axis=1)
    e_2 = y - y_2
    
    R1 = np.zeros_like(y)
    R2 = np.zeros_like(y)
    
    R1[abs(e_1)<abs(e_2)] = y[abs(e_1)<abs(e_2)]
    E_R  = np.mean(y)
    E_R1 = np.mean(R1)
    # E_R2 = E_R-E_R1
    return E_R1

gran = 500
out = np.zeros((gran,gran))
for ii,alpha in enumerate(np.linspace(0,5,gran)[::-1]):
    for jj,beta in enumerate(np.linspace(0,5,gran)):
        out[ii,jj] = return_E_R1(alpha,beta,X,y)

## max(alpha) min(beta) R1 is best guaranteed reward (player A)
print(np.max(out.min(axis=1)))
   
sns.heatmap(out)
plt.show()        
ipdb.set_trace()
