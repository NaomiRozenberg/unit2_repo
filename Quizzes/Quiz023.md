Part A
```py
import numpy as np
import matplotlib.pyplot as plt
def absolute_value_function(x):
    return np.abs(x)
x_values = np.linspace(-10, 10, 100)
y_values = absolute_value_function(x_values)
plt.plot(x_values, y_values, label='y = |x|')  
plt.title('Graph of the Absolute Value Function')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
```
<img width="360" alt="Screenshot 2023-11-22 at 12 53 04" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/1580dedc-4edc-40d2-9dda-73c3e87b647e">

Part B 
