key = 10551354
half = key//2
sum = 0
for i in range(1,half+1):
    if not key % i and i < key//i:
        print(i, key//i)
        input()
        sum += i
        sum += key//i
print(sum)
