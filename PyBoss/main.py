import csv
import re

#Borrowing the helpful state abbreviation dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Create a series of lists to be the columns of the output csv, including the headers
PlaceHolder = []
IDs = ["ID"]
FirstNames = ["First Name"]
LastNames = ["Last Name"]
ConvertedDates = ["DOB"]
ConvertedSSNs = ["SSN"]
ConvertedStates = ["State"]

with open("../Resources/employee_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        #IDs remain unchanged
        IDs.append(row[0])

        #Split first and last names on spaces and put them in a placeholder list
        PlaceHolder = re.split(" ", row[1])
        #Add first and last names to their respective lists
        FirstNames.append(PlaceHolder[0])
        LastNames.append(PlaceHolder[1])
        #Clear the placeholder list
        PlaceHolder.clear()

        #Splits the date on dashes and places the year, month and day into the placeholder list respectively
        PlaceHolder = re.split("-", row[2])
        #Reassembles the month, day and year (respectively) into the new, ConvertedDates list
        ConvertedDates.append(f"{PlaceHolder[1]}/{PlaceHolder[2]}/{PlaceHolder[0]}")
        #Clear the placeholder list
        PlaceHolder.clear()

        #Splits the social security number on dashes into three chunks
        PlaceHolder = re.split("-", row[3])
        #Adds only the third, four digit chunk of the SSN to a series of asterixes and adds it to the ConvertedSSN list
        ConvertedSSNs.append(f"***-**-{PlaceHolder[2]}")
        #Clear the placeholder
        PlaceHolder.clear()

        #Uses the dictionary to reference state names and then adds the abbreviated form to the ConvertedState list
        ConvertedStates.append(us_state_abbrev[row[4]])

#Zips together the various lists in the desired order
ConvertedData = zip(IDs, FirstNames, LastNames, ConvertedDates, ConvertedSSNs, ConvertedStates)    

#Outputs them all to a CSV
with open("output_file.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(ConvertedData)