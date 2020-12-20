import numpy as np
import matplotlib.pyplot as plt
import os
n = 10000 
A = 1.25313
x = np.linspace(-100, 100, 10000) # создание "отрезка"
fx = ((0.5+((np.cos(np.sin(((x)**2)-((A)**2))))**2)-0.5)
      /((1+0.001*(((x)**2)+((A)**2)))**2))
# создание файл
try:
 os.mkdir('results')
except OSError:
 pass
complete_file = os.path.join('results', 'task_01_307B_Kozlova_10.txt')
f = open(complete_file, 'w')
# текстовик с таблицей
f.write('   x    f(x)\n')
for i in range(n):
 f.write(str("%.4f" % x[i])+' '+str("%.4f" % fx[i])+"\n")
f.close()
# построение графика
fig, ax = plt.subplots()
ax.plot(x, fx)
ax.set_xlim(0, 5);
ax.set_ylim(0, 1);
ax.grid(linewidth = 2)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, fx, color = 'black')
plt.show()