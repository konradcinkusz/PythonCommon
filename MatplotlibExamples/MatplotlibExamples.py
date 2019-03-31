#%%
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as patches
from matplotlib.path import Path

matplotlib.interactive(True)
plt.ion()
matplotlib.is_interactive()

#%%
stock_data = pd.read_csv(r"E:\Sprawy akademickie\Python\Common\MatplotlibExamples\datasets\stocks.csv")
stock_data.head()