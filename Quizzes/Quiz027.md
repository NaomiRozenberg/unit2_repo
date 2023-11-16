```py
def count_letters(my_dict, msg):
    for x in range (len(msg)):
        if msg[x] in my_dict:
            my_dict[msg[x]] += 1
    return my_dict

case1 = count_letters({'w': 0, 'l':0, 'c':0}, "hello world")
print(case1)
```
