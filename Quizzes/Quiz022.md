Part A 
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
<img width="445" alt="Screenshot 2023-11-22 at 12 58 53" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/ea57bcd5-ebbf-4dfc-903b-54c0e251fef8">
