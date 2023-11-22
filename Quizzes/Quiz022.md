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
<img width="549" alt="Screenshot 2023-11-22 at 13 05 26" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/40b6f648-3413-4158-87ae-e49fb5cfe841">
Part B
![IMG_9D4B85A795B7-1](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/0d9179f7-deea-4162-9dd4-3cc2d4147909)
