```py
import numpy as np
import matplotlib.pyplot as plt

def parabola_function(x):
    return 2 * (x + 5)**5

x_values = np.linspace(-10, 10, 100)

y_values = parabola_function(x_values)

plt.plot(x_values, y_values, label='y = 2(x+5)^5')
plt.title('Graph of the Parabola')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
``` 
