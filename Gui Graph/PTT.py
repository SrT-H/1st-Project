import csv
import numpy as np
from   sklearn.svm import SVR
import matplotlib.pyplot as plt
 

months = []
prices = []

def get_data_and_plot(filename, months, prices, name):
	with open(filename, 'r') as csvfile:
		csvFileReader = csv.reader(csvfile)
		for row in csvFileReader:
			months.append(int(row[0].split('.')[1]))
			prices.append(float(row[5]))
			
	months = np.reshape(months,(len(months), 1))

	plt.plot(months, prices, '-')
	plt.xlabel('Months')
	plt.ylabel('Prices')
	plt.title(name)
	plt.legend()
	plt.show()
	return

get_data_and_plot('PTT43200.csv', months, prices, 'PTT Public Company Limited')
