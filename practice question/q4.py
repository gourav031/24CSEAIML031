str1=input("Enter the string-")
str1_rev=str1[::-1]
print(str1_rev)
vowel=0
consonant=0
for i in str1:
    if i in 'AEIOUaeiou': 

        vowel+=1
    else:
        consonant+=1
print("no of vowels is ",vowel,"no of consonant is ",consonant)