Part A
```py 

def produce(n,m,s):
    random.seed(1234)
    y= [ ]
    x = [ ]
    string  = "|  x  |  y(x)  |\n"
    for i in range (n):
        x_rnd = random.randint(1,100)
        y_rnd = x_rnd**(-0.5*((m/s)**2))
        y.append(y_rnd)
        x.append(x_rnd)
        string += f'|  {x_rnd}  |  {y_rnd}  |\n'
    return string
sample = produce(n=5,m=3,s=2)
print(sample)
```
<img width="306" alt="Screenshot 2023-10-31 at 10 08 11" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/d3590451-63c6-4600-94ea-39925ef7282b">
<img width="670" alt="Screenshot 2023-11-18 at 11 58 22" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/c813ca4f-e569-42d0-ab18-6f80515b3ebb">

Part B 
![IMG_0492](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/78a733af-4026-4944-9c41-010340683ef6)
