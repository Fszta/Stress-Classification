
# coding: utf-8
__author__='Ferszterowski Antoine, antoinefer@hotmail.com'

import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from  get_value_sensor import PulseSensor
from detect_peak import detect_peaks
from keras.models import load_model


class GetHrv():
    """Calculs des mesures de la HRV à partir du capteur ppg contact"""

    def __init__(self, time_ppg, amplitude_ppg):
        self.time_ppg = time_ppg
        self.amplitude_ppg = amplitude_ppg
        self.peak_list = []
        self.rr_list = []
        self.rr_diff = []
        self.rr_square_diff = []

    def run(self):
        """Execution"""

        # Détection des piques
        self.detect_peak()

        # Extraction des intervalles R-R
        self.get_rr_interval()

        # Extraction de la différence des R-R
        self.get_rr_interval_diff()

        # Calcul des grandeurs temporelles
        self.time_statistical_measures()

        # Transformée de fourier du tachogramme
        self.fast_fourier_transform()

        # Calcul du rapport LF/HF, balance sympatho-vagale
        self.frequency_measures()

    def detect_peak(self):
        """Détection des piques R du signal PPG"""

        # Obtention de l'indices des piques
        self.index_peak = detect_peaks(self.amplitude_ppg,show=True,mph=50,mpd = 60)

        # Obtention du temps correspondant aux indices
        [self.peak_list.append(self.time_ppg[i]) for i in self.index_peak]

    def get_rr_interval(self):
        """Obtention des intervalles rr"""

        [self.rr_list.append(abs(self.peak_list[i] - self.peak_list[i+1])*1000) for i in range(1,len(self.peak_list)-1)]
        for i in self.rr_list:
            if i > 1400:
                self.rr_list.remove(i)
            elif i < 600:
                self.rr_list.remove(i)

    def get_rr_interval_diff(self):
        """Obtention de la différence des R-R"""

        i = 0
        while i < len(self.rr_list) - 1 :
            self.rr_diff.append((abs(self.rr_list[i] - self.rr_list[i+1])))
            self.rr_square_diff.append(math.pow(self.rr_list[i] - self.rr_list[i+1], 2))
            i += 1

    def time_statistical_measures(self):
        """Calcul des mesures temporelles de la HRV"""

        self.sdnn = np.std(self.rr_list)
        self.rmssd = np.sqrt((np.mean(self.rr_square_diff)))
        self.bpm = 60 * (len(self.index_peak)) /             (self.time_ppg[-1] - self.time_ppg[0])
        self.icf = 60000/(self.rr_list[-1])
        self.ibi = (np.mean(self.rr_list))
        self.bpm = 60000 / self.ibi
        

        print("BPM:",self.bpm)
        print("RMSSD:",self.rmssd)
        print("SDNN:",self.sdnn)
        
    def fast_fourier_transform(self):
        """Transformée de fourier rapide"""
        f = 1
        n = len(self.rr_list)
        self.frq = np.fft.fftfreq(n,d=(1./f))
        self.frq = self.frq[range(n//2)]
        self.Y = np.fft.fft(self.rr_list)/n
        self.Y = self.Y[range(n//2)]

    def frequency_measures(self):
        """Calcul du rapport LF/HF"""

        lf = np.trapz(abs(self.Y[(self.frq >= 0.04) & (self.frq <= 0.15)]))
        hf = np.trapz(abs(self.Y[(self.frq >= 0.15) & (self.frq <= 0.4)]))
        self.bsv = lf/hf
        print(self.bsv)

    def get_measures(self):
        return self.bpm, self.rmssd, self.sdnn, self.bsv
    

class TestSensor():

    """ Code pour tester le bon positionnement du capteur sur le doigt"""
    def __init__(self):
        self.pulse_sensor = PulseSensor()
        self.time_init = time.time()
        self.fs_sensor = 150
        
    def get_window(self):
        """Récupère les valeurs du capteur dans une fenêtre de 30s"""
        
        self.value_pulse, self.time_pulse, _ = self.pulse_sensor.get_value()
        if len(self.value_pulse) > self.fs_sensor*30:
            self.value_pulse = self.value_pulse[len(self.value_pulse)-self.fs_sensor*30:]
            self.time_pulse = self.time_pulse[len(self.time_pulse)-self.fs_sensor*30:]
            
    def get_hrv_measures(self):
        """Récupère 4 quantités de la variabilité cardiaque"""
        hrv = GetHrv(self.time_pulse,self.value_pulse)
        hrv.run()
        self.bpm, self.rmssd, self.sdnn, self.bsv = hrv.get_measures()
        if self.rmssd > 100:
            self.rmssd = 50
        if self.sdnn > 100:
            self.sdnn = 60
            
    def predict_state(self):
        """Prédiction à partir des 4 paramètres physiologiques de la HRV"""
        
        X = np.array([[self.bpm,self.rmssd ,self.bsv,self.sdnn]])
        print(self.model.predict_classes(X))
        
        if self.model.predict_classes(X) == [0]:
            self.state = "relax"
        else:
            self.state = "stress"
        print(self.state)
        
    def run(self):
        """Récupère les valeurs du capteur après 15 secondes"""
        
        print("Debut capture...")
        self.pulse_sensor.start()
        self.model = load_model('model.h5')
        
        try : 
            while True:
                clear_output(wait=True)
                time.sleep(0.5)
                if time.time() - self.time_init > 15:
                    self.get_window()
                    self.get_hrv_measures()
                    self.predict_state()
                    
        except KeyboardInterrupt:
            self.pulse_sensor.stop_capture()
            print('Fin capture')


def Programm():
    test_sensor = TestSensor()
    test_sensor.run()
                             
if __name__ == '__main__':
    Programm()

