

def fiboN(n):
    count = 0
    n1 = 0
    n2 = 1
    sum_ = 0
    for i in range(0, n+1):
        if i == 0:
            count = 0
        elif i == 1:
            sum_ = sum_ + 1
        else:
            count = n1 + n2
            n1 = n2
            n2 = count
            sum_ = sum_ + count
    return sum_

print("Sum of 1-5th fibonacci terms: ", fiboN(5))
print("Sum of 1-5th fibonacci terms: ", fiboN(10))
