# Use Numerology: Code Numerology with Classes program
# Author: Meghan Coogan

# import Numerology.py to make a Numerology object
# import datetime from datetime module to use for date validation
import Numerology
from datetime import datetime

def main():

    while True:

        # get name from the user; inputted name should not be empty and should contain a-z characters
        # continue asking until user enters name, then break out of loop
        sName = input("Enter your full name (don't leave blank): ").title()
        if sName.replace(" ", "").isalpha() and sName != '': break

    # call function to validate DOB input
    sDOB = validateDOB()

    # call the numerology class __init__ to instantiate an object
    num_obj = Numerology.Numerology(sName, sDOB)

    # convert sDOB to a list of integers to be used in calculations
    sDOB = num_obj.convertDOB()

    # call method to get the life path number
    iLifePath = num_obj.getLifePath(sDOB)
    print(f"{'Life Path Number:':20} {iLifePath}")

    # call method to get the birthday number
    iBirthDay = num_obj.getBirthDay(sDOB)
    print(f"{'Birth Day Number:':20} {iBirthDay}")

    # call method to get the attitude number
    iAttitude = num_obj.getAttitude(sDOB)
    print(f"{'Attitude Number:':20} {iAttitude}")

    # call method to split sName into vowels and consonants
    sVowels, sConsonants = num_obj.convertName()

    # get soul, personality, and power name, and output each to the screen
    iSoul = num_obj.getSoul(sVowels)
    print(f"{'Soul Number:':20} {iSoul}")

    iPersonality = num_obj.getPersonality(sConsonants)
    print(f"{'Personality Number:':20} {iPersonality}")

    iPowerName = num_obj.getPowerName(iSoul, iPersonality)
    print(f"{'Power Name Number:':20} {iPowerName}\n")

    # call __str__ method
    print(num_obj)

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