import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.1, 2 * np.pi, 100)
y_1 = x
y_2 = np.square(x)
y_3 = np.log(x)
y_4 = np.sin(x)
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)
plt.plot(x, y_4)
plt.show()
