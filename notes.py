f = 0
seen = {}
last_f = 0
while 1:
    d = f | 65536
    f = 733884
    b = d & 255
    f += b
    f &= 16777215
    f *= 65899
    f &= 16777215
    while d >= 256:
        d //= 256
        b = d & 255
        f += b
        f &= 16777215
        f *= 65899
        f &= 16777215

    if f in seen:
        print(last_f)
        break
    seen[f] = 1
    last_f = f
