from scipy import signal
from pytc2.sistemas_lineales import plot_plantilla
import matplotlib.pyplot as plt
import numpy as np

################## Filtro A #######################
## Funcion de aprox: Chebyshev
## fp: 100Hz
## fs: 300Hz
## alfa_max: 1db
## alfa_min: 60db

fp = 100#Hz
fstop = 300#Hz
alfa_max = 1#db
alfa_min = 60#db
fs=1000#Hz


system_a = signal.iirdesign(fp, fstop, alfa_max, alfa_min,ftype='cheby1',output='sos',fs=fs)
w, h = signal.freqz_sos(system_a,worN=1000,fs=fs)

plt.close('all')

plt.figure()

plt.plot(w,20*np.log10(np.abs(h)))


plt.title('Plantilla de diseño')
plt.xlabel('Frecuencia normalizada a Nyq [#]')
plt.ylabel('Amplitud [dB]')
plt.grid(which='both', axis='both')

#plt.gca().set_xlim([0, 1])

plot_plantilla(filter_type = 'lowpass' , fpass = fp, ripple = alfa_max , fstop = fstop, attenuation = alfa_min, fs = fs)

plt.legend()


################## Filtro B #######################

fnotch=50#HZ
fpass = [fnotch-1,fnotch+1] #Hz
BW=1#HZ
fstop = [fnotch-BW/2,fnotch+BW/2] #Hz
alfa_max = 0.1#db
alfa_min = 3#db
fs=1000#Hz


system_b = signal.iirdesign(fpass, fstop, alfa_max, alfa_min,ftype='cheby1',output='sos',fs=fs)
w, h = signal.freqz_sos(system_b,worN=10000,fs=fs)

plt.figure()

plt.plot(w,20*np.log10(np.abs(h)))


plt.title('Plantilla de diseño')
plt.xlabel('Frecuencia normalizada a Nyq [#]')
plt.ylabel('Amplitud [dB]')
plt.grid(which='both', axis='both')

#plt.gca().set_xlim([0, 1])

plot_plantilla(filter_type = 'bandstop' , fpass = fpass, ripple = alfa_max , fstop = fstop, attenuation = alfa_min, fs = fs)

plt.legend()
