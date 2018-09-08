# Real time stress classification
<br/>
import sys
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from  get_value_sensor import PulseSensor
from detect_peak import detect_peaks
from keras.models import load_model
<br/>
MCP3008.py : Contient le code du convertisseur analogique numérique du même nom 
<br/><br/>
get_pulse.py : Contient le code du capteur photopléthysmographique
<br/><br/>
Stress_classification.ipynb : Contient le code des mesures de la variabilité de la fréquence cardiaque en temps réel, mesures qui sont injectés dans un modèle de classification précédemment construit avec un réseau de neurones
<br/>
<br/>


![GitHub Logo](/images/schéma_final.png)
