import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import mplcursors

data = {'jenis': ['set1', 'set2', 'set3', 'set4', 'set5'],
        'data1': [0.80443, 0.84176, 0.84278, 0.82316, 0.82260],
        'data2': [0.71956, 0.77691, 0.77279, 0.74522, 0.74747],
        'data3': [0.84256, 0.83268, 0.84152, 0.84204, 0.83775],
        'data4': [0.71956, 0.77691, 0.77279, 0.74522, 0.74747],
        'data5': [0.80320, 0.83787, 0.83933, 0.82087, 0.82008],
        'data6': [0.71956, 0.77043, 0.76772, 0.74286, 0.74432],
        'data7': [0.83641, 0.83009, 0.83847, 0.83743, 0.83333],
        'data8': [0.71956, 0.77043, 0.76772, 0.74286, 0.74432]}
df = pd.DataFrame.from_dict(data)

fig = plt.figure(figsize=(8, 4))
ax1 = plt.subplot(111)
for i, data_col in enumerate( df.columns[1:]):
    ax1.plot(df.jenis, [x * 100 for x in df[data_col]], 's-', label=f'Skenario {i+1}')
plt.ylim([60, 100])


for data_col in df.columns[1:]:
    for i,j in df[data_col].items():
         ax1.annotate(str(j), xy=(i, j*100))

mplcursors.cursor(hover=True)

plt.ylabel('Akurasi')
plt.title('Performance Measurements')
plt.legend(loc='best')
plt.show()
