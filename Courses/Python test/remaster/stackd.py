import matplotlib.pyplot as plt
import numpy as np
plt.stackplot(np.arange(1,11),np.random.randint(1,9,10),np.random.randint(1,9,10))
plt.show()