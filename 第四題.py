x1 = 0
x2 = 100
n = 10

from random import randint
target = (randint(1, 100))

while n > 0 :
    
    num = int(input("plz enter your number:"))
    if num == target :
        print("you are correct!")
        break
    elif num > target :
        print("too big!")
    else :
        print("too small!")
    n = n -1 