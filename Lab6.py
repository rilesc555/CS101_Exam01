
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


def Decrypt(string_text, int_key) -> str:
    ''' Decrypts Caesar-encrypted string with specified key. '''



def Get_input()->str:
    '''Interacts with user. Returns one of: '1', '2', '3', '4'.'''


def Print_menu():
  '''Prints menu. No user interaction. '''

  
def main(): 

      
      
# our entire program: 
main() 
