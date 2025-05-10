# PART 2: Use the SQlite database
# Author: Meghan Coogan

import sqlite3

def main():

    # DB connection and cursor
    dbConnection = sqlite3.connect("EmployeeInfo.db")
    dbCursor = dbConnection.cursor()

    # join all three tables together and retrieve EmployeeID, Name, Year, Earnings, and Minimum values
    # join Employee and Pay tables using EmployeeID and join Pay to SocialSecurityMin using Year
    sSelect = ("SELECT Employee.Name, Pay.Year, Pay.Earnings, SocialSecurityMin.Minimum FROM Employee "
               "INNER JOIN Pay ON Employee.EmployeeID = Pay.EmployeeID INNER JOIN SocialSecurityMin ON Pay.Year = SocialSecurityMin.Year ORDER BY Employee.Name")

    dbCursor.execute(sSelect) # execute select statement to join tables

    print(f"{'Employee Name': <20} {'Year': <12} {'Earnings': <15} {'Minimum': <8} Include") # print column headings

    # process each record in the data result set using fetchall() method
    for tupEmployeePay in dbCursor.fetchall():

        # if the Earnings columns in the Pay file is >= the Minimum column print out Yes
        # if less than, print out no
        sSocialSec = "No"
        if tupEmployeePay[2] >= tupEmployeePay[3]:
            sSocialSec = "Yes"

        print(f"{tupEmployeePay[0]: <20} {tupEmployeePay[1]: <10} {tupEmployeePay[2]: >10,.2f} {tupEmployeePay[3]: 15,.2f} {sSocialSec}")

    dbConnection.close() # close the database connection

main()