from numpy import *
from matplotlib import pyplot as plt
x_vals = []
y_vals = []
for x in range(0,6283):
    x_vals.append(16*pow(sin(x/1000),3))

for y in range(0,6283):
    y=y/1000
    y_vals.append((13*cos(y))-(5*cos(2*y))-(2*cos(3*y))-(cos(4*y)))

data = []
for i in range(0,len(x_vals)):
    data.append(x_vals[i])
    data.append(y_vals[i])
print(data)
plt.plot(x_vals,y_vals)
plt.show()