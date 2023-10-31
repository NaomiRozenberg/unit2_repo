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
<img width="161" alt="Screenshot 2023-10-30 at 15 57 58" src="https://github.com/NaomiRozenberg/unit2_repo/assets/142605919/afba8dfb-3504-4a48-a7a4-a171b85eb65a">
![Uploading IMG_AEDB90F32D4C-1.jpeg…]()
Part 2 ![Uploading IMG_65A4F27158ED-1.jpeg…]()
