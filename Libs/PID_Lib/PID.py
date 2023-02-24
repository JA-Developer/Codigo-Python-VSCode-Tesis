import numpy as np

class PID_Controller:
    Kp = 0
    Ki = 0
    Kd = 0

    e0 = 0
    e1 = 0
    e2 = 0
    e3 = 0

    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    def PID_Delta_U(self, Error):
        self.e3 = self.e2
        self.e2 = self.e1
        self.e1 = self.e0
        self.e0 = Error
            
        Delta_U = np.abs(self.Kp)*(self.e0 - self.e1) + np.abs(self.Ki)*self.e0 + np.abs(self.Kd)*(self.e0 - 2*self.e1 + self.e2)
        return Delta_U
    
    def D_U_Kp(self):
        return np.sign(self.Kp)*(self.e0 - self.e1)
    
    def D_U_Ki(self):
        return np.sign(self.Ki)*self.e0

    def D_U_Kd(self):
        return np.sign(self.Kd)*(self.e0 - 2*self.e1 + self.e2)