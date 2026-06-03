import numpy as np 
import matplotlib.pyplot as plt
import scipy.signal as signal # peforms signal processing functions 
fs = 100 # sampling frequency, sensor is going to collect data 100 times per second,
nyq = fs / 2  # "Nyquist number" the sampling frequency must be twice as high as the signal to avoid distortion maximum detectable frequency 
low = 0.5 / nyq # normalize low cutoff to 0-1 scale (0.5 Hz = 1% of nyquist)
high = 3.0 / nyq # normalize high cutoff to 0-1 scale (3 Hz = 6% of nyquist)
time = np.linspace(0, 10, 1000)
heartbeat = np.sin(2 * np.pi * 1.2 * time)  #simulating heartbeat of 72 beats per min
noise = np.random.normal(0, 0.5, len(time))  # creates random data to simulate the noisy signals 
noisy_signal = heartbeat + noise  # what the real sensor will send us 
b,a = signal.butter(4, [low,high], btype='band')  #creating two arrays of numbers a and b of the signals between 0.5 and 3.0 Hz with a cutoff strength of 4 , the type band pass
filtered = signal.filtfilt(b, a, noisy_signal)
plt.plot(time, noisy_signal, alpha=0.5, label="noisy signal")    #plots a noisy signal on y axis with transparency 0.5 
plt.plot(time,heartbeat, alpha = 1 , label="clean heartbeat" )
plt.plot(time,filtered, alpha = 1 , label = "filtered signal ")
plt.legend() #shows the labels 
plt.show() #shows the actual plot 