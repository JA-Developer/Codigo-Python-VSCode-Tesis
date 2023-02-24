import numpy as np
import Libs.AHN_Lib.Utils as Utils

class AHN_Compound:

    #Inicializar valores de compuesto

    n_inputs = 0
    n_molecules = 0
    atoms_values = []
    centers_of_molecules = []
    c = 20

    input_ranges = []

    #Inicializar valores de ADAM Optimizer

    optimizer_params = []

    def __init__(self, NInputs, NMolecules, InputRanges):

        #Inicializar valores de compuesto

        self.atoms_values = []
        self.centers_of_molecules = []

        #Inicializar valores de ADAM Optimizer

        self.optimizer_params = []

        self.b0 = 0.333
        self.b1 = 0.999

        #Guardar tamaños
        self.n_inputs = NInputs
        self.n_molecules = NMolecules
        
        #Guardar rangos
        self.input_ranges = InputRanges

        #Agregar átomos
        if(NMolecules == 1):
            
            self.atoms_values.append(np.zeros((self.n_inputs, 5)))
            self.optimizer_params.append(np.zeros((self.n_inputs, 5, 3)))

        elif(NMolecules >= 2):
            
            self.atoms_values.append(np.zeros((self.n_inputs, 4)))
            self.optimizer_params.append(np.zeros((self.n_inputs, 4, 3)))

            for mol in range(NMolecules - 2):
            
                self.atoms_values.append(np.zeros((self.n_inputs, 3)))
                self.optimizer_params.append(np.zeros((self.n_inputs, 3, 3)))
            
            self.atoms_values.append(np.zeros((self.n_inputs, 4)))
            self.optimizer_params.append(np.zeros((self.n_inputs, 4, 3)))

        #Agregar centros de moléculas
        self.centers_of_molecules = 2*np.random.rand(self.n_molecules, self.n_inputs)-1
    
    def evaluate(self, X):

        #Escalar entrada

        XNorm = Utils.scale_inputs(X, self.input_ranges)

        #Calcular molécula activa de acuerdo a los centros de molécula
        
        L = np.sqrt(np.sum(np.power(self.centers_of_molecules - np.ones((self.n_molecules, self.n_inputs))*XNorm, 2), axis=1))
        Dm = np.ones(self.n_molecules)

        for i_dm in range(self.n_molecules):
            for j_dm in range(self.n_molecules):
                if(i_dm != j_dm):
                    Dm[i_dm] *= Utils.association_function(L[j_dm] - L[i_dm], self.c)

        #Calcular respuesta de la red

        output = 0

        for i_molecules in range(self.n_molecules):

            #Salida de la molécula

            output_molecule = 0
            
            for i_inputs in range(self.n_inputs):
                output_molecule += np.polynomial.polynomial.polyval(XNorm[i_inputs], self.atoms_values[i_molecules][i_inputs])
            
            output += output_molecule*Dm[i_molecules]

        return output
    
    def train_step_with_derivate(self, X, derivate, alpha, epsilon, tolerance):

        #Escalar entrada

        XNorm = Utils.scale_inputs(X, self.input_ranges)

        Noise = np.random.rand(len(X))*tolerance - (tolerance/2)

        XNorm_With_Noise = XNorm + Noise

        #Calcular molécula activa de acuerdo a los centros de molécula
        
        L = np.sqrt(np.sum(np.power(self.centers_of_molecules - np.ones((self.n_molecules, self.n_inputs))*XNorm_With_Noise, 2), axis=1))
        Dm = np.ones(self.n_molecules)

        for i_dm in range(self.n_molecules):
            for j_dm in range(self.n_molecules):
                if(i_dm != j_dm):
                    Dm[i_dm] *= Utils.association_function(L[j_dm] - L[i_dm], self.c)
        
        #Precalcular valores potenciados

        XtoN = np.vander(XNorm_With_Noise, 5, True)

        #Entrenar
        
        for i_molecules in range(self.n_molecules):

            for i_inputs in range(self.n_inputs):

                N_atoms = len(self.atoms_values[i_molecules][i_inputs])

                for i_atom in range(N_atoms):

                    de_dh = derivate*XtoN[i_inputs][i_atom]*Dm[i_molecules]

                    #ADAM

                    self.optimizer_params[i_molecules][i_inputs][i_atom][0] = self.b0*self.optimizer_params[i_molecules][i_inputs][i_atom][0] + (1 - self.b0)*de_dh
                    self.optimizer_params[i_molecules][i_inputs][i_atom][1] = self.b1*self.optimizer_params[i_molecules][i_inputs][i_atom][1] + (1 - self.b1)*np.power(de_dh, 2)

                    if(self.optimizer_params[i_molecules][i_inputs][i_atom][1] > self.optimizer_params[i_molecules][i_inputs][i_atom][2]):
                        self.optimizer_params[i_molecules][i_inputs][i_atom][2] = self.optimizer_params[i_molecules][i_inputs][i_atom][1]

                    self.atoms_values[i_molecules][i_inputs][i_atom] -= alpha*self.optimizer_params[i_molecules][i_inputs][i_atom][0]/(np.sqrt(self.optimizer_params[i_molecules][i_inputs][i_atom][2]) + epsilon)

    def train_step_with_desired_output(self, X, real_output, desired_output, alpha, epsilon, tolerance):

        #Calcular error

        error = real_output - desired_output
        
        #Escalar entrada

        XNorm = Utils.scale_inputs(X, self.input_ranges)

        Noise = np.random.rand(len(X))*tolerance - (tolerance/2)

        XNorm_With_Noise = XNorm + Noise

        #Calcular molécula activa de acuerdo a los centros de molécula
        
        L = np.sqrt(np.sum(np.power(self.centers_of_molecules - np.ones((self.n_molecules, self.n_inputs))*XNorm_With_Noise, 2), axis=1))
        Dm = np.ones(self.n_molecules)

        for i_dm in range(self.n_molecules):
            for j_dm in range(self.n_molecules):
                if(i_dm != j_dm):
                    Dm[i_dm] *= Utils.association_function(L[j_dm] - L[i_dm], self.c)
        
        #Precalcular valores potenciados

        XtoN = np.vander(XNorm_With_Noise, 5, True)
        
        #Entrenar
        
        for i_molecules in range(self.n_molecules):
            
            for i_inputs in range(self.n_inputs):
                
                N_atoms = len(self.atoms_values[i_molecules][i_inputs])

                for i_atom in range(N_atoms):
                    
                    de_dh = 2*error*XtoN[i_inputs][i_atom]*Dm[i_molecules]

                    #ADAM

                    self.optimizer_params[i_molecules][i_inputs][i_atom][0] = self.b0*self.optimizer_params[i_molecules][i_inputs][i_atom][0] + (1 - self.b0)*de_dh
                    self.optimizer_params[i_molecules][i_inputs][i_atom][1] = self.b1*self.optimizer_params[i_molecules][i_inputs][i_atom][1] + (1 - self.b1)*np.power(de_dh, 2)

                    if(self.optimizer_params[i_molecules][i_inputs][i_atom][1] > self.optimizer_params[i_molecules][i_inputs][i_atom][2]):
                        self.optimizer_params[i_molecules][i_inputs][i_atom][2] = self.optimizer_params[i_molecules][i_inputs][i_atom][1]

                    self.atoms_values[i_molecules][i_inputs][i_atom] -= alpha*self.optimizer_params[i_molecules][i_inputs][i_atom][0]/(np.sqrt(self.optimizer_params[i_molecules][i_inputs][i_atom][2]) + epsilon)