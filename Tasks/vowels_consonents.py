# WAP to identify no. of vowels and consonants from the string

v=input("Please enter a string : ");
vowels=0
consonants=0

for i in v:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1
    else:
        consonants=consonants+1

print("The number of vowels:",vowels)
print("\nThe number of consonant:",consonants)
