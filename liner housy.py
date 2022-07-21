a = []

print(a)

status = True
count = 1

while status:
    num = int(input('enter number:'))
    if  count <= 12:
        if num not in a:
            a.append(num)
            count += 1
        else:
            pass
    else:
        status = False
print(a)
