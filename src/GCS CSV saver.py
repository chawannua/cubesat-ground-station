import serial
import csv

# Open the serial port
ser = serial.Serial('COM5', 9600)

# Create a CSV file and write headers
with open('midflight.csv', mode='w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Package' ,'Time', 'Temp', 'Axis X', 'Axis Y', 'Axis Z','Latitude','Longitude'])
    # Loop to continuously read data from the serial port and write to CSV file
    while True:
        data = ser.readline().decode('utf-8').strip()
        file.write((data))
        file.write('\n')
        print(data)
            
########## ต้องหยุดการทำงานโดยใช้ ctrl+c เท่านั้น  ถ้า error หรืออะไร เปลี่ยนชื่อแล้วรันใหม่