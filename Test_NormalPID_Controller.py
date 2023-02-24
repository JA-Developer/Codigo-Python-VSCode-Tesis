import numpy as np
import matplotlib.pyplot as plt
import Libs.AHN_Lib.Con_AHN as Con_AHN
import Libs.PID_Lib.PID as PID
import Libs.TCP_Utils.Controller_Client as Controller_Client
import Libs.Ref_Model_Lib.Reference_Model as Reference_Model
import time

print("CONTROLER")

Client = Controller_Client.ControllerClient('localhost', 10000)

#Crear controlador PID
Controller = PID.PID_Controller(331.95315033054728250210531170863, 123.67852098753624534355637545031
, 222.74056387179722655891266415649)

#Crear redes artificiales de hidrocarburos

Max_U = 100
Min_U = 0

#Proceso de control

U_Signal = 0
DYp_DU = 1

Y_string = ""

Xplot = np.arange(310000)
Yplot = np.zeros(310000)
Refplot = np.zeros(310000)
Uplot = np.zeros(310000)
Timeplot = np.zeros(310000)

Start_Time = time.time()
Time = 0

Yp = 0

Ref_Signal = 0

for t in range(0, 310000):

    Time = time.time() - Start_Time    
    Timeplot[t] = Time
    
    if(Time > 800):
        Ref_Signal = 20
    elif(Time > 600):
        Ref_Signal = 35
    elif(Time > 400):
        Ref_Signal = 15
    elif(Time > 200):
        Ref_Signal = 10
    else:
        Ref_Signal = 30

    Refplot[t] = Ref_Signal
    
    #Solicitar salida de la planta

    Client.sendString("getY")

    #Esperar respuesta de la planta

    Y_string = Client.getString()

    #Obtener salida de la planta
    if(Y_string != ''):
        Yp = float(Y_string)
    Yplot[t] = Yp

    print("Periodo: " + str(t) + ", Salida: " + str(Yp) + ", Kp: " + str(np.abs(Controller.Kp)) + ", Ki: " + str(np.abs(Controller.Ki)) + ", Kd: " + str(np.abs(Controller.Kd)) + ", U: " + str(U_Signal))

    #Calcular error

    E = Ref_Signal - Yp

    #Obtener señal de control

    U_Signal += Controller.PID_Delta_U(E)

    if(U_Signal > Max_U):
        U_Signal = Max_U
    if(U_Signal < Min_U):
        U_Signal = Min_U

    Client.sendString(U_Signal)

plt.plot(Timeplot,Refplot,color='darkred', linestyle='--', label='Reference signal')
plt.plot(Timeplot,Yplot,color='darkblue', label = 'Plant output using the Ziegler-Nichols method')

TestTuning2Yplot = np.load('TestTuning2Yplot.txt.npy')
TestTuning2Timeplot = np.load('TestTuning2Timeplot.txt.npy')

plt.plot(TestTuning2Timeplot, TestTuning2Yplot,color='darkgreen', linestyle='-.', label = 'Plant output using adaptive tuning')

plt.xlabel("Time (s)", size = 16)
plt.ylabel("Value", size = 16)

plt.title("PID tuning test using the Ziegler–Nichols method", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()
plt.grid(True)
plt.show()