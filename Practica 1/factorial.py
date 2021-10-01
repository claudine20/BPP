def factorial(n):
    assert(n >=0)

    fct= 1
    for i in range(1,n+1):
        fct *=i
    print(f' (n)! = {fct}')


factorial(5)
factorial(3)
factorial(1)
factorial(0)
#factorial(-1)
