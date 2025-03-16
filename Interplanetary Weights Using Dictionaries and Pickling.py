# Interplanetary Weights Program with Dictionaries and Pickling
# Author: Meghan Coogan

# import statement for pickle module
import pickle

# define main function
def main():
    dictGravityFactors = {
        'Mercury':0.38, 'Venus':0.91, 'our Moon':0.165, 'Mars':0.38, 'Jupiter':2.34,
        'Saturn':0.93, 'Uranus':0.92, 'Neptune':1.12, 'Pluto':0.066
                         }

    # call function to load planetary history file into a dictionary
    dictPlanetHistory = open_planetary_history()

    # call function that will display the planetary history if user wishes to see it
    display_planetary_history(dictPlanetHistory)

    # code a while loop, asking the user for a unique Name to make sure
    # the Name doesn't already exist in dictPlanetHistory (both upper and lowercase)
    while True:
        sName = input("What is your name (enter key to quit): ").title()

        # if the user enters a blank name, break out of the loop
        if sName == '': break

        # if sName already exists, ask the user for another unique name
        elif sName in dictPlanetHistory:
            print(f"{sName} is already in the history file. Enter a unique name")
            continue

        # prompt the user for their Earth Weight & call input validation function to check for bad data
        fEarthWeight = get_float_input("What is your weight: ")

        # call function to calculate sName's weight on different planets
        # pass fEarthWeight and dictGravityFactors as parameters
        dictPersonWeights = calculate_planetary_weights(fEarthWeight, dictGravityFactors)

        # call function to print out sName's planetary weights
        output_planetary_weights(sName, dictPersonWeights)

        # add sName's weights to dictPlanetHistory
        # sName is the key and the dictionary dictPersonWeights is the value
        dictPlanetHistory[sName] = dictPersonWeights

    # add dictPlanetHistory to mcPlanetaryWeights.db file
    output_file = open('mcPlanetaryWeights.db', 'wb')
    pickle.dump(dictPlanetHistory, output_file)
    output_file.close()

# function to get float input, using try/except to handle ValueError
# keep prompting until a valid number is entered
def get_float_input(sPromptMessage):
    fInput = 0.0
    nMinNumber = 0
    sErrorMessage = "Input must be a numeric value that is greater than 0."

    while fInput <= nMinNumber:

        try:
            fInput = float(input(sPromptMessage))
            if fInput <= nMinNumber:
                print(sErrorMessage)
        except ValueError:
            print(sErrorMessage)

    return fInput

# function to open up pickling file that stored previous values from the program
# name the file mcPlanetaryWeights.db and return dictPlanetHistory
def open_planetary_history():
    dictPlanetHistory = {}

    # code try/except to handle if the file does not exist
    try:
        input_file = open('mcPlanetaryWeights.db', 'rb')

        # transfer the contents of the .db file into dictPlanetHistory and close the file
        dictPlanetHistory = pickle.load(input_file)
        input_file.close()

    # if file not found, pass
    except FileNotFoundError:
        pass

    return dictPlanetHistory

# function to output planetary weights, formatted in columns using f-string
# takes in two parameters: sName and a dictionary of the person's weights on each planet
def output_planetary_weights(sName, dictPlanetaryWeights):
    print(f"{sName}, here are your weights on our Solar System's planets.")
    for sPlanet, fWeight in dictPlanetaryWeights.items():
        print(f"Weight on {sPlanet + ':':10} {fWeight:10.2f}")

# display planetary history if the user wishes to see it and history file exists
def display_planetary_history(dictHistory):

    # ask the user if they wish to see planetary history (Y,y,N,n) (if planetary history dictionary isn't empty)
    if dictHistory:
        sPlanetaryHistory = input('Would you like to see the planetary history (y/n): ').lower()

        # if y, print out the previous entries from dictHistory
        if sPlanetaryHistory == 'y':
            for sName, dictWeights in dictHistory.items():
                output_planetary_weights(sName, dictWeights) # call function to output formatted weights

# function to calculate a person's planetary weights using their earth weight and gravity factors dictionary
# return a dictionary of the person's weights on each planet
def calculate_planetary_weights(fEarthWeight, dictFactors):

    # declare empty dictionary called dictPersonWeights
    dictPersonWeights = {}

    # for each planet, compute weight using factors dictionary and fEarthWeight
    # add the planet name and the computed planet weights to dictPersonWeights
    for sPlanet in dictFactors:
        fPlanetWeight = fEarthWeight * dictFactors[sPlanet]
        dictPersonWeights[sPlanet] = fPlanetWeight

    return dictPersonWeights

# call the main function
main()
