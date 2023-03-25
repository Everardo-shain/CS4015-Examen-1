import numpy as np
import math
import pandas as pd
import sys

m = int(input('Introduzca la dimensión de la matriz A (mayor o igual a 3): '))
if m< 3:
    sys.exit('Dimensión debe ser mayor o igual a 3')
A=[]
elementos = 0
x=2
while elementos < m*m:
    primo=1;
    for i in range(2,x):
        if (x%i) == 0:
            primo=0
    if primo == 1:
        A.append(x)
        elementos += 1  
    x += 1 
A = np.asarray(A)
A = A.reshape((m, m))
df=pd.DataFrame(A)
print("\n La matriz A de números primos consecutivos es: \n")
print(df.to_string(index=False,header=False))
suma=0
for i in range(m):
    for j in range(i, m):
        suma=suma+A[i,j]
    
print("\n La suma de los elementos en la matriz diagonal superior es: \n")
print(suma)