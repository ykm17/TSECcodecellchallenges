import decimal

n = [5, 500, 5000000000]
x = 0
ans = 1

def getSum(num):
    sum = 0
    while num > 0:
        sum += int(num % 10)
        num = int(num / 10)

    return sum

for i in range(0, 3):
    x = n[i] * (n[i] + 1) / 2
    x = x ** 2
    d = decimal.Decimal(x)
    d = format(d)
    d = int(d)
    d = getSum(d)
    isSingleDigit = (0 < d < 10)
    while not isSingleDigit:
        d = getSum(d)
        isSingleDigit = (0 < d < 10)

    ans = ans * d
print(ans)
