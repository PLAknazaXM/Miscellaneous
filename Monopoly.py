import numpy as np

Money = 0
Check = False
Yes = ('y','Y','yes','t','true','on','1')

def space():
    print('')
    return

print('''Welcome to Monopoly!  Be ready for either have fun or lose friends!''')

while Check == False:
    Start = input('''Please enter the starting cash for the game.
For traditional Monopoly, you start with $1500.

Starting currency: ''')
    
    try:
        Start = int(Start)
    except:
        print('Invalid Entry!')
        continue
    
    space()
    print('Currency Entered: $', Start)
    check = input('Confirm? (Y/N)')
    space()
    if check in Yes:
        Check = True
    else:
        print('Accidental value entered!')
print('Ready to start!')

Money = Start
Actions = ('1','2','3')
Bankrupt = False
Win = False


while Bankrupt == False:

    pause = input('Press enter to continue:')
    space()

    print('''Something is about to happen!
Starting balance: $''', Money)
    
    action = input('''What are you doing?

1: Paying
2: Being paid
3: Nothing, but wait...
                   
Action: ''')
    
    if action not in Actions:
        print('''Non-valid action entry entered!''')
        continue

    Check = False
    space()
    if action == '1':
        while Check == False:
            cost = input('How much are you paying?: ')
            try:
                cost = int(cost)
            except:
                print('Invalid Entry!')
                continue
            print('Cost Entered: $', cost)
            check = input('Confirm? (Y/N)')
            if check in Yes:
                Check = True
            else:
                print('Accidental value entered!')

            if Money - cost < 0:
                print('Not enough money!')
                b = input('Are you going bankrupt? [Y/N] : ')
                if b in Yes:
                    Bankrupt = True
                else:
                    print('Trade, mortgage, whatever you must do!  Then come back!')
                    continue
            Money = Money - cost
        space()
        print('Remaining balance: $', Money)

    elif action == '2':
        while Check == False:
            payment = input('How much are you being paid?: ')
            try:
                payment = int(payment)
            except:
                print('Invalid Entry!')
                continue
            print('Income Entered: $', payment)
            check = input('Confirm? (Y/N)')

            if check in Yes:
                Check = True
            else:
                print('Accidental value entered!')
        Money = Money + payment
        space()
        print('New balance: $', Money)

    else:
        print('Nothing happened, for now...')
        win = input('Wait, did you win? [Y/N] : ')
        if win in Yes:
            Bankrupt = True
            Win = True

space()
if Win == True:
    print('CONGRATS! You won the game!')
else:
    print('Better luck next time...')

space()
pause = input('Press enter to close the program.')
