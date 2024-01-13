# This program is for more examples on Python
# I am writing my program here

import random
systemnumber = random.randint(1, 10)
myguess = int(input())

if myguess < systemnumber:
    print('Your guess is small')
elif myguess > systemnumber:
    print('Your guess is big')
elif myguess == systemnumber:
    print('you got it!')
    print('Congratulations!!')