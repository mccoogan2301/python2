# Password Validator Program
# Author: Meghan Coogan

def main():
    
    # prompt the user for their First and Last name and store in sName
    sName = input("Enter your full name such as John Smith: ")

    # while loop to keep asking for a password until a valid one is entered
    # prompt the user to enter their desired password and store in sPassword
    while True:
        sPassword = input("Please enter your new password: ")

        # call functions to see if password meets all requirements
        bRightLength = check_length(sPassword)
        bHasPass = check_pass_start(sPassword)

        # if a requirement isn't met (is_valid = False), print message to the screen to inform the user
        bHasUpper, bHasLower, bHasNumber, bHasSpecial, bIsValid = check_valid_characters(sPassword)
        if not bIsValid:
            if not bHasUpper:
                print("Password must contain at least 1 uppercase letter.")

            if not bHasLower:
                print("Password must contain at least 1 lowercase letter.")

            if not bHasNumber:
                print("Password must contain at least 1 number.")

            if not bHasSpecial:
                print("Password must contain at least one of these special characters: ! @ # $ % ^")

        # check to make sure sPassword doesn't contain sInitials within the string
        bHasInitials = check_initials(sName, sPassword)

        # call function to make sure no characters are repeated
        # if repeated is not empty, print message to the screen and
        # output the character and the number of occurrences
        repeated = check_repeat_characters(sPassword)
        if repeated:
            print("These characters appear more than once: ")

            # sort dictionary first
            repeated = dict(sorted(repeated.items()))
            for sCharacter, iCount in repeated.items():
                print(f"{sCharacter}: {iCount} times")

        # check to see if all conditions are met
        # if password is valid, print message to the screen and break out of loop
        if bRightLength and not bHasPass and bIsValid and not bHasInitials and not repeated:
            print("Password is valid and OK to use.")
            break

# extract the first character of both the First name and Last name from sName
# variable and place into sInitials
# check if sPassword contains sInitials
def check_initials(sName, sPassword):
    iLastInitial = sName.find(" ")
    sInitials = sName[:1] + sName[iLastInitial + 1:iLastInitial + 2]
    bHasInitials = False

    if sInitials.lower() in sPassword.lower():
        bHasInitials = True
        print("Password must not contain user initials.")

    return bHasInitials

# check to make sure sPassword length is between 8 and 12 characters
# if sPassword isn't the correct length, print message to the screen
def check_length(sPassword):

    # create min and max length constants and set bRightLength to True
    MIN_LENGTH = 8
    MAX_LENGTH = 12
    bRightLength = True

    if not (len(sPassword) >= MIN_LENGTH and len(sPassword) <= MAX_LENGTH):
        print(f"Password must be between {MIN_LENGTH} and {MAX_LENGTH} characters.")
        bRightLength = False

    return bRightLength

# define function to make sure sPassword doesn't start with pass (any case)
# if it does, print message to the screen
def check_pass_start(sPassword):
    bHasPass = False
    if sPassword.lower().startswith("pass"):
        bHasPass = True
        print("Password can't start with Pass.")

    return bHasPass

# function to make sure password has uppercase, lowercase, number, and special characters
def check_valid_characters(sPassword):

    # set Boolean variables to False and create list of special characters
    bHasUpper = False
    bHasLower = False
    bHasNumber = False
    bHasSpecial = False
    bIsValid = False
    special_characters = ['!', '@', '#', '$', '%', '^']

    # iterate over characters in sPassword and set Boolean variables to True when requirement is met
    for ch in sPassword:
        if ch.isupper():
            bHasUpper = True
        elif ch.islower():
            bHasLower = True
        elif ch.isdigit():
            bHasNumber = True
        elif ch in special_characters:
            bHasSpecial = True

        # break out of loop if all requirements are met and set bIsValid to True
        if bHasUpper and bHasLower and bHasNumber and bHasSpecial:
            bIsValid = True
            break

    return bHasUpper, bHasLower, bHasNumber, bHasSpecial, bIsValid

# function to make sure characters in sPassword don't appear more than once
# create dictionary to keep track of repeated characters
def check_repeat_characters(sPassword):
    pass_dict = {}
    repeated = {}

    # add all characters to a dictionary and count them using get method
    for ch in sPassword.lower():
        pass_dict[ch] = pass_dict.get(ch, 0) + 1

        # check for repeated characters in pass_dict
        # if a character appears > 1 time, add it to new dictionary
        if pass_dict[ch] > 1:
            repeated[ch] = pass_dict.get(ch)

    return repeated

main()
