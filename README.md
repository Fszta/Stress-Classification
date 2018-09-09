# Real time stress classification
<h2>Fonctionnement:</h2>
<ul>
  <li><h3>1) Filtrage du signal avec un passe-bande de butterworth</h3></li>
  Utilisation d'un passe-bande d'ordre 4 avec comme fréquences de coupures [0,8 Hz; 4 Hz], ce qui correspond à des fréquences cardiaques de 48 à 240 battements par minute
  <hr/>
  <li><h3>2) Détection des piques (pulsations cardiaques)</h3></li>
  
  ![GitHub Logo](/images/signal.png)
  
  <hr/>
  <li><h3>3) Extraction des intervalles de temps entre chaque pulsation (intervalle R-R)</h3></li>
  
  ![GitHub Logo](/images/Tachogramme.png)
  
  <li><h3>4) Calcul des mesures de la variabilité cardiaque à partir des R-R</h3></li>
  <h4>3 mesures temporelles: </h4><br/>
  
  ![GitHub Logo](/images/formule.png)
  
  <br/>
  <p><b>BPM</b> : nombre de battements par minutes</p>
  <h4>
    1 mesure fréquentielle:
  </h4> 
  <p>Obtenue par transformée de fourier du tachogramme : la balance sympato-vagale <b>(BSV)</b></p>
  
  ![GitHub Logo](/images/bsv.png)
    
  <p>
  <b>BSV</b> = LF/HF avec :
      <ul>
        <li>LF: De 0.04 Hz à 0.15 Hz, reflète l’activité sympathique du système nerveux autonome.</li>
        <li>HF: De 0.15 Hz à 0.4 Hz, reflète l’activité parasympathique du système nerveux autonome</li>
      </ul>     
  </p>
  <li><h3>5) Injecte les mesures chaque seconde dans le modèle de classification</h3></li>
  <p>Les 4 mesures de la VFC sont les features de notre modèle</p>
</ul> 

<h2>Matériel:</h2>
<ul>
  <li>Raspberry pi 3B+ sous Raspbian</li>
  <li>Capteur ppg : <a href="https://pulsesensor.com/">pulse sensor</a></li>
  <li>Convertisseur analogique numérique <a href="/datasheet_MCP/MCP3008.pdf">MCP3008</a></li>
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



