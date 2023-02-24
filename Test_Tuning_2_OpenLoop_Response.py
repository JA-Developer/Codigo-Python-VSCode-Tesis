import numpy as np
import matplotlib.pyplot as plt
import Libs.AHN_Lib.Con_AHN as Con_AHN
import Libs.PID_Lib.PID as PID
import Libs.TCP_Utils.Controller_Client as Controller_Client
import Libs.Ref_Model_Lib.Reference_Model as Reference_Model
import time

print("CONTROLER")

Client = Controller_Client.ControllerClient('localhost', 10000)

#Crear redes artificiales de hidrocarburos

Max_U = 100
Min_U = 0

#Proceso de control

U_Signal = 0

Y_string = ""


Stableplot = np.ones(300000)*21.777777777777777777777777777778
Xplot = np.arange(300000)
Yplot = np.zeros(300000)
Uplot = np.zeros(300000)
Timeplot = np.zeros(300000)

Start_Time = time.time()
Time = 0

Yp = 0

Ref_Signal = 0

for t in range(0, 300000):

    Time = time.time() - Start_Time    
    Timeplot[t] = Time
    
    if(t > 500):
        U_Signal = 50
    else:
        U_Signal = 0
    
    #Solicitar salida de la planta

    Client.sendString("getY")

    #Esperar respuesta de la planta

    Y_string = Client.getString()

    #Obtener salida de la planta
    if(Y_string != ''):
        Yp = float(Y_string)
    Yplot[t] = Yp

    print("Periodo: " + str(t) + ", Salida: " + str(Yp) +  ", U: " + str(U_Signal))

    if(U_Signal > Max_U):
        U_Signal = Max_U
    if(U_Signal < Min_U):
        U_Signal = Min_U
    
    Uplot[t] = U_Signal

    Client.sendString(U_Signal)

plt.plot(Timeplot,Uplot,color='darkred', linestyle='--', label='U signal')
plt.plot(Timeplot,Stableplot,color='orange', linestyle='dotted', label='Stabilization value')
plt.plot(Timeplot,Yplot,color='darkblue', label = 'Plant output')

m = (Yplot[1000] - Yplot[2000])/(Timeplot[1000] - Timeplot[2000])
b = Yplot[1000] - m*Timeplot[1000]

Rectplot = m*Timeplot + b

plt.plot(Timeplot,Rectplot,color='darkgreen', linestyle='-.', label='Tangent line')

plt.xlabel("Time (s)", size = 16)
plt.ylabel("Value", size = 16)

plt.title("Open loop response in two tank system", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()
plt.grid(True)
plt.show()