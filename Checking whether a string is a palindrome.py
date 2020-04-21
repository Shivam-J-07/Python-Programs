user_input = input(("Enter a word to check whether it is a palindrome or not: "))
user_input = user_input.lower() #ignoring case
reversed_string = user_input[::-1]
if reversed_string == user_input:
    print("It is a palindrome!")
else:
    print("It is not a palindrome")
