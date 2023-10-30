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
