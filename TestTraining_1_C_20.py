import numpy as np
import matplotlib.pyplot as plt
import Libs.AHN_Lib.Con_AHN as Con_AHN

Samples = 100
N = 5

#Crear redes artificiales de hidrocarburos
Compound = Con_AHN.AHN_Compound(1, N, [1])

Compound.centers_of_molecules = [[0], [0.25], [0.5], [0.75], [1]]

Compound.c = 20

for epoch in range(0, 2000):

    print(epoch)

    for t in range(0, Samples):

        x_value = 0.01*t

        X = [x_value]

        Real_Y = Compound.evaluate(X)

        Desired_Y = np.sin(5*x_value)*np.sin(2*x_value + 4) + np.cos(x_value) + (1/(1 + np.sin(0.5*x_value))) + np.cos(10*x_value)

        Compound.train_step_with_desired_output(X, Real_Y, Desired_Y, 0.01, 0.0000001, 0)

Xplot = np.zeros(Samples)
Yplot = np.zeros(Samples)
Refplot = np.zeros(Samples)

Error = 0

for t in range(0, Samples):

    x_value = 0.01*t

    X = [x_value]

    Real_Y = Compound.evaluate(X)
    Desired_Y = np.sin(5*x_value)*np.sin(2*x_value + 4) + np.cos(x_value) + (1/(1 + np.sin(0.5*x_value))) + np.cos(10*x_value)
    
    Error += np.power(Real_Y - Desired_Y, 2)

    print(Real_Y)

    Xplot[t] = x_value

    Yplot[t] = Real_Y
    Refplot[t] = Desired_Y

print(Error)
print(Compound.atoms_values)
print(Compound.centers_of_molecules)

plt.plot(Xplot, Yplot,color='darkred', linestyle='--', label='Salida obtenida')
plt.plot(Xplot, Refplot,color='darkgreen',linestyle='-.', label='Salida deseada')

plt.xlabel("X", size = 16)
plt.ylabel("Y", size = 16)

plt.title("Prueba de entrenamiento con c = 20", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()

plt.grid(True)
plt.show()