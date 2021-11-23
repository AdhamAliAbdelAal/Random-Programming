import numpy as np 
data=np.genfromtxt('Book1.csv')

print(np.median(data),np.mean(data),np.std(data),np.sum(data))