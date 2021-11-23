from matplotlib import pyplot as plt
import numpy as np
import time
plt.style.use('fivethirtyeight')
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.xlabel("Age")
plt.plot(dev_x,dev_y,label='ppppp')
plt.ylabel("median salary")
plt.title("test")
py_dev_x = np.arange(0,11,1)
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(py_dev_x,py_dev_y,'mo:',label='wahed')   
plt.legend()
plt.grid(1)
plt.tight_layout()
plt.show()