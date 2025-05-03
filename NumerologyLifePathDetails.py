# Numerology Class with Inheritance program
# Author: Meghan Coogan

class Numerology:

    # __init__ has three parameters: self, sName, and sDOB
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

        # create empty string attributes for vowels and consonants to use for name manipulation
        self.__vowels = ''
        self.__consonants = ''

    # property that returns the person's name
    @property
    def Name(self):
        return self.__name

    # property that returns the birthdate
    @property
    def Birthdate(self):
        return self.__birthdate

    # get the attitude number: addition of birth month (mm) and birth day (dd) numbers
    @property
    def Attitude(self):

        # replace - or / in the birthdate with empty string and call getSum method with self.__birthdate as the parameter
        # set self.__attitude attribute to reduced value and then return the number
        self.__attitude = self.getSum(self.__birthdate.replace('-', '').replace('/', '')[0:4]) # first 4 index positions (0-3) are: mm dd
        return self.__attitude

    # extract the day from the birthdate list to calculate the Birth Day number
    @property
    def BirthDay(self):

        self.__birthDay = self.getSum(self.__birthdate.replace('/', '').replace('-', '')[2:4]) # dd is index positions 2-3
        return self.__birthDay

    # get the Life Path Number by adding all the digits of sDOB and reduce until a single digit
    @property
    def LifePath(self):

        self.__lifePath = self.getSum(self.__birthdate.replace('-', '').replace('/', ''))
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

        # for each character in sName, add the character to sVowels or sConsonants
        for ch in sName.upper():
            if ch in vowels_list:
                self.__vowels += ch
            else:
                self.__consonants += ch

            # convert letters to numbers using the letters dictionary
            for num_key, letter_list in letters_dict.items():

                # if a character is in the letter_list, convert num_key to a string,
                # and replace ch with a number for self.__vowels and self.__consonants attributes
                if ch in letter_list:
                    self.__vowels = self.__vowels.replace(ch, str(num_key))
                    self.__consonants = self.__consonants.replace(ch, str(num_key))

    # add all the vowels in self.__name and reduce until single digit to get the Soul number
    @property
    def Soul(self):

        self.__soul = self.getSum(self.__vowels)
        return self.__soul

    # take all the consonants in the name and add them together
    @property
    def Personality(self):

        self.__personality = self.getSum(self.__consonants)
        return self.__personality

    # add the soul number and the personality number together and reduce
    @property
    def PowerName(self):

        self.__powerName = self.__reduceNumber(self.__soul + self.__personality)
        return self.__powerName

    # method to get the sum for numerology calculations
    def getSum(self, sNumberToSum):
        iNumber = 0
        for char in sNumberToSum:
            iNumber += int(char)

        return self.__reduceNumber(iNumber) #return the reduced number

    # private method to calculate numerology number and reduce to a single digit
    def __reduceNumber(self, iNumber):

        if int(iNumber) <= 9:
            return iNumber
        else:
            return self.__reduceNumber(iNumber // 10 + iNumber % 10) # reduce number with recursion

    # __str__ method will return the state of an object
    def __str__(self):
        return (f"Client Name: {self.__name}\n"
                f"Client DOB: {self.__birthdate}\n"
                f"{'Attitude:':15} {self.__attitude}\n"
                f"{'Birth Day:':15} {self.__birthDay}\n"
                f"{'Life Path:':15} {self.__lifePath}\n"
                f"{'Soul:':15} {self.__soul:}\n"
                f"{'Personality:':15} {self.__personality}\n"
                f"{'Power Name:':15} {self.__powerName}")

# life path class inherits from numerology class
class LifePathDetails(Numerology):

    def __init__(self, sName, sDOB):
        Numerology.__init__(self, sName, sDOB) # call Numerology init method

        # set life path details attribute to empty string
        self.__lifePathDetails = ''

    # property that calls the LifePath property to return the life path description
    @property
    def LifePathDescription(self):

        lifePathDetails = {1:'The Independent: Wants to work/think for themselves',
                           2:'The Mediator: Avoids conflict and wants love and harmony',
                           3:'The Performer: Likes music, art, and to perform or get attention',
                           4:'The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful',
                           5:'The Adventurer: Likes to travel and meet others, often an extrovert',
                           6:'The Inner Child: Is meant to be a parent and/or one that is young at heart',
                           7: 'The Naturalist: Enjoys nature and water and alternative life paths; open to spirituality',
                           8:'The Executive: Gravitates to money and power',
                           9:'The Humanitarian: Helps others and/or experiences pain and learns the hard way'
                           }

        # use dictionary's get method and Numerology class's LifePath property to find life path details
        self.__lifePathDetails = lifePathDetails.get(self.LifePath, 'Not Found')
        return self.__lifePathDetails

    # call the Numerology class's __str__ method and add lifePathDetails attribute
    def __str__(self):
        return (f"{Numerology.__str__(self)}\n" 
                f"Life Path Description: {self.__lifePathDetails}")