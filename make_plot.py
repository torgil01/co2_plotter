# import libs
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
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
data['datetime'] = data['time']
# next we take the differenec of the datetime column to find the time difference between
# consequtive rows, if the difference is negative it means that the time has wrapped around
m = data['datetime'].diff() < pd.Timedelta(0)
# next we add a day each time timediff is negative
data['datetime'] += pd.to_timedelta(m.cumsum(), unit='d')
# finally, since datetime starta at 1900-01-01 we add 124 years, 4 months and 12 days
# to get the correct date 
time = data['datetime'] + pd.DateOffset(years=124, months = 4, days=12)

print(time)

# Create a figure and a set of subplots
# co2 data is on the 1st axis
fig, (ax1, ax2) = plt.subplots(2,1, tight_layout=True) 
ax1.plot(time, data['co2'], label='co2')

# Set major ticks format
ax1.xaxis.set_major_locator(mdates.DayLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%a'))
ax1.tick_params(axis='x', which='major', labelsize=12,pad=20)
# Set minor ticks format
ax1.xaxis.set_minor_locator(mdates.HourLocator(interval=3))
ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))

# Rotate and align the tick labels so they look better
#plt.xticks(rotation=45)
import matplotlib.pyplot as plt

# add labels
ax1.set_xlabel('Time', fontsize=16)
ax1.set_ylabel('CO2', fontsize=16)

ax2.plot(time, data['tvoc'], label='tvoc')
ax2.set_xlabel('Time', fontsize=16)
ax2.set_ylabel('tvoc', fontsize=16)

# Set major ticks format
ax2.xaxis.set_major_locator(mdates.DayLocator())
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%A'))
ax2.tick_params(axis='x', which='major', labelsize=12, pad=20, rotation=45)
# Set minor ticks format
ax2.xaxis.set_minor_locator(mdates.HourLocator(interval=6))
ax2.xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
ax2.tick_params(axis='x', which='minor', labelsize=9, rotation=45)

plt.show()
