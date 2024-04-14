
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
#import numpy as np

file='co2_log2.csv'
data = pd.read_csv(file, delimiter=';')

#time = datetime.strptime(data['time'], "%H:%M")
data['time'] = pd.to_datetime(data['time'], format="%H:%M")
data['datetime'] = data['time']
m = data['datetime'].diff() < pd.Timedelta(0)
data['datetime'] += pd.to_timedelta(m.cumsum(), unit='d')

time = data['datetime'] + pd.DateOffset(years=124, months = 4, days=2)

print(time)

plt.plot(data['datetime'], data['co2'], label='co2')
# plt.plot(data['time'], data['co2'], label='co2')
# plt.xlabel('Time')plt.ylabel('ppm and co2')z
# plt.legend()
plt.show()


# The function reads the data from the csv file and plots the ppm and co2 against time. The function returns the plot.
# The plot shows the ppm and co2 against time.
# The plot is displayed in the console.
# The function is called make_plot.
# The function takes a file as an argument.
# The file is a csv file.

# The function reads the data from the csv file and plots the ppm and co2 against time. The function returns the plot.
# The plot shows the ppm and co2 against time.
# The plot is displayed in the console.

# The function is called make_plot.
