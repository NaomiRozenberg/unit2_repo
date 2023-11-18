Part A. 
```py
import numpy as np
import matplotlib.pyplot as plt
data = []
with open("data3.csv ",'r') as f:
    titles = f.readline()
    values = f.readlines()
x = []
t = 0
for v in values:
    s1,s2,s3 =v.strip().split(',')
    data.append([int(s1),int(s2),int(s3)])
    x.append(t)
    t += 1
mean = []
std = []
min = []
max = []
for d in data:
    mean.append(np.mean(d))
    std.append(np.std(d))
    min.append(np.min(d))
    max.append(np.max(d))
plt.errorbar(x, mean, std, fmt='o', color='#023047')
plt.fill_between(x, max, min, alpha=0.5, linewidth=0)
plt.xlabel("Time")
plt.ylabel("Temp")
plt.show()
```
<img width="506" alt="Screenshot 2023-11-17 at 21 27 12" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/2f462bef-b0d1-4203-bf08-0485dd662d1d">
<img width="953" alt="Screenshot 2023-11-18 at 12 19 34" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/413ec7b0-5d4b-4415-a036-b8d72f6bde71">
