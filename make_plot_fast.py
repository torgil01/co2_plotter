# import libs
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import argparse
from datetime import datetime


#parse input arguments 
parser = argparse.ArgumentParser(description='Plot the data from the csv file')
parser.add_argument('-i','--input', type=str, help='The csv file to read the data from')
args = parser.parse_args()
file = args.input

#read the data from the csv file into a pandas dataframe called "data"
data = pd.read_csv(file, delimiter=';')
# the dataframe has three columsn, 
# time, co2, and ppm

# the time column is in the format HH:MM but since the logging 
# goes over several days we need to convert it to a datetime object 
# so that we get the correct data for the time series
# first we convert the time column to a datetime object
data['time'] = pd.to_datetime(data['time'], format="%H:%M")
# next we make a new column called datetime which is a copy of the time column
num_rows = data.shape[0]
seconds = np.arange(0, num_rows)*2 
#float(range(0, num_rows))*2


# Create a figure and a set of subplots
# co2 data is on the 1st axis
fig, (ax1, ax2) = plt.subplots(2,1, tight_layout=True) 
ax1.plot(seconds, data['co2'], label='co2')

# Rotate and align the tick labels so they look better
#plt.xticks(rotation=45)
import matplotlib.pyplot as plt

# add labels
ax1.set_xlabel('Time (sec)', fontsize=16)
ax1.set_ylabel('CO2', fontsize=16)

ax2.plot(seconds, data['tvoc'], label='tvoc')
ax2.set_xlabel('Time', fontsize=16)
ax2.set_ylabel('tvoc', fontsize=16)

# Set major ticks format

plt.show()
