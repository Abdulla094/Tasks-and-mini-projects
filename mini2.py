# Geuss the number

import random

number = random.randint(0,10)

for i in range(0,3):
    guess = int(input('guess the number: '))
    if guess == number:
        print(f'Yoy won!, you guessed the number -- {number} -- Correctly!')
        break
    else:
        print('Wrong guess')
        if i == 2:
            print(f'You lost the number was -- {number}')