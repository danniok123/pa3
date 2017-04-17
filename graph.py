import math
import csv
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go

file = "results.csv"
txt = np.genfromtxt(file, delimiter = ",")

hillS = list(txt[1:len(txt) - 2, 1])
hillP = list(txt[1:len(txt) - 2, 2])
sim_annS = list(txt[1:len(txt) - 2, 3])
sim_annP = list(txt[1:len(txt) - 2, 4])
reprandS = list(txt[1:len(txt) - 2, 5])
reprandP = list(txt[1:len(txt) - 2, 6])
kk = list(txt[1:len(txt) - 2, 7])

hillS_avg = txt[102, 1]
hillP_avg = txt[102, 2]
simannS_avg = txt[102, 3]
simannP_avg = txt[102, 4]
reprandS_avg = txt[102, 5]
reprandP_avg = txt[102, 6]
kk_avg = txt[102, 7]

print hillS_avg
print hillP

"""plt.plot(hillS)
plt.show()"""

data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

py.iplot(data, filename='basic-bar')