str1=input("Enter a String-")
s2=''.join(reversed(str1))
if str1==s2:
    print("pallindrome")
else:
    print("not pallindrome")