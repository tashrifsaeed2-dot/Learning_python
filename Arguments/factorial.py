def factorial(x):
    '''this is recursive function to find the factorial of the integer'''
    if x<=1:
        return 1
    return x*factorial(x-1)

#display result'
print(factorial.__doc__)
print("the factorial of 0:",factorial(0))
print("the factorial of 1:",factorial(1))
print("the factorial of 2:",factorial(2))
print("the factorial of 5:",factorial(5))
print("the factorial of 10:",factorial(10))