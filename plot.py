import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y = np.sin(x)

plt.plot(x, y)
plt.title("sin(x)")
plt.grid(True)
plt.show()