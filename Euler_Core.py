import numpy as np
import matplotlib.pyplot as plt

def f(x,y,input):
	formula = input
	result = eval(formula)
	return result

x0 = 0
y0 = 1
xf = 10
n = 101
dx = (xf-x0)/(n-1)

x = np.linspace(x0, xf, n)

y = np.zeros([n])

y[0] = y0

for i in range(1, n):
	y[i] = dx*f(x[i-1], y[i-1]) + y[i-1]

plt.plot(x , y , 'o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Approximate Solution with Forward Euler’s Method")
plt.show()