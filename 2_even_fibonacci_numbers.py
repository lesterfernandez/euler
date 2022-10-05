first, second = 1, 2
sum = 0
while second < 4000000:
    first, second = second, first + second
    if first % 2 == 0:
        sum += first

print(sum)

