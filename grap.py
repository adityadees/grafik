import numpy as np
import matplotlib.pyplot as plt

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}


plt.rcParams.update(params)
jumlah = 4

data = [
[round(99.9838,2), round(97.9887,2), round(97.8641,2), round(99.9919,2)],
[round(98.0303,2), round(79.8333,2), round(77.4524,2), round(98.9198,2)],
[round(99.9380,2), round(93.3712,2), round(95.3463,2), round(98.9686,2)],
[round(98.1538,2), round(69.2308,2), round(69.2308,2), round(99.0769,2)],
[round(100.0000,2), round(100.0000,2), round(100.0000,2), round(100.0000,2)],

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
                    fontsize='x-large',
                    ha='center', va='bottom')


autolabel(set_all)
autolabel(set_homo)
autolabel(set_syno)
autolabel(set_homosyno)
autolabel(set_nonhomosyno)

fig.tight_layout()
plt.plot(figsize=(2,5))
plt.show()
