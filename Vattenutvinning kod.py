#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 10:16:41 2021

@author: edvineng
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data= pd.read_csv("/Users/edvineng/Documents/Vinylcrackle/matte 2/CHALMERS/Programering/vattenuttag.csv", sep=";")
lista= np.array(data)

xlist=[]
ylist=[]

for i in range(9):
    x=lista[i, 0]
    y=lista[i, 1]
    xlist.append(x)
    ylist.append(y)


xx= np.linspace(1975, 2015)
curvefit= np.polyfit(xlist, ylist, 4)
yfunklist= np.polyval(curvefit, xx)

plt.plot(xlist,ylist, ".")
plt.plot(xx, yfunklist)
