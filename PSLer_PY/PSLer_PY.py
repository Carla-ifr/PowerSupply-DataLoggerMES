# --------------------
#  VOLUME GAS METER
# --------------------

# Autor : Carla Isabel Flores Rodriguez 
# References: https://doi.org/10.5281/zenodo.12808300




# Definition of libraries
# ----------------------
import serial
from serial import SerialException
#import serial_open as puerto
import os
import time as time
import csv
import pandas as pd
import datetime as dt 
from dateutil.relativedelta import relativedelta # Time difference
#from drawnow import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec           # gridspec
import sys

# Set up the serial port
# ----------------------
#arduino_port = puerto.str1
arduino_port = 'COM5'              # UBS port name assignation
baud_rate = 9600                   # Bits transference per second 
arduinoData = serial.Serial(arduino_port, baud_rate)
print(arduino_port,' is open', arduinoData.isOpen())
#arduinoData.flushInput()           # Remove junk and noise -> clear the computer's input buffer
arduinoData.reset_input_buffer()
arduinoData.reset_output_buffer()
auxiliarWaiting = 0 

# Data saving variables
# ---------------------
path = os.getcwd()                 # Getting current diretory
root_TemporaryData = path + '\\temporary_measurements\\' # Temporal file directory
root_Data  = path + '\\measurements\\'  # Data file directory
flag = 1                           # Flag for file saving
SavingPeriod = 10                  # Saving period (in minutes)
header = True                      # Name of columns actived

# Data variables
#---------------
temp = 0                           # Reference inicial time
#MeasureTime = 2                    # Measurement time period ('period' defined in arduino)
timeHMS_var = []                   # Time in H-M-S array
t_var  = np.array([])              # Time periods array
y0_var = np.array([])              # Voltage array of sensor #1
y1_var = np.array([])              # Voltage array of sensor #2 
y2_var = np.array([])              # Voltage array of sensor #3
y3_var = np.array([])              # Voltage array of sensor #4

# Data recording
# ---------------
while True:
   
    print('wait ',arduinoData.inWaiting()) 
    while (arduinoData.inWaiting()==0): #  number of bytes in the input buffer

        pass        

    auxiliarWaiting = 0
    print('oye ', arduinoData.inWaiting())
    # Data reading
    ser_bytes = arduinoData.readline()          # read a byte string
    #print('ser_bytes')
    
    # Inicial capture time
    if flag == 1:
        date_inicial = dt.datetime.now()
        flag = 0
    
    # Data read as list
    str_decoded_bytes = ser_bytes.decode()      # decode byte string into Unicode  
    string = str_decoded_bytes.rstrip()         # remove \n and \r
    string = string.split(sep="\t")             # to list
    measurement = [float(i) for i in string]    # from string to float
       
    #print('measurement')
    
    # Capture time of curret measurement
    date = dt.datetime.now()
    timeHMS = date.strftime("%H:%M:%S")
    
    # Relative time
    delta = relativedelta(date,date_inicial)
    # print(delta.minutes)
    
    # Print current measurement in console
    print('\r Heard ',timeHMS,measurement,'                                                              ', end='')
    #time.sleep(2)
        
    # ------------ saving in termporal file-------------------
    with open(root_TemporaryData+"temporal.csv","a") as f:
        writer = csv.writer(f,delimiter=",",lineterminator='\r')
        if header:
            writer.writerow(['Time','Votage1','Voltage2','Voltage3','Voltage4'])
            header = False 
            writer.writerow([date,measurement[0],measurement[1],measurement[2],measurement[3]])
        else:
            writer.writerow([date,measurement[0],measurement[1],measurement[2],measurement[3]])
    
    # Plots Append measurements (within 'SavingPeriod' minutes)
    timeHMS_var.append(timeHMS)
    t_var = np.append(t_var,timeHMS)
    y0_var = np.append(y0_var,measurement[0])
    y1_var = np.append(y1_var,measurement[1])
    y2_var = np.append(y2_var,measurement[2])
    y3_var = np.append(y3_var,measurement[3])
    
    # -----------  saving in memeasurements file ----------
    # Saves the collected data only every 'SavingPeriod' minutes
    if delta.minutes >= SavingPeriod:
        print('Heard  Saving data file...                                                                     ', end='')
        #time.sleep(2)
    
        # Save data
        today = date_inicial.strftime('%Y%m%d%H%M')
        df = pd.DataFrame(columns=['Time','Votage1','Voltage2','Voltage3','Voltage4'])
        df['Time'] = timeHMS_var
        df['Voltage1'] = y0_var
        df['Voltage2'] = y1_var
        df['Voltage3'] = y2_var
        df['Voltage4'] = y3_var
        df.to_csv(root_Data + today + '.csv')


        
        # Plots Variables reset
        timeHMS_var = []
        t_var  = np.array([]) 
        y0_var = np.array([])
        y1_var = np.array([])
        y2_var = np.array([])
        y3_var = np.array([])
        temp = 0
        flag = 1
        
        #arduinoData.flushInput() # Clean buffer
        arduinoData.reset_input_buffer()
        arduinoData.reset_output_buffer()
        
        os.remove(root_TemporaryData+"temporal.csv") # avoid reescribir
        header = True
     

        
           



    
   





    


