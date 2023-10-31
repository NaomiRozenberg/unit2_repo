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
