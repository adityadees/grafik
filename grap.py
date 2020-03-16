import numpy as np
import matplotlib.pyplot as plt


jumlah = 4

data = [
[99.9838, 97.9887, 97.8641, 99.9919],
[98.0303, 79.8333, 77.4524, 98.9198],
[99.9380, 93.3712, 95.3463, 98.9686],
[98.1538, 69.2308, 69.2308, 99.0769],
[100.0000, 100.0000, 100.0000, 100.0000],

]

fig, ax = plt.subplots()

index = np.arange(jumlah)
lebar = 0.65

index = np.arange(0, jumlah * 4, 4)
set_all = plt.bar(index , data[0], lebar,
                 label='ALL TEST')

set_homo = plt.bar(index + lebar, data[1], lebar,
                 label='HOMONYM TEST')

set_syno = plt.bar(index + lebar + lebar, data[2], lebar,
                 label='SYNONYM TEST')
set_homosyno = plt.bar(index + lebar + lebar + lebar, data[3], lebar,
                 label='HOMONYM-SYNONYM TEST')
set_nonhomosyno = plt.bar(index + lebar + lebar + lebar+ lebar, data[4], lebar,
                 label='NON HOMO-SYNONYM TEST')
plt.ylabel('Means Accuracy')
plt.title('DNN Testing Graph')
plt.xticks(index + lebar + lebar, ('Accuracy', 'Precision', 'Recall', 'F1-Score'))
plt.legend(loc='lower left')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(set_all)
autolabel(set_homo)
autolabel(set_syno)
autolabel(set_homosyno)
autolabel(set_nonhomosyno)

fig.tight_layout()
plt.plot(figsize=(2,5))
plt.show()
