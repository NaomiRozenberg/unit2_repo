A. 
```py
def count_letters(my_dict, msg):
    for x in range (len(msg)):
        if msg[x] in my_dict:
            my_dict[msg[x]] += 1
    return my_dict

case1 = count_letters({'w': 0, 'l':0, 'c':0}, "hello world")
print(case1)
```
<img width="289" alt="Screenshot 2023-11-16 at 11 08 00" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/ee954d4e-bb87-46e8-a0ac-e30214569410">

B. 
