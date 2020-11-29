import numpy as np
import random


def check_dif(a_f, k_f):
    flag = False
    if int(a_f) - int(k_f) == 0:
        flag = True
    return flag


points = 3
a = random.randrange(1, 10, 1)
if a % 2 == 0:
    print("It's a multiple of 2")
else:
    print("It's an odd number")
k = input("Type your prediction: ")

if check_dif(a, k):
    print("You WON")
    print("Points: " + str(points))
else:
    print("Wrong number : Here's one more clue-")
    points -= 1
    if a > 5:
        print("The number is greater than 5")
    else:
        print("The number is less than or equal to 5")
    k = input("Type your prediction: ")

    if check_dif(a, k):
        print("You WON")
        print("Points: " + str(points))
    else:
        print("Wrong number : Here's one more clue-")
        points -= 1
        if np.cbrt(a) == 2:
            print("The cube root of the number is an integer")
        elif a == 2 or a == 3 or a == 5 or a == 7:
            print("It's a prime number")
        elif a == 6 or a == 9:
            print("It's a multiple of 3")
        elif a == 1:
            print("It's factor of all numbers")
        else:
            print("Either it's square root is an integer or it's second multiple of 5")
        k = input("Type your prediction: ")
        if check_dif(a, k):
            print("You WON")
            print("Points: " + str(points))
        else:
            points -= 1
            print("Wrong Number. Bye bye ,you failed.")
            print("Points: " + str(points))
