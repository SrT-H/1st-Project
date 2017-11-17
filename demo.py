import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

class set50:

    #plt.switch_backend('Qt5Agg')
    def __init__(self):
        self.dates = []
        self.prices = []

    def get_data(self, filename):
        with open(filename, 'r') as csvfile:
            csvFileReader = csv.reader(csvfile)
            next(csvFileReader)	# skipping column names
            for row in csvFileReader:
                self.dates.append((row[0]))
                self.prices.append(float(row[5]))
        return

    def predict_price(self, dates, prices, x):
        self.dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1

        plt.scatter(self.dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('SET50 Graph')
        plt.legend()
        plt.show()

    def create_graph(self):
        self.get_data('S50Z171440.csv') # calling get_data method by passing the csv file to it
        print("Dates- ", self.dates)
        print("Prices- ", self.prices)

        predicted_price = self.predict_price(self.dates, self.prices, 29)
        print(predicted_price)

