# SQL Data Manipulation with Python
# Part 1: Data creation, import, and insertion
# Author: Meghan Coogan

import sqlite3
import csv
from pathlib import Path

# getDataInput function to read the entire file in
# function will return a list of all the records
def getDataInput(sTextFile):

    # use Path from pathlib and with statement syntax to handle the file and open in read mode
    # convert file using csv reader method, make it a list, skip headings, and return the list
    data_file = Path(sTextFile)
    with data_file.open(mode='r') as file:
        return list(csv.reader(file))[1:]

# creates a table using dbConnection object, table name, and the column names + data types
# returns a boolean variable to determine if a table exists
def createTable(dbConnection, sTable, sColumns):

    # try to create a table; if the table exists, set boolean variable to True and print error message
    bTableExists = False
    try:
        dbConnection.execute(f"CREATE TABLE {sTable}({sColumns})")

    except sqlite3.OperationalError:
        bTableExists = True
        print(f"{sTable} Table already exists")

    return bTableExists

# function to insert data into tables
# 3 Parameters: dbCursor object, a list of values, and a string of the table's name
def insertData(dbCursor, data_list, sTable):

    if len(sTable) == 3:
        for sRecord in data_list:
            sInsertStatement = f"INSERT INTO {sTable} VALUES('{sRecord[0]}', '{sRecord[1]}', '{sRecord[2]}')"
            dbCursor.execute(sInsertStatement)
    else:
        for sRecord in data_list:
            sInsertStatement = f"INSERT INTO {sTable} VALUES('{sRecord[0]}', '{sRecord[1]}')"
            dbCursor.execute(sInsertStatement)

def main():

    # create a sqlite database and a cursor object
    dbConnection = sqlite3.connect("EmployeeInfo.db")
    dbCursor = dbConnection.cursor()

    # create 3 Tables: Employee, Pay, SocialSecurityMin
    bEmpExists = createTable(dbConnection, 'Employee', 'EmployeeID integer, Name text')
    bPayExists = createTable(dbConnection, 'Pay', 'EmployeeID integer, Year integer, Earnings real')
    bSocSecExists = createTable(dbConnection, 'SocialSecurityMin', 'Year integer, Minimum real')

    # insert the data into Employee, Pay, and Social Security tables if the tables didn't already exist
    # call getInput function to get data from files and insertData function to insert the data into the appropriate table
    if not bEmpExists:
        employees_list = getDataInput('Employee.txt')
        insertData(dbCursor, employees_list, 'Employee')

    if not bPayExists:
        pay_list = getDataInput('Pay.txt')
        insertData(dbCursor, pay_list, 'Pay')

    if not bSocSecExists:
        socialSecurity_list = getDataInput('SocialSecurityMinimum.txt')
        insertData(dbCursor, socialSecurity_list, 'SocialSecurityMin')

    dbConnection.commit() # commit the data changes

    dbConnection.close() # close the database connection

main()