import numpy as np

def association_function(x, c):
  return 0.5 + np.tanh(c*x)/2

def scale_inputs(X, Ranges):
  #Escalar entrada

  XNorm = np.zeros(len(X))

  for i_x_norm in range(len(XNorm)):
    XNorm[i_x_norm] = X[i_x_norm]/Ranges[i_x_norm]

  return XNorm