num = 2021
i = 0

while num > 0:
    if num%3 == 0:
        i += 1
        num -= 7
    else:
        num -= 7

print(i)
