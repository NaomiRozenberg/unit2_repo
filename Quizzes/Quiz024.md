Part A
```py

import matplotlib.pyplot as plt
import numpy as np

h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0, 53.0, 53.0, 54.0, 53.0, 53.0, 52.0, 52.0, 51.0, 51.0, 51.0, 50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 49.0, 49.0, 48.0, 48.0, 48.0, 49.0]
time = []
t = 0
for i in range(0, len(h)):
    time.append(t)
    t+=10

plt.scatter(time, h)
plt.xlabel("Time (min)")
plt.ylabel("Humidity%")
plt.show()
```
<img width="506" alt="Screenshot 2023-11-17 at 21 28 59" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/c48b8503-6f85-4017-93d3-27074d8a46fa">
<img width="418" alt="Screenshot 2023-11-22 at 13 11 35" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/caf02b01-977f-44e8-8804-1be4454a84f5">

Part B 
![IMG_EF6FD48B0EA0-1](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/c86f7f8b-156d-4611-aa7a-5f73279eb4ba)
