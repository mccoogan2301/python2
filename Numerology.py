# Numerology Class
# Author: Meghan Coogan

class Numerology:

    # __init__ has three parameters: self, sName, and sDOB
    # attributes should be private
    def __init__(self, sName, sDOB):
        self.__name = sName
        self.__birthdate = sDOB

        # set numerology number attributes to zero to use later in the __str__ method
        self.__attitude = 0
        self.__birthDay = 0
        self.__lifePath = 0
        self.__personality = 0
        self.__soul = 0
        self.__powerName = 0

    # method to get the person's name
    def getName(self):
        return self.__name

    # method to get the person's birthdate
    def getBirthdate(self):
        return self.__birthdate

    # remove - and / from birthdate so it can be used for calculations
    def convertDOB(self):
        return self.__birthdate.replace('-', '').replace('/', '')

    # get the attitude number: addition of birth month (mm) and birth day (dd) numbers
    def getAttitude(self, sDOB):

        # call getSum method and set self.__attitude attribute to the reduced value
        self.__attitude = self.getSum(sDOB[0:4]) # first 4 index positions (0-3) are: mm dd
        return self.__attitude

    # extract the day from the birthdate list to calculate the Birth Day number
    def getBirthDay(self, sDOB):
        self.__birthDay = self.getSum(sDOB[2:4]) # birth day (dd) is index 2-3
        return self.__birthDay

    # get the Life Path Number by adding all the digits of sDOB and reduce until a single digit
    def getLifePath(self, sDOB):
        self.__lifePath = self.getSum(sDOB)
        return self.__lifePath

    # get numbers derived from birth name: convert the letters to a corresponding number
    # use this to find soul number, personality number, and power name number
    def convertName(self):
        letters_dict = {1:['A', 'J', 'S'], 2:['B', 'K', 'T'], 3:['C', 'L', 'U'],
                        4:['D', 'M', 'V'], 5:['E', 'N', 'W'], 6:['F', 'O', 'X'],
                        7:['G', 'P', 'Y'], 8:['H', 'Q', 'Z'], 9:['I', 'R']
                        }

        sName = self.__name.replace(' ', '') # remove space from self.__name
        vowels_list = ['A', 'E', 'I', 'O', 'U'] # create vowels list
        sVowels = ''
        sConsonants = ''

        # for each character in sName, add the character to sVowels or sConsonants
        for ch in sName.upper():
            if ch in vowels_list:
                sVowels += ch
            else:
                sConsonants += ch

            # convert letters to numbers using the letters dictionary
            for num_key, letter_list in letters_dict.items():

                # if a character is in the letter_list, convert num_key to a string,
                # and replace ch with a number for sVowels and sConsonants variables
                if ch in letter_list:
                    sVowels = sVowels.replace(ch, str(num_key))
                    sConsonants = sConsonants.replace(ch, str(num_key))

        # returns two string variables consisting of digits (1-9)
        return sVowels, sConsonants

    # add all the vowels in self.__name and reduce until single digit to get the Soul number
    def getSoul(self, sVowels):
        self.__soul = self.getSum(sVowels)
        return self.__soul

    # add all the consonants in the name and reduce to get Personality number
    def getPersonality(self, sConsonants):
        self.__personality = self.getSum(sConsonants)
        return self.__personality

    # add the soul number and the personality number together and reduce
    def getPowerName(self, iSoul, iPersonality):
        self.__powerName = self.__reduceNumber(iSoul + iPersonality)
        return self.__powerName

    # get sum for numerology calculations, then call reduceNumber method
    # and return a single digit integer
    def getSum(self, sNumberToSum):
        iNumber = 0
        for char in sNumberToSum:
            iNumber += int(char)

        return self.__reduceNumber(iNumber)

    # private method to reduce number to a single digit
    def __reduceNumber(self, iNumber):

        if int(iNumber) <= 9:
            return iNumber
        else:
            return self.__reduceNumber(iNumber // 10 + iNumber % 10) # reduce number with recursion

    # __str__ method will return the state of an object
    def __str__(self):
        return (f"Client Name: {self.__name}\n"
                f"Client DOB: {self.__birthdate}\n"
                f"{'Life Path:':15} {self.__lifePath}\n"
                f"{'Attitude:':15} {self.__attitude}\n"
                f"{'Birth Day:':15} {self.__birthDay}\n"
                f"{'Soul:':15} {self.__soul:}\n"
                f"{'Personality:':15} {self.__personality}\n"
                f"{'Power Name:':15} {self.__powerName}")