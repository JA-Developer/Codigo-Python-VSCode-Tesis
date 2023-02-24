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
Controller = PID.PID_Controller(0.001, 0.001, 0.0011)

#Crear redes artificiales de hidrocarburos

Max_Kp = 5
Max_Ki = 5
Max_Kd = 5

Max_U = 50
Min_U = -50

Time_Interval = 0.1

N_Identification = 6
N_Tuning = 6

Min_Absolute_Error = 0.1

#Crear redes artificiales de hidrocarburos
Kp_Compound = Con_AHN.AHN_Compound(12, N_Tuning, [20, 20, 20, 20, 20, 20, 20, 20, 100, 100, 100, 100])
Ki_Compound = Con_AHN.AHN_Compound(12, N_Tuning, [20, 20, 20, 20, 20, 20, 20, 20, 100, 100, 100, 100])
Kd_Compound = Con_AHN.AHN_Compound(12, N_Tuning, [20, 20, 20, 20, 20, 20, 20, 20, 100, 100, 100, 100])

#Crear emulador de la planta

Identification_Compound = Con_AHN.AHN_Compound(9, N_Identification, [20, 20, 20, 20, 100, 100, 100, 100, 100])

#Crear modelo de referencia

Ref_Model = Reference_Model.ReferenceModel(1, 1, 10000,1000)

#Proceso de control

U_Signal = 0
DYp_DU = 1

Y_string = ""
PastValues = np.zeros(4)
PastYmValues = np.zeros(4)
PastRefValues = np.zeros(4)
PastUValues = np.zeros(4)

Xplot = np.arange(20000)
Yplot = np.zeros(20000)
Refplot = np.zeros(20000)
Ref_Modelplot = np.zeros(20000)

Kpplot = np.zeros(20000)
Kiplot = np.zeros(20000)
Kdplot = np.zeros(20000)

Start_Period = time.time()

for t in range(0, 20000):

    Kpplot[t] = np.abs(Controller.Kp)
    Kiplot[t] = np.abs(Controller.Ki)
    Kdplot[t] = np.abs(Controller.Kd)

    if(t > 16000):
        Ref_Signal =-6
    elif(t > 12000):
        Ref_Signal = 5
    elif(t > 8000):
        Ref_Signal = 6
    elif(t > 4000):
        Ref_Signal = 4
    else:
        Ref_Signal = -3
    
    Refplot[t] = Ref_Signal

    #Solicitar salida de la planta

    Client.sendString("getY")

    #Esperar respuesta de la planta

    Y_string = Client.getString()

    #Obtener salida de la planta

    Yp = float(Y_string)
    Yplot[t] = Yp

    print("Periodo: " + str(t) + ", Salida: " + str(Yp) + ", Kp: " + str(np.abs(Controller.Kp)) + ", Ki: " + str(np.abs(Controller.Ki)) + ", Kd: " + str(np.abs(Controller.Kd)) + ", U: " + str(U_Signal))

    #Calcular salida de la señal de Ref_Signalerencia

    Ym = Ref_Model.get_output_from_last_values(PastRefValues[0], PastRefValues[1], PastValues[0], PastValues[1])
    
    Ref_Modelplot[t] = Ym

    #Calcular error con respecto al modelo de Ref_Signalerencia

    Ec = Ym - Yp

    #Entrenar Identification_Compound

    X_Train_Identification_Compound = [PastValues[0], PastValues[1], PastValues[2], PastValues[3], U_Signal, PastUValues[0], PastUValues[1], PastUValues[2], PastUValues[3]]

    Yp_Predicted = Identification_Compound.evaluate(X_Train_Identification_Compound)
    Identification_Compound.train_step_with_desired_output(X_Train_Identification_Compound, Yp_Predicted, Yp, 0.0001, 0.00000001, 0.0001)

    End_Period = time.time()
    Time_Elapsed = End_Period - Start_Period
    
    if(Time_Elapsed > Time_Interval):

    #Verificar si se necesita entrenamiento

        Absolute_Error = np.abs(Ym - Yp)
        #print(Absolute_Error)
        Start_Period = End_Period

        if(Absolute_Error > Min_Absolute_Error):
            
            Input = [Ym, PastYmValues[0], PastYmValues[1], PastYmValues[2], Yp, PastValues[0], PastValues[1], PastValues[2], U_Signal, PastUValues[0], PastUValues[1], PastUValues[2]]

            #Calcular DYp_DU

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
                Kp_Compound.train_step_with_derivate(Input, De_DKp, 0.0001, 0.0000001, 0.000001)

            if(not(De_DKi < 0 and np.abs(Controller.Ki) >= Max_Ki)):
                Ki_Compound.train_step_with_derivate(Input, De_DKi, 0.0001, 0.0000001, 0.000001)

            if(not(De_DKd < 0 and np.abs(Controller.Kd) >= Max_Kd)):
                Kd_Compound.train_step_with_derivate(Input, De_DKd, 0.0001, 0.0000001, 0.000001)

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
    
    Client.sendString(U_Signal)
    
    #Actualizar valores pasados

    PastValues[3] = PastValues[2]
    PastValues[2] = PastValues[1]
    PastValues[1] = PastValues[0]
    PastValues[0] = Yp

    PastRefValues[3] = PastRefValues[2]
    PastRefValues[2] = PastRefValues[1]
    PastRefValues[1] = PastRefValues[0]
    PastRefValues[0] = Ref_Signal

    PastUValues[3] = PastUValues[2]
    PastUValues[2] = PastUValues[1]
    PastUValues[1] = PastUValues[0]
    PastUValues[0] = U_Signal

plt.plot(Xplot,Refplot,color='darkred', linestyle='--', label='Reference signal')
plt.plot(Xplot,Ref_Modelplot,color='darkgreen',linestyle='-.', label = 'Reference model output')
plt.plot(Xplot,Yplot,color='darkblue', label = 'Plant output')

plt.xlabel("Iteration (k)", size = 16)
plt.ylabel("Value", size = 16)

plt.title("Tuning test 1", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()
plt.grid(True)
plt.show()

plt.plot(Xplot,Kpplot,color='darkred', linestyle='--', label='Kp')
plt.plot(Xplot,Kiplot,color='darkgreen',linestyle='-.', label = 'Ki')
plt.plot(Xplot,Kdplot,color='darkblue',linestyle='dotted', label = 'Kd')

plt.xlabel("Iteration (k)", size = 16)
plt.ylabel("Value", size = 16)

plt.title("K values for tuning test 1", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()
plt.grid(True)
plt.show()