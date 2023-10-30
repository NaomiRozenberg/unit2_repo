```py
def get_l3tt3r(msg):
    vowel_mapping = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'u': '2'}
    result = ''
    for char in msg:
        if char in vowel_mapping:
            result += vowel_mapping[char]
        else:
            result += char
    return result

msg = "hello world"
result = get_l3tt3r(msg)
print(result)
```
