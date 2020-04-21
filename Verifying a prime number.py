user_input = int(input("Enter a number greater than 1 to verify whether it is a prime number or not: ")) #accepting input
factors = []
not_prime = 2
if user_input <=1:
    print("Enter a valid input")
else:
    for divisor in range(2,user_input):
        if user_input%divisor == 0:
            factors.append(divisor)
        else:
            not_prime = not_prime+1
    if not_prime == user_input:
        print("It is a prime number")
    else:
        print("It is not a prime number. It can be divided by the following factors:")
        for i in range(len(factors)):
            print(factors[i])

