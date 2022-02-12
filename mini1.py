# dice roll stimulator

import random as r

while True:
    print('''1.Roll the dice
    2.Quit''')
    user = int(input("What would you like to do : "))
    if user == 1:
        
        print("ROLLING THE DIES.... YOU GOT : ",r.randint(1,6))
    else:
        break
