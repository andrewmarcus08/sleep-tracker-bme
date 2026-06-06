import numpy as np       #imports numpy library called np, numpy can do math on every number in an array at once 
import matplotlib.pyplot as plt  #plots things 
import scipy.signal as signal   #peforms signal processing functions 
time = np.linspace(1, 10, 1000)  #10 seconds of time, 1000 data points 
heartbeat = np.sin(2 * np.pi * 1.2 * time)  #simulating heartbeat of 72 beats per min
noise = np.random.normal(0, 0.5, len(time))  # creates random data to simulate the noisy signals 
noisy_signal = heartbeat + noise  # what the real sensor will send us 
plt.plot(time, noisy_signal, alpha=0.5, label="noisy signal")    #plots a noisy signal on y axis with transparency 0.5 
plt.plot(time,heartbeat, alpha = 1 , label="clean heartbeat" )
plt.legend() #shows the labels 
plt.show() #shows the actual plot 







