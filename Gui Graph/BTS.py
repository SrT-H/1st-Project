import csv
import numpy as np
from   sklearn.svm import SVR
import matplotlib.pyplot as plt

class bts:
        def __init__(self):
                self.months = []
                self.prices = []

        def get_data_and_plot(self, filename, months, prices, name):
                with open(filename, 'r') as csvfile:
                        csvFileReader = csv.reader(csvfile)
                        for row in csvFileReader:
                                self.months.append(int(row[0].split('.')[1]))
                                self.prices.append(float(row[5]))
                                
                self.months = np.reshape(months,(len(months), 1))

                plt.plot(self.months, self.prices, '-')
                plt.xlabel('Months')
                plt.ylabel('Prices')
                plt.title(name)
                plt.legend()
                plt.show()
                return

get_data_and_plot('BTS43200.csv', self.months, self.prices, 'BTS Group Holdings Public Company')
