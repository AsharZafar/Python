def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)


print(fun(25))