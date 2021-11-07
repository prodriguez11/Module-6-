#Problem 4
#Import math library 
#Initialize denominator
#Initialize sum
#even index elements are positive
#odd index elements are negative 
#denominator is odd
#print the valuye of pi

import math

k = 1
s = 0
for i in range(1000000):
    if i % 2 ==0:
        s += 4/k
    else:
        s -= 4/k
    k += 2
print("Value of estimated pi:" , s)
print("Value of pi from math module:", math.pi)

#Problem 5
rad = float(input("Enter an radians:"))
degrees = rad * (180/math.pi)
print("degrees of {} radians using calculation:{}".format(rad,degrees))
print("degrees of {} radians using inbuilt function:{}".format(rad, math.degrees(rad)))

#Problem 6
n = int(input("Enter an integer:"))
result = 1
for i in range(1, n+1):
    result = result * i
print("factorial of {} using for loop {}".format(n, result))
print("factorial of {} using inbuilt function:{}".format(n, math.factorial(n)))
