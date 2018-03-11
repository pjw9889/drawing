#-

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


data = np.loadtxt("./Sample.log")

df = pd.DataFrame(data, columns=['A', 'B', 'C'])
df = df.drop('A', 1)

df.plot()
plt.show()




