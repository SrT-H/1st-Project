import csv
import numpy as np
import matplotlib.pyplot as plt
 
class kbank_graph:
	''' KBANK graph '''

	def __init__(self):
		self.months = []
		self.prices = []

	def get_data_and_plot(self, filename, months, prices, name):
		with open(filename, 'r') as csvfile:
			csvFileReader = csv.reader(csvfile)
			for row in csvFileReader:
				self.months.append(int(row[0].split('.')[1]))
				self.prices.append(float(row[5]))

                #reshape the data in fist row which are year, month, date to display only month position
		months = np.reshape(self.months,(len(self.months), 1))

		plt.plot(months, prices, '-')
		plt.xlabel('Months')
		plt.ylabel('Prices')
		plt.title(name)
		plt.legend()
		plt.show()
		return

	def show(self):
		self.get_data_and_plot('KBANK43200.csv', self.months, self.prices, 'Kasikorn Bank Public Company Limited')
