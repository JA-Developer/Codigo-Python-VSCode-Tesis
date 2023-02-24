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
Controller = PID.PID_Controller(0.12, 0.1, 0.1)

#Crear redes artificiales de hidrocarburos

Max_Kp = 500
Max_Ki = 500
Max_Kd = 500

Max_U = 100
Min_U = 0

Time_Interval = 0.1

N_Identification = 3
N_Tuning = 3

Min_Absolute_Error = 0.1

#Crear redes artificiales de hidrocarburos
Kp_Compound = Con_AHN.AHN_Compound(12, N_Tuning, [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200])
Ki_Compound = Con_AHN.AHN_Compound(12, N_Tuning, [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200])
Kd_Compound = Con_AHN.AHN_Compound(12, N_Tuning, [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200])

#Crear emulador de la planta

Identification_Compound = Con_AHN.AHN_Compound(9, N_Identification, [200, 200, 200, 200, 200, 200, 200, 200, 200])
#Crear modelo de referencia

Ref_Model = Reference_Model.ReferenceModel(1, 1, 1000,1000)

#Proceso de control

U_Signal = 0
DYp_DU = 1

Y_string = ""
PastValues = np.zeros(4)
PastYmValues = np.zeros(4)
PastRefValues = np.zeros(4)
PastUValues = np.zeros(4)

Xplot = np.arange(120000)
Yplot = np.zeros(120000)
Refplot = np.zeros(120000)
Ref_Modelplot = np.zeros(120000)
Uplot = np.zeros(120000)
Timeplot = np.zeros(120000)

Kpplot = np.zeros(120000)
Kiplot = np.zeros(120000)
Kdplot = np.zeros(120000)

Start_Time = time.time()
Start_Period = Start_Time

Yp = 0

Ref_Signal = 0

