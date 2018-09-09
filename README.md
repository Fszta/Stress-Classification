# Real time stress classification
<h2>Fonctionnement:</h2>
<ul>
  <li><h3>Filtrage du signal avec un passe-bande de butterworth</h3></li>
  Utilisation d'un passe-bande d'ordre 4 avec comme fréquences de coupures [0,8 Hz; 4 Hz], ce qui correspond à des fréquences cardiaques de 48 à 240 battements par minute
  <li><h3>Détection des piques(pulsations cardiaques)</h3></li>
  
  ![GitHub Logo](/images/signal.png)
  
  <li><h3>Extraction des intervalles de temps entre chaque pulsation(intervalle R-R)</h3></li>
  
  ![GitHub Logo](/images/Tachogramme.png)
  
  <li><h3>Calcul des mesures de la variabilité cardiaque à partir des R-R</h3></li>
  <p> 4 mesures utilisées : </p> <br/>
  
  ![GitHub Logo](/images/formule.png)
  
  <br/>
  <p>BPM : nombre de battements par minutes</p>
  <p>1 mesure fréquentielle obtenue par transformée de fourier du tachogramme : la balance sympato-vagale <i>(BSV)</i></p>
  <p align="center">
  
  ![GitHub Logo](/images/bsv.png)
  
  </p>
  
  
  <li><h3>Injecte les mesures chaque seconde dans le modèle de classification</h3></li>
  <p>Les 4 mesures de la VFC sont les features de notre modèle</p>
</ul> 

<h2>Matériel:</h2>
<ul>
  <li>Raspberry pi 3B+ sous Raspbian</li>
  <li>Capteur ppg : <a href="https://pulsesensor.com/">pulse sensor</a></li>
  <li>Convertisseur analogique numérique <a href="/datasheet_MCP/MCP3008.pdf">MCP3008</a></li>
  <li>matplotib</li>
  <li>keras</li>
</ul> 

<h2>Librairies:</h2>
<ul>
  <li>spidev</li>
  <li>numpy</li>
  <li>scipy</li>
  <li>matplotib</li>
  <li>keras</li>
</ul> 

<h2>Codes:</h2>
 <ul>
  <li>MCP3008.py: Code du convertisseur analogique numérique du même nom </li>
  <li>get_pulse.py: Code du capteur photopléthysmographique</li>
  <li>Stress_classification.py: Contient le code des mesures de la variabilité de la fréquence cardiaque en temps réel, mesures qui sont injectés dans un modèle de classification précédemment construit avec un réseau de neurones</li>
 <li>bandpass.py: Filtre passe bande de butterworth</li>
 <li>detect_peak.py: Algorithme de détection de piques </li>

</ul> 

<h2>Schéma électronique:</h2>

![GitHub Logo](/images/schéma_final.png)



