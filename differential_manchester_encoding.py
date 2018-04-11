import numpy as np
import matplotlib.pyplot as plt

output_signal = [1]

for i in input():
    if int(i) == 0:
        output_signal.append(not output_signal[-1])
        output_signal.append(not output_signal[-1])

    else:
        output_signal.append(output_signal[-1])
        output_signal.append(not output_signal[-1])

x = np.linspace(0, (len(output_signal) - 1) / 2, len(output_signal))
y = np.array(output_signal)

plt.step(x, y)
plt.show()
