#ask for bet
#random int gen
#if 3 = same, x 5

import random as rnd



def main():
    again = 'y'
    bank = 5
    while again == 'y' or again == 'Y':
        
        if bank > 0 and (again == 'y' or again == 'Y'):
            print('Your bank holds', bank, 'cents')
            bet = input('How much would you like to bet? ')
            if int(bet) <= int(bank):
                bank = spin(bet, bank)
                print()
                again = input('Would you like to play again? y = yes ')
            else:
                print('Sorry, that value is either invalid or you' +
                          ' do not have enough funds in your bank.')
        else:
            print('Unfortunately, you are out of funds')
            reset = input('Would you like to refuel your funds?'
                          + ' y = yes, q to quit ')
            if reset == 'y' or reset == 'Y':
                bank = 5
                again = 'y'
            else:
                break
            
    
            
        


def spin(x, z):
    slots = []
    x = int(x)
    for i in range(3):
        slots.append(rnd.randint(1,6))

    if slots[0] == slots[1] == slots[2]:
        print("Congratulations! You've matched 3 numbers and won", x*5,"cents.")
        z += int(x*5) - x
        return z
    elif slots[0] == slots[1] or slots[1] == slots[2] or slots[0] == slots[2]:
        print("Congratulations! You've matched 2 numbers and won", x*2,"cents.")
        z += int(x*2) - x
        return z
    else:
        print('Sorry, maybe next time.')
        z -= int(x)
        return z
        
main()
        
        
                
