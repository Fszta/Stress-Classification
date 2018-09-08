# Real time stress classification
<h2>Fonctionnement:</h2>
<ul>
  <li>Filtrage du signal avec un passe-bande de butterworth</li>
  <li>Détection des piques(pulsations cardiaques)</li>
  
  ![GitHub Logo](/images/signal.png)
  
  <li>Extraction des intervalles de temps entre chaque pulsation(intervalle R-R)</li>
  <li>Calcul des mesures de la variabilité cardiaque à partir des R-R "></li>
  
  ![GitHub Logo](/images/formule.png)
  
  <li>Injecte les mesures chaque seconde dans le modèle de classification</li>
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



