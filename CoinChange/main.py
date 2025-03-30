
from amounts import coins as coin

def main(): #Main user interface
    while True:
        ask = input('WELCOME TO COIN CHANGER.\nFirst. What country will you like to pick?\n\n1) Russia\n2) USA\n3) Colombia\n4) Mexico\n')
        if ask == '1':
            country = 'Russia'
            coin(country)
        elif ask == '2':
            country = 'US'
            coin(country)
        elif ask == '3':
            country = 'Colombia'
            coin(country)
        elif ask == '4':
            country = 'Mexico'
            coin(country)
        else: 
            print('Choose a VALID OPTION')
            continue


main()