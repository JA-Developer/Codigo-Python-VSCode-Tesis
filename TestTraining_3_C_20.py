import numpy as np
import matplotlib.pyplot as plt
import Libs.AHN_Lib.Con_AHN as Con_AHN

def Fn(x):
    return np.sin(12*x)

Samples = np.arange(-1, 1, 0.01)
N = 5

#Crear redes artificiales de hidrocarburos
Compound = Con_AHN.AHN_Compound(1, N, [1])

#Agregar centros de moléculas
Compound.centers_of_molecules = Compound.centers_of_molecules = [[-1], [-0.5], [0], [0.5], [1]]

Compound.c = 20

for epoch in range(0, 2000):

    print(epoch)

    for t in Samples:

        X = [t]

        Real_Y = Compound.evaluate(X)

        Desired_Y = Fn(t)

        Compound.train_step_with_desired_output(X, Real_Y, Desired_Y, 0.01, 0.0000001, 0)

Xplot = np.zeros(len(Samples))
Yplot = np.zeros(len(Samples))
Refplot = np.zeros(len(Samples))

Error = 0
i = 0

for t in Samples:

    X = [t]

    Real_Y = Compound.evaluate(X)
    Desired_Y = Fn(t)
    
    Error += np.power(Real_Y - Desired_Y, 2)

    print(Real_Y)

    Xplot[i] = t

    Yplot[i] = Real_Y
    Refplot[i] = Desired_Y
    i += 1

print(Error)
print(Compound.atoms_values)
print(Compound.centers_of_molecules)

plt.plot(Xplot, Yplot,color='darkred', linestyle='--', label='Salida obtenida')
plt.plot(Xplot, Refplot,color='darkgreen',linestyle='-.', label='Salida deseada')

plt.xlabel("X", size = 16)
plt.ylabel("Y", size = 16)

plt.title("Prueba de entrenamiento con c = 1", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()

plt.grid(True)
plt.show()