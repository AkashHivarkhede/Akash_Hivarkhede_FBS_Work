# Write a program to input any alphabet and check whether it is vowel or consonant.

alpha = str(input('Enter a letter :'))

vowel = 'aeiou'

if(alpha.lower() in vowel):
    print('Alphabet is vowel')
else:
    print('Alphabet is consonanet')