import csv
import re

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
        IDs.append(row[0])

        PlaceHolder = re.split(" ", row[1])
        FirstNames.append(PlaceHolder[0])
        LastNames.append(PlaceHolder[1])
        PlaceHolder.clear()

        PlaceHolder = re.split("-", row[2])
        ConvertedDates.append(f"{PlaceHolder[1]}/{PlaceHolder[2]}/{PlaceHolder[0]}")
        PlaceHolder.clear()

        PlaceHolder = re.split("-", row[3])
        ConvertedSSNs.append(f"***-**-{PlaceHolder[2]}")
        PlaceHolder.clear()

        ConvertedStates.append(us_state_abbrev[row[4]])


    #print(", ".join(IDs[n], FirstNames[n], LastNames[n], ConvertedDates[n]))

ConvertedData = zip(IDs, FirstNames, LastNames, ConvertedDates, ConvertedSSNs, ConvertedStates)    

with open("output_file.csv", "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerows(ConvertedData)