import time
import Libs.AHN_Lib.Con_AHN as Con_AHN
import Libs.TCP_Utils.Plant_Server as Plant_Server
import cmath

print("Tank")

#Crear servidor de planta para comunicación TCP/IP
Srvr = Plant_Server.PlantServer('localhost', 10000)
Srvr.listen()

#Planta a controlar

T = 0.1

C = 280

H1 = 0
H2 = 0

UCurrent = 100
K1 = 30
K2 = 30

A1 = 289
A2 = 144

t = 0

LastPeriod = time.time()

Q1 = 0
H1 = 0
Q12 = 0
H2 = 0
Q2 = 0

while True:

    ThisPeriod = time.time()
    Time_Elapsed = ThisPeriod - LastPeriod
    LastPeriod = ThisPeriod

    t = t + Time_Elapsed

    if(t>400):
        K2 = 10

    #

    Q1 = UCurrent*C/100

    Q2 = K2 * cmath.sqrt(H2)

    Q12 = K1 * cmath.sqrt(H1 - H2)

    #

    dH2_dt = (Q12 - Q2)/A2

    H2 += dH2_dt*Time_Elapsed

    #

    Q1 = UCurrent*C/100

    Q2 = K2 * cmath.sqrt(H2)

    Q12 = K1 * cmath.sqrt(H1 - H2)

    #

    dH1_dt = (Q1 - Q2)/A1

    H1 += dH1_dt*Time_Elapsed

    #

    print(str(t) + ", " + str(UCurrent) + ", " + str(H2))

    Received = Srvr.getString(0)
    if(Received == ""):
        pass
    elif(Received == "getY"):
        Srvr.sendString(H2.real, 0)
    else:
        UCurrent = float(Received)
        if(UCurrent >= 100):
            UCurrent = 100