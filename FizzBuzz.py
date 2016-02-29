# -*- coding: utf-8 -*-


x=raw_input("Vnesi številko med 1 in 100:")
x=int(x)

for x in range(1, x+1):

    if x%5==0 and x%3==0:
        print("FizzBuzz")

    elif x%3==0:
        print("Fizz")

    elif (x%5) ==0:
        print("Buzz")

    else:
        print(str(x))
