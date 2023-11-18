```py def get_truth():
    out = 'A|B|C | AB+(not B)+not(CB)\n'

    for a in range(2):
        for b in range(2):
            for c in range(2):
                result = a and b or (not b) or (not (c and b))
                out += f'{a}|{b}|{c} | {int(result)}\n'

    return out

test = get_truth()
print(test)
```
<img width="405" alt="Screenshot 2023-11-05 at 12 31 47" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/f0f79aff-495b-4b95-bb7f-c98cfc7a26b5">
<img width="842" alt="Screenshot 2023-11-18 at 11 52 20" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/f1f174cb-70d4-42e0-aed1-5f7160838ccd">
