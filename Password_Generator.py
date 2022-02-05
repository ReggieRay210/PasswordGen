
import random  # assist in generating random variables

# all the available characters that you want to use
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@# $*[]()"
while True:
    # Ask user the length of the password
    password_len = int(input("How long would you like the password to be?:"))

    # Is there any more passwords that the user needs to create? (generate a new password each time.)
    passwordCount = int(input("How many passwords would you like to create"))

    # create a "for" loop that will create the needed amount of passwords that the user requests.
    for x in range(0, passwordCount):
        password = ''  # blank string
        for x in range(0, password_len):

            # tell the random module to choose some of the characters that was created above.
            password_char = random.choice(char)

            # concatenate the first password variable to the password_char variable
            password = password + password_char

        # this will print out the desired password.
        print("Your Generated Password is: ", password)
    break  # stop the program after the desired password count is met.
print("Good-Bye")
