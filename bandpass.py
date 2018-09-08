import numpy as np
import time
from scipy.signal import butter, lfilter,freqz,filtfilt

# Implementation du filtre passe bande de Butterworth

def butter_bandpass(lowcut,highcut,fe,order):

	nyq = 0.5* fe
	low = lowcut/nyq
	high = highcut/nyq
	b,a = butter(order,[low,high],btype='band')
	return b,a

def butter_bandpass_filter(data,lowcut,highcut,fe,order):

	b,a  =  butter_bandpass(lowcut,highcut,fe,order=order)
	y = filtfilt(b,a,np.ravel(data))
	return y

def run(x,fs,f_l,f_h,order):

	x = x+np.mean(x)
	lowcut = f_l
	highcut = f_h
	y = butter_bandpass_filter(x,lowcut,highcut,fs,order=order)
	return y


