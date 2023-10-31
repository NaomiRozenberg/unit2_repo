```py 
def base_converter(num, base):
    out = ''
    while num >1:
        d=num%base
        num = num // base
        out += f'{str(d)}'
    out +=  str(num)
    return out[::-1]
test = base_converter(num=139,base=3)
print(test)
```
<img width="306" alt="Screenshot 2023-10-31 at 10 09 51" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/230143c9-d3c7-4006-8731-2c96e24c0dcc">
