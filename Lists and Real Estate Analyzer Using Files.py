# Real Estate Analyzer Program Using Files
# Author: Meghan Coogan

# import csv module and import Path from pathlib
import csv
from pathlib import Path

# getDataInput function to read the entire file in
# function will return a list of all the records
def getDataInput():

    # use Path from pathlib and with statement syntax to handle the file and open in read mode
    # convert file using csv reader method, make it a list, skip headings, and return the list
    data_file = Path('RealEstateData.csv')
    with data_file.open(mode='r') as file:
        return list(csv.reader(file))[1:]

# getMedian function receives a list as a parameter and returns a float
def getMedian(sales_list):

    # if the number of elements is even, divide count by 2 & take that entry
    # and the entry before it and average the two elements to use as median
    if len(sales_list) % 2 == 0:
        iMedian = len(sales_list) // 2
        fMedianValue = (sales_list[iMedian - 1] + sales_list[iMedian]) / 2

    # if the number of elements in the list is odd, divide count by 2
    # and use that entry as the median
    else:
        iMedian = len(sales_list) // 2
        fMedianValue = sales_list[iMedian]

    # return the calculated median value
    return fMedianValue

# display summary of total prices from real estate dictionaries
def display_property_summary(real_estate_dict, sString):
    print(f"Summary by {sString}:")
    for sKey, fPrice in real_estate_dict.items():
        print(f"{sKey + ':':20} {fPrice:14,.2f}")
    print()

# function to find  and display the max, min, sum, average,
# and median prices from the prices_list
def find_price_analytics(prices_list):

    # sort the list of property prices from smallest value to largest
    prices_list.sort()

    # from the prices_list, determine the minimum value and
    # output formatted as currency with 2 decimal positions to the screen
    print(f"{'Minimum:':10} {min(prices_list):15,.2f}")

    # from the prices_list, determine the maximum value and
    # output formatted as currency with 2 decimal positions to the screen
    print(f"{'Maximum:':10} {max(prices_list):15,.2f}")

    # from the prices_list, determine the total value and
    # output formatted as currency with 2 decimal positions to the screen
    print(f"{'Sum:':10} {sum(prices_list):15,.2f}")

    # from the prices_list, determine the average value and
    # output formatted as currency with 2 decimal positions to the screen
    print(f"{'Average':10} {sum(prices_list)/len(prices_list):15,.2f}")

    # from the prices_list, determine the median value by calling the getMedian function
    # and output formatted as currency with 2 decimal positions to the screen
    fMedianPrice = getMedian(prices_list)
    print(f"{'Median:':10} {fMedianPrice:15,.2f}")
    print()

# code a main function that extracts these columns from the record:
# 1. City, 2. Property Type, 3. Zip, 4. Price
def main():

    # call the getDataInput function to get the data you need for this program
    real_estate_list = getDataInput()

    # create empty prices_list and empty dictionaries for cities, zip code, and property type
    prices_list = []
    cities_dict = {}
    zip_dict = {}
    property_type_dict = {}

    # code a for loop that reads each record from the real_estate list
    for sRecord in real_estate_list:

        # extract the columns for city, zip code, property type, and price from the list
        sCity = sRecord[1].title()
        sZip = sRecord[2]
        sPropertyType = sRecord[7]
        fPrice = float(sRecord[8]) #convert price to a float

        # add each price to a list
        prices_list.append(fPrice)

        # for each city, total up the price and add to cities dictionary
        cities_dict[sCity] = cities_dict.get(sCity, 0.0) + fPrice

        # for each zip, total up the price and add to zip dictionary
        zip_dict[sZip] = zip_dict.get(sZip, 0.0) + fPrice

        # for each property type, total up the price and add to property_type dictionary
        property_type_dict[sPropertyType] = property_type_dict.get(sPropertyType, 0.0) + fPrice

    # call function to find the min, max, sum, average, and median prices from the prices_list
    find_price_analytics(prices_list)

    # call function to display total price for each city, zip code, and property type
    display_property_summary(property_type_dict, 'Property Type')
    display_property_summary(cities_dict, 'City')
    display_property_summary(zip_dict, 'Zip Code')

main()