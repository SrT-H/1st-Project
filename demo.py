import csv
import numpy as np
from   sklearn.svm import SVR
import matplotlib.pyplot as plt

#plt.switch_backend('Qt5Agg')  

dates = []
prices = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)	# skipping column names
        for row in csvFileReader:
            dates.append((row[0]))
            prices.append(float(row[5]))
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates,(len(dates), 1)) # converting to matrix of n X 1

    plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('SET50 Graph')
    plt.legend()
    plt.show()

get_data('S50Z171440.csv') # calling get_data method by passing the csv file to it
print("Dates- ", dates)
print("Prices- ", prices)

predicted_price = predict_price(dates, prices, 29)
print(predicted_price)
