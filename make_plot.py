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

#plot the data
fig, ax = plt.subplots()
ax.plot(time, data['co2'], label='co2')

# Set major ticks format
ax.xaxis.set_major_locator(mdates.DayLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%A'))
ax.tick_params(axis='x', which='major', labelsize=12)
# Set minor ticks format
ax.xaxis.set_minor_locator(mdates.HourLocator(interval=3))
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%H:%M'))

# Rotate and align the tick labels so they look better
#plt.xticks(rotation=45)
fig.autofmt_xdate(rotation=45, ha='right', which='both')

plt.show()
