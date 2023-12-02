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
<img width="673" alt="Screenshot 2023-11-18 at 12 30 34" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/eed49e12-fa12-41e1-8a3f-1bc162448eca">
<img width="1470" alt="Screenshot 2023-12-02 at 11 39 30" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/405b9712-8b3b-4a11-b350-bc20e5e09396">

B. 
