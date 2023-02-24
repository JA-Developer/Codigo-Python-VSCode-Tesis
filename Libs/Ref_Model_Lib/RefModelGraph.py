import numpy as np
import matplotlib.pyplot as plt
import Reference_Model as Reference_Model
#Crear modelo de referencia

RefM = Reference_Model.ReferenceModel(1, 1, 1000,1000)

print(RefM.coef_U2, RefM.coef_U1, RefM.coef_Y2, RefM.coef_Y1)

#Proceso de control

PastValues = np.zeros(3)
PastU = 0

Xplot = np.arange(100)
Yplot = np.zeros(100)

for t in range(0, 100):
    
    Ref = 6
    
    #Calcular salida de la señal de referencia

    Ref_Output = RefM.get_output_from_last_values(Ref, Ref, PastValues[0], PastValues[1])

    Yplot[t] = Ref_Output

    #Actualizar valores pasados

    PastValues[2] = PastValues[1]
    PastValues[1] = PastValues[0]
    PastValues[0] = Ref_Output

plt.plot(Xplot, Yplot)
plt.show()