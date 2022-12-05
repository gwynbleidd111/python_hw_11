#Задача №1______________________________________________________________

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)
y = 5*x**2 + 10*x-30


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title('График функции 𝑓(𝑥) = 5𝑥^2 + 10𝑥 − 30')
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,y, 'g')
plt.show()
