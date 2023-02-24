import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from Test.Ref_Model_Lib import Reference_Model

Ref_Model = Reference_Model.ReferenceModel(0.1, 1, 1000,1000)

print(str(Ref_Model.coef_U2) + ", " + str(Ref_Model.coef_U1) + ", " + str(Ref_Model.coef_Y2) + ", " + str(Ref_Model.coef_Y1))