import numpy as np

class ReferenceModel:

    PastY = np.zeros(2)
    PastU = np.zeros(2)

    def __init__(self, T, K, frecuencia, amortiguamiento):
        self.T = T
        self.K = K
        self.frecuencia = frecuencia
        self.amortiguamiento = amortiguamiento

        self.calculate_parameters()
    
    def calculate_parameters(self):
        self.A = self.amortiguamiento

        if(self.A >= 1):
            self.B = np.sqrt(np.power(self.A, 2) - 1)
        else:
            self.B = (1j)*np.sqrt(1 - np.power(self.A, 2))
        self.C = np.exp((-self.frecuencia*self.A + self.frecuencia*self.B)*self.T)
        self.D = np.exp((-self.frecuencia*self.A - self.frecuencia*self.B)*self.T)

        self.coef_U1 = (self.K/(2*self.B))*(-self.A*self.C+self.A*self.D-self.B*self.C-self.B*self.D+2*self.B)
        self.coef_U2 = (self.K/(2*self.B))*(self.A*self.C-self.A*self.D+2*self.B*self.C*self.D-self.B*self.C-self.B*self.D)
        self.coef_Y1 = self.C+self.D
        self.coef_Y2 = -self.C*self.D
    
    def get_output(self, u_signal):
        Y = self.coef_U2*self.PastU[1] + self.coef_U1*self.PastU[0] - self.coef_Y2*self.PastY[1] + self.coef_Y1*self.PastY[0]
        
        self.PastY[1] = self.PastY[0]
        self.PastY[0] = Y

        self.PastU[1] = self.PastU[0]
        self.PastU[0] = u_signal
        
        return float(Y)
    
    def get_output_from_last_values(self, u1, u2, y1, y2):
        Y = self.coef_U2*u2 + self.coef_U1*u1 - self.coef_Y2*y2 + self.coef_Y1*y1
        
        return float(Y)