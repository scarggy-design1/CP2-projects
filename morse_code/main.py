#This is Nicoles Morse Code
import string

basics = str(string.digits)
numbers = list(basics)
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
SYM_NUM = symbols + numbers
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
specifc_morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
'.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', ' ', '/']

MORSE_CODES = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
'.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..', ' ']

def convert_EM():
    word = input("What is your sentence/word you'd like to convert?: ").upper()
    finalWord = list(word)
    
    # Check if there are any invalid characters
    if any(char in SYM_NUM for char in finalWord) and '.' not in finalWord:
        print("You cannot have numbers or special characters. (excluding periods)")
        return 'error'
    
    empty = []
    for char in finalWord: 
        if char == ' ' or char == '.':
            empty.append('/')
        else:
            try:
                instances = LETTERS.index(char)
                morse = MORSE_CODES[instances]
                empty.append(morse)
                empty.append('/')
            except ValueError:
                pass 

    print(*empty, sep=" ") 
    print('')

def convert_ME():
    dots = input("""What is your sentence/word you'd like to convert? Please put spaces between letters in morse, and separate with /'s: 
                 EXAMPLE: ... / --- / ... OR ...   ---   ...
    """)
    finalDots = dots.split()
    
    if any(char not in specifc_morse for char in finalDots):
        print("You cannot have numbers or special characters. (excluding .-/)")
        return 'error'
    
    empty = []
    for code in finalDots:
        if code == '/':
            empty.append(' ')
        else:
            try:
                instances = specifc_morse.index(code)
                word = LETTERS[instances]
                empty.append(word)
            except ValueError:
                pass 

    print(*empty, sep="") 
    print('')

def main():
    while True:
        ask = input("""
What would you like to do?
1) Convert from English
2) Convert from Morse
                    """)
        if ask == '1':
            english_morse = convert_EM()
            if english_morse == 'error':
                print("Try again")
        elif ask == '2':
            morse_english = convert_ME()
            if morse_english == 'error':
                print("Try again")
        else:
            print("Pick a valid input. TRY AGAIN.")

main()