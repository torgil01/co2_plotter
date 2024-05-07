import serial
import time

#serial.Serial('/dev/ttyACM0', 9600)
ser = serial.Serial("/dev/ttyACM0", 9600)
f = open("co2_log_rask.csv","a")
f.write("time;tvoc;co2\n")

while True:
    line = ser.readline()  # read input from Arduino
    line = line.decode()
    t = time.localtime()
    print(str(t.tm_hour) + ":" + str(t.tm_min) + ";" + line)
    f.write(str(t.tm_hour) + ":" + str(t.tm_min) + ";" + line)
    f.flush()