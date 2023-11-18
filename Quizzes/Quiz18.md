Part A 
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
<img width="731" alt="Screenshot 2023-11-18 at 11 43 02" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/e388f2ec-4df5-4ef2-9a75-ee7b0128ba56">
part B 
![IMG_0487](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/251d24c0-782e-406f-85ac-530f25fe1b14)

![IMG_0488](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/16f2e3d6-0179-474d-a621-ab435c3fd1d9)

![IMG_0487](https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/f63ea031-eabc-42b7-ae39-d185c5f0eba0)
