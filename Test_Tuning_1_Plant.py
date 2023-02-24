import numpy as np
import time
import Libs.AHN_Lib.Con_AHN as Con_AHN
import Libs.TCP_Utils.Plant_Server as Plant_Server

print("PLANT")

class Plant:

    past_values = []
    last_u = 0
    K = 0

    def __init__(self, n_past_values):
        self.past_values = np.zeros(n_past_values)
        self.last_u = 0
    
    def shift_past_values(self, current_value):
        self.past_values[2] = self.past_values[1]
        self.past_values[1] = self.past_values[0]
        self.past_values[0] = current_value

    def get_output(self, u_signal):
                
        if(self.K==0):
            val = self.past_values[0]*self.past_values[1]*(self.past_values[0] + 2.5)/(1 + np.power(self.past_values[0], 2) + np.power(self.past_values[1], 2)) + u_signal
        elif(self.K==1):
            val = u_signal + 0.8*self.last_u + 5*(self.past_values[0]*self.past_values[1])/(1 + np.power(self.past_values[0], 2)+ np.power(self.past_values[1], 2)+ np.power(self.past_values[2], 2))
        else:
            val = 0.3*self.past_values[0] + 0.6*self.past_values[1] + 0.6*np.sin(np.pi*u_signal) + 0.3*np.sin(3*np.pi*u_signal) + 0.1*np.sin(5*np.pi*u_signal)
        
        self.shift_past_values(val)
        self.last_u = u_signal
        return val

#Crear servidor de planta para comunicación TCP/IP
Srvr = Plant_Server.PlantServer('localhost', 10000)
Srvr.listen()

#Planta a controlar

Plant_To_Control = Plant(3)
UCurrent = 0
t = 2

while True:
    t=t+0.01
    Plant_To_Control.K = 1
    #if(t>1000):
        #Plant_To_Control.K = 1
    #elif(t>500):
        #Plant_To_Control.K = 2

    #Calcular salida de planta

    Y = Plant_To_Control.get_output(UCurrent)

    print(str(Plant_To_Control.K) + ', ' + str(Y))

    Received = Srvr.getString(0)
    if(Received == ""):
        pass
    elif(Received == "getY"):
        Srvr.sendString(Y,0)
    else:
        UCurrent = float(Received)
