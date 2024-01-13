#Condition loop

import random
systemnumber = random.randint(1, 20)
count = 1

while count < 4:
    print('Take a guess:')
    myguess = int(input())
    if myguess < systemnumber:
        print('Your guess is small')
    elif myguess > systemnumber:
        print('Your guess is big')
    elif myguess == systemnumber:
        break
    count = count + 1 

if myguess == systemnumber:
        print('you got it!')
        print('Congratulations!!')
elif myguess != systemnumber:
        systemnumber = str(systemnumber)
        print('Sorry you lost! the number I have is: ' + systemnumber)