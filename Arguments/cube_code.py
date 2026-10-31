#define function to calculate cube
def cube(number):
    return number*number*number

#define af unction which will execute cube functionif the user entered number is divisible by 3
def by_three(number):
    if number %3 ==0:
        return cube(number)
    return False

#display result
print(by_three(9))
print(by_three(4))