for t in range(0, 120000):

    Time = time.time() - Start_Time    
    Timeplot[t] = Time

    Kpplot[t] = np.abs(Controller.Kp)
    Kiplot[t] = np.abs(Controller.Ki)
    Kdplot[t] = np.abs(Controller.Kd)
    
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

    #Calcular salida de la señal de referencia

    Ym = Ref_Model.get_output_from_last_values(PastRefValues[0], PastRefValues[1], PastValues[0], PastValues[1])
    
    Ref_Modelplot[t] = Ym
    
    #Calcular error con respecto al modelo de referencia

    Ec = Ym - Yp

    #Entrenar Identification_Compound

    X_Train_Identification_Compound = [PastValues[0], PastValues[1], PastValues[2], PastValues[3], U_Signal, PastUValues[0], PastUValues[1], PastUValues[2], PastUValues[3]]

    Yp_Predicted = Identification_Compound.evaluate(X_Train_Identification_Compound)
    Identification_Compound.train_step_with_desired_output(X_Train_Identification_Compound, Yp_Predicted, Yp, 0.001, 0.00000001, 0.0001)

    End_Period = time.time()
    Time_Elapsed = End_Period - Start_Period
    
    if(Time_Elapsed > Time_Interval):
        
        #Verificar si se necesita entrenamiento

        Absolute_Error = np.abs(Ym - Yp)
        #print(Absolute_Error)
        Start_Period = End_Period
        
        if(Absolute_Error > Min_Absolute_Error):
            
            Input = [Ym, PastYmValues[0], PastYmValues[1], PastYmValues[2], Yp, PastValues[0], PastValues[1], PastValues[2], U_Signal, PastUValues[0], PastUValues[1], PastUValues[2]]

            #Calcular Jacobiano

            X_Identification_Compound = [Yp, PastValues[0], PastValues[1], PastValues[2], 2*U_Signal - PastUValues[1], U_Signal, PastUValues[0], PastUValues[1], PastUValues[2]]
            Yp_Predicted = Identification_Compound.evaluate(X_Identification_Compound)

            dU = 2*(U_Signal - PastUValues[1])
            dY = 3*Yp_Predicted - 4*Yp + PastValues[0]

            if(dU != 0):
                DYp_DU = dY/dU

            #Entrenar redes de hidrocarburos

            De_DKp = Ec*DYp_DU*Controller.D_U_Kp()
            De_DKi = Ec*DYp_DU*Controller.D_U_Ki()
            De_DKd = Ec*DYp_DU*Controller.D_U_Kd()

            if(not (De_DKp < 0 and np.abs(Controller.Kp) >= Max_Kp)):
                Kp_Compound.train_step_with_derivate(Input, De_DKp, 0.01, 0.0000001, 0.000001)

            if(not(De_DKi < 0 and np.abs(Controller.Ki) >= Max_Ki)):
                Ki_Compound.train_step_with_derivate(Input, De_DKi, 0.01, 0.0000001, 0.000001)

            if(not(De_DKd < 0 and np.abs(Controller.Kd) >= Max_Kd)):
                Kd_Compound.train_step_with_derivate(Input, De_DKd, 0.01, 0.0000001, 0.000001)

            #Actualizar valores PID
            
            Controller.Kp = Kp_Compound.evaluate(Input)
            Controller.Ki = Ki_Compound.evaluate(Input)
            Controller.Kd = Kd_Compound.evaluate(Input)

            #Asegurarse de que los valores PID esté dentro del rango permitido

            if(Controller.Kp > Max_Kp):
                Controller.Kp = Max_Kp
            if(Controller.Kp < -Max_Kp):
                Controller.Kp = -Max_Kp

            if(Controller.Ki > Max_Ki):
                Controller.Ki = Max_Ki
            if(Controller.Ki < -Max_Ki):
                Controller.Ki = -Max_Ki

            if(Controller.Kd > Max_Kd):
                Controller.Kd = Max_Kd
            if(Controller.Kd < -Max_Kd):
                Controller.Kd = -Max_Kd
    
    #Obtener señal de control

    U_Signal += Controller.PID_Delta_U(Ec)

    if(U_Signal > Max_U):
        U_Signal = Max_U
    if(U_Signal < Min_U):
        U_Signal = Min_U
    
    #if(t >= 100):
        #U_Signal = 30
    #else:
        #U_Signal = 0
    #Uplot[t] = U_Signal
    #Timeplot[t] = Time_Elapsed
    #print(str(Time_Elapsed) + "," + str(U_Signal) + "," + str(Yp))

    Client.sendString(U_Signal)
    
    #Actualizar valores pasados

    PastValues[3] = PastValues[2]
    PastValues[2] = PastValues[1]
    PastValues[1] = PastValues[0]
    PastValues[0] = Yp

    PastYmValues[3] = PastYmValues[2]
    PastYmValues[2] = PastYmValues[1]
    PastYmValues[1] = PastYmValues[0]
    PastYmValues[0] = Ym

    PastRefValues[3] = PastRefValues[2]
    PastRefValues[2] = PastRefValues[1]
    PastRefValues[1] = PastRefValues[0]
    PastRefValues[0] = Ref_Signal

    PastUValues[3] = PastUValues[2]
    PastUValues[2] = PastUValues[1]
    PastUValues[1] = PastUValues[0]
    PastUValues[0] = U_Signal

plt.plot(Timeplot,Refplot,color='darkred', linestyle='--', label='Reference signal')
plt.plot(Timeplot,Ref_Modelplot,color='darkgreen',linestyle='-.', label = 'Reference model output')
plt.plot(Timeplot,Yplot,color='darkblue', label = 'Plant output')

np.save('TestTuning2Yplot.txt', Yplot)
np.save('TestTuning2Timeplot.txt', Timeplot)

#plt.plot(Xplot,Uplot,color='darkred', linestyle='--', label = 'U signal')

#mvar = (Yplot[1030] - Yplot[1010])/(Timeplot[1030] - Timeplot[1010])
#bvar = Yplot[1030] - mvar*Timeplot[1030]

#Linea = mvar*Timeplot + bvar

#plt.plot(Timeplot,Linea,color='darkgreen', linestyle='dotted', label = 'Tangent line')

plt.xlabel("Time (s)", size = 16)
plt.ylabel("Value", size = 16)

plt.title("Tuning test 2", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()
plt.grid(True)
plt.show()

plt.plot(Timeplot,Kpplot,color='darkred', linestyle='--', label='Kp')
plt.plot(Timeplot,Kiplot,color='darkgreen',linestyle='-.', label = 'Ki')
plt.plot(Timeplot,Kdplot,color='darkblue',linestyle='dotted', label = 'Kd')

plt.xlabel("Time (s)", size = 16)
plt.ylabel("Value", size = 16)

plt.title("K values for tuning test 2", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()
plt.grid(True)
plt.show()