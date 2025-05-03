# Use Numerology with Inheritance program
# Author: Meghan Coogan

import NumerologyLifePathDetails as num
from datetime import datetime

def main():

    while True:

        # get name from the user; inputted name should not be empty and should contain a-z characters
        # continue asking until user enters name, then break out of loop
        sName = input("Enter your full name (don't leave blank): ").title()
        if sName.replace(" ", "").isalpha() and sName != '': break

    # call function to validate DOB input
    sDOB = validateDOB()

    # call the lifepathdetails class __init__ to instantiate an object
    numerology = num.LifePathDetails(sName, sDOB)

    # use properties to get Attitude, BirthDay, and LifePath numbers
    print(f"{'Attitude number:':25} {numerology.Attitude}")
    print(f"{'Birth Day number:':25} {numerology.BirthDay}")
    print(f"{'Life Path number:':25} {numerology.LifePath}")

    numerology.convertName() # convert name to use in numerology calculations

    # use properties to get Soul, Personality, and PowerName numbers
    print(f"{'Soul number:':25} {numerology.Soul}")
    print(f"{'Personality number:':25} {numerology.Personality}")
    print(f"{'Power Name number:':25} {numerology.PowerName}\n")

    # get the Life Path description using properties
    print(f"Life Path Details: {numerology.LifePathDescription}\n")
    print(numerology) # call _str_ method to get the state of numerology object

# function to validate DOB input --> checks date length and date format
# the inputted DOB should be tested to verify 8 digits are entered with - or / as separators
def validateDOB():

    while True:

        sDOB = input("Date of Birth (mm-dd-yyyy): ")
        lstBirthdate = sDOB.replace("-", '/').split("/") # replace - and split at / to test date

        # print error message if inputted DOB is incorrect length
        if len(lstBirthdate[0]) != 2 or len(lstBirthdate[1]) != 2 or len(lstBirthdate[2]) != 4:
            print(f"{sDOB} was entered incorrectly. Date should be entered in the format: mm-dd-yyyy or mm/dd/yyyy.")
            continue

        # try to use datetime.strptime to check if date format is correct
        try:
            date_check = datetime.strptime(sDOB.replace("-", "").replace("/", ""), '%m%d%Y')
            break # break out of loop if the format is correct

        # except: print error message and continue asking for input
        except:
            print(f"Error: {sDOB} is an invalid date.")
            continue

    return sDOB

main()