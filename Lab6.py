
##CS 101  
##
##PROBLEM: Do Caesar Encryption/Decryption, including cracking a string w/ 
##  unknown Caesar key. 
##  
##Functions needed: 
##  Encrypt(string_text, int_key): Takes a string and integer key, returns 
##  the encryption of the string using that key. Note that for Caesar encryption, 
##  an encryption with key k (k in 1 - 25) is decrypted by doing the same process 
##  with key 26-k. Returns encrypted string using specified key. 
##  
##  Decrypt(string_text, int_key): Decrypts key by calling Encrypt with key 
##    26-int_key and returning the result. Done this way to make for a cleaner
##    breakdown of the problem. Returns decrypted string using specified key. 
##        
##  Get_input(): Interacts with user, gets user choice of '1'-'4' and returns that 
##  value. If user enters anything else, prints brief error message and tries again. 
##  
##  Print_menu(): Prints menu. No user interaction. 
  
################################ 
import string

def Encrypt(string_text, int_key) -> str:
    '''Caesar-encrypts string using specified key.'''
    encrypted = ''
    string_text = string_text.lower()
    for letter in string_text:
        if letter in string.ascii_lowercase:
            letter = int(string.ascii_lowercase.find(letter))
            letter += int_key
            if letter > 25:
                letter -= 26
            letter = string.ascii_lowercase[letter]
        
        encrypted += letter

    return encrypted.upper()
    

def Decrypt(string_text, int_key) -> str:
    ''' Decrypts Caesar-encrypted string with specified key. '''
    decrypted = Encrypt(string_text, 26-int_key)
    return decrypted.upper()


def Get_input():
    '''Interacts with user. Returns one of: '1', '2', '3'.'''
    while True:
        user_input = input('Enter your selection ==> ')
        if user_input in ['1', '2']:
            return int(user_input)
        elif user_input == 'Q':
            return 3
        else:
            print('Invalid selection')

def Print_menu():
    '''Prints menu. No user interaction. '''
    print('MAIN MENU')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')
  
def main(): 
    Print_menu()
    answer = Get_input()
    while answer != 3:
        if answer == 1:
            secret = input('\nEnter (brief) text to encrypt: ')
            key = int(input('Enter the number to shift letters by: '))
            print(f'Encrypted: {Encrypt(secret, key)}')
        elif answer == 2:
            secret = input('\nEnter (brief) text to decrypt: ')
            key = int(input('Enter the number to shift letters by: '))
            print(f'Decrypted: {Decrypt(secret, key)}')
        print()
        Print_menu()
        answer = Get_input()
    
      
      
# our entire program: 
main() 
