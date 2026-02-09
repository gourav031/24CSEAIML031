def pallindrome(number):
    number_str=str(number)
    if (number_str==number_str[::-1]):
         return "pallindrome"
    else:
         return "not pallindrome"
number=int(input("enter number-"))
print(pallindrome(number))