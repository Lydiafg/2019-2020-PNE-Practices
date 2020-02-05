# Exercise 2. Session 2 fibonacci

def fiboN(n):
    count = 0
    n1 = 0
    n2 = 1
    for i in range(0, n+1):
        if i == 0:
            count = 0
        elif i == 1:
            count = 1
        else:
            count = n1 + n2
            n1 = n2
            n2 = count
    return count

print("5th Fibonacci term: ", fiboN(5))
print("5th Fibonacci term: ", fiboN(10))
print("5th Fibonacci term: ", fiboN(15))