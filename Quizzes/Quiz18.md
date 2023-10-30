```py
def get_truth():
    a = 0
    b = 0
    c = 0
    out = ''
    out1 = 'A|B|C'
    for x in range(8):
        out += f'{int(a)}|{int(b)}|{int(c)}\n'
        if x%2== 0:
            b = not b
        if x%4== 0:
            a = not a
        c = not c

    return f'{out1}\n{out}'

test = get_truth()
print(test)
```
<img width="161" alt="Screenshot 2023-10-30 at 13 08 58" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/bae2b4d8-b828-4e35-a7f2-90989157ebe6">
![Uploading IMG_9F22401AB112-1.jpeg…]()
