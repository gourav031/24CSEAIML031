n=int(input("Enter a 5 digit number-"))

for i in range(1,6):
    digit = int(i)
    if digit % 2 != 0:
        print(digit)

    print("the digits are-",digit)
