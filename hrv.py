import numpy as np # peforms math on multiple arrays at once
import scipy.signal as signal # peforms signal processing functions 
import matplotlib.pyplot as plt # does plotting 
fs = 100
nyq = fs / 2 
low = 0.5 / nyq 
high = 3.0 / nyq 
time = np.linspace(0,10,1000)
heartbeat = np.sin(2 * np.pi * 1.2 * time)
noise = np.random.normal(0, 0.5, len(time))  
noisy_signal = heartbeat + noise
b,a = signal.butter(4,[low,high], btype = 'band')
filtered = signal.filtfilt(b,a, noisy_signal)
plt.plot(time, noisy_signal, alpha=0.5, label="noisy signal")    #plots a noisy signal on y axis with transparency 0.5 
plt.plot(time,heartbeat, alpha = 1 , label="clean heartbeat" )
plt.plot(time,filtered, alpha = 1 , label = "filtered signal ")
plt.legend() #shows the labels 
plt.show() #shows the actual plot 
