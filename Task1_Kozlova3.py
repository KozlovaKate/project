import matplotlib.pyplot as plt
import numpy as np
import math
import os

A = 1.25313

#Заданная функция
def f(x):
    return (0.5+(((np.cos (np.sin( abs((x**2)-(A**2)))))**2)-0.5)
      /((1+0.001*((x**2)+(A**2)))**2))

for x in list(range(-100, 101, 1)):
    y=(0.5+(((np.cos (np.sin( abs((x**2)-(A**2)))))**2)-0.5)
      /((1+0.001*((x**2)+(A**2)))**2))
    print(x,y)

x= np.linspace(-100,100,300)
y=f(x)

if not os.path.exists('results'):
    os.mkdir('results')
with open("results/task_01_307b_Kozlova_10.txt",'w') as txt:
    i = 0 
    for _x in x:
        txt.write(str(_x)+' '+str(y[i])+'\n')
        i+=1
 
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
