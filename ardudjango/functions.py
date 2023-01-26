# place here all the functions to be run
import serial
import matplotlib.pyplot as plt
from drawnow import *

ardudata=serial.Serial('com3', 9600)
sensor1Data=[]
sensor2Data=[]

def streamer():
    def makePlot(): # create a function to plot the data 
        plt.plot(sensor1Data,'-r')
        plt.grid(True)
        plt.ylabel('Data')
        plt.title('Live Stream Data')
        plt2=plt.twinx() # create another axis for the plot of data2
        plt2.plot(sensor2Data,'-o')
        plt.legend(['data1', 'data2'])
    
    while True:
        if(ardudata.inWaiting()>0):
            data=ardudata.readline()
            array1=float(data[0])
            array2=float(data[1])
            sensor1Data.append(array1)
            sensor2Data.append(array2)
            drawnow(makePlot)
            plt.pause(0.00001) # pause the plot a little.  