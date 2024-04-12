import numpy as np
import matplotlib.pyplot as plt
import time

from operation import vectorized, nonvectorized
matrix = np.loadtxt('testcases/in/1.csv', delimiter = ',')
result = vectorized(matrix = matrix)
print(result)

matrix = np.loadtxt('testcases/in/2.csv', delimiter = ',')
result = vectorized(matrix = matrix)
print(result)

with open('data/nonvectorized.txt') as f:
	lines = f.readlines()
	nonvec = []
	for line in lines:
		nonvec.append(float(line.strip()))

with open('data/vectorized.txt') as f:
	lines = f.readlines()
	vec = []
	for line in lines:
		vec.append(float(line.strip()))

plt.figure(figsize=(10,6))

x = np.linspace(0, 100, 100)
y1 = x/(10**6)
y2 = x**2/(10**6)
y3 = x**3/(10**6)
plt.plot(x, nonvec, label='Non-vectorized')
plt.plot(x, vec, label='Vectorized')
plt.plot(x, y1, label='N', linestyle='--')
plt.plot(x, y2, label="N^2", linestyle='--')
plt.plot(x, y3, label='N^3', linestyle='--')

plt.legend()
plt.savefig('plot1.png')
plt.show()

