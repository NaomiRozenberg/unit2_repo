Part A 
```py 
import matplotlib.pyplot as plt
import random

def produce(n,m,s):
    random.seed(1234)
    y= []
    x = []
    for i in range (n):
        x_rnd = random.randint(1,100)
        y_rnd = x_rnd**(-0.5*((m/s)**2))
        y.append(y_rnd)
        x.append(x_rnd)
    return x,y
a,b=produce(n=5,m=3,s=2)
plt.plot(a,b)
plt.show()
```
<img width="423" alt="Screenshot 2023-11-01 at 15 01 52" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/a485bf79-72dc-4a20-a3a1-fccd8977dda8">
<img width="760" alt="Screenshot 2023-11-18 at 12 03 42" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/d83b86e0-7869-42ef-98e1-0892e57457c5">
Part B 
A(A ⊕ B)  
![IMG_0493](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/d430b7aa-5eee-4283-83b7-4d5abd0b0a7b)
