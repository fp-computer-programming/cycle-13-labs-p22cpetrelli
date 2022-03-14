#author CJP 03/14/2022
#define function
def factorial(number):
    total = 1
    x = 1
# conditional used to see if number is greater than zero and can therefore be multiplied
    if number >= 1:
        for x in range(1, number + 1):
            total *= x
            x += 1
        return total
    elif number < 1:
        print("Must be greater than zero.")
        
print(factorial(8))