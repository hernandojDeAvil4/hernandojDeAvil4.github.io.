import slycot
import control
from control.matlab import *
import numpy as np

#Representación del espacio de estados con Python.

#Numerador de la función de transferencia
num1 =np.array([1,0])
#Denominador de la función de transferencia 
den1 = np.array([1,14,56,160])

#Combierte los coeficientes en una función de transferencia
Tf=control.tf(num1,den1)

#La función control.ss me permite realizar la representación  de espacio de estados del sistema
sol=control.ss(Tf)

G=control.matlab.ss2tf(sol.A, sol.B, sol.C, sol.D)

print('----------------------------------------------------------------------')
print('**********La solución para la representación de espacio de estado es:***********')
print(sol)
print('----------------------------------------------------------------------')