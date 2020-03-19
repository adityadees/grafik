import matplotlib.pyplot as plt
import numpy as np


data = [
[0.80443, 0.84176, 0.84278, 0.82316,0.82260],
[0.71956, 0.77691, 0.77279, 0.74522,0.74747],
[0.84256, 0.83268, 0.84152, 0.84204,0.83775],
[0.71956, 0.77691, 0.77279, 0.74522,0.74747],
[0.80320, 0.83787, 0.83933, 0.82087,0.82008],
[0.71956, 0.77043, 0.76772, 0.74286,0.74432],
[0.83641, 0.83009, 0.83847, 0.83743,0.83333],
[0.71956, 0.77043, 0.76772, 0.74286,0.74432],
]


kategori = ['sensitivity', 'Specificity', 'Precision', 'F1-Score', 'Accuracy']

sk1 = plt.plot(kategori, [ x * 100 for x in data[0] ],'s-')
sk2 = plt.plot(kategori, [ x * 100 for x in data[1] ],'s-')
sk3 = plt.plot(kategori, [ x * 100 for x in data[2] ],'s-')
sk4 = plt.plot(kategori, [ x * 100 for x in data[3] ],'s-')
sk5 = plt.plot(kategori, [ x * 100 for x in data[4] ],'s-')
sk6 = plt.plot(kategori, [ x * 100 for x in data[5] ],'s-')
sk7 = plt.plot(kategori, [ x * 100 for x in data[6] ],'s-')
sk8 = plt.plot(kategori, [ x * 100 for x in data[7] ],'s-')
plt.ylim([60, 100])
plt.legend(
    ['Skenario 1',
     'Skenario 2',
     'Skenario 3',
     'Skenario 4',
     'Skenario 5',
     'Skenario 6',
     'Skenario 7',
     'Skenario 8'
     ],
    loc='best'
    )

plt.ylabel('Akurasi')
plt.title('Performance Measurements')
plt.show()
