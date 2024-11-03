
"""
Write a Python function to check whether a string is pangram or not. (Assume
the string passed in does not have any punctuation)
Note: Pangrams are words or sentences containing every letter of the
alphabet at least once. For example: "The quick brown fox jumps over the
lazy dog"

"""
def check_panagram(str):
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for char in alphabet: 
        if char not in str.lower():
            return False
        else:
            return True
str=input('enter the sentence  ')
if(check_panagram(str)==True):
    print('the sentence entered is a panagram')
else:
    print('the sentence is not panagram')

        
    

