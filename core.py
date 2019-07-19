import threading
import serial
import time
import glob
import os

ser = serial.Serial('/dev/ttyACM1')

while True:
        if glob.glob('outbox/*.txt'):
                files = glob.glob('outbox/*.txt')
                data = open(files[0], "r").read()
                split = [data[i:i+190] for i in range(0, len(data), 190)]
                for i in split:
                        print ser.write(b'<'+i+'>')
                os.remove(files[0])
        else:
                if (ser.inWaiting()>0):
                        data_str = ser.read(ser.inWaiting()).decode('ascii')
                        open("inbox/data.txt", "ab").write(data_str)
                        print(data_str)
        time.sleep(0.01)

