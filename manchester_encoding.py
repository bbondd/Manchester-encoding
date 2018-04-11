import numpy as np
import matplotlib.pyplot as plt

input_binary = [0]
clock = [1]
for i in input():
    input_binary.append(int(i))
    input_binary.append(int(i))
    clock.append(0)
    clock.append(1)

x = np.linspace(0, (len(clock) - 1) / 2, len(clock))
y = np.array(input_binary) ^ np.array(clock)

print(x)
print(y)
plt.step(x, y)
plt.show()
