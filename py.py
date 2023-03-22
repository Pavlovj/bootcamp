import json
from datetime import datetime, timedelta

# Define the products and their properties
products = [
    { 'name': 'bananas', 'amount': [100, 150], 'price': 1 },
    { 'name': 'oranges', 'amount': [80, 120], 'price': 3 },
    { 'name': 'tomatoes', 'amount': [150, 200], 'price': 1.5 },
    { 'name': 'lemons', 'amount': [80, 100], 'price': 5 },
    { 'name': 'grapes', 'amount': [50, 70], 'price': 3 },
]

# Define an empty list to store the days
days = []

# Define a function to add a week of data
def addWeek(numberOfWeeks, startDate):
    days = []  # Define an empty list to store the days for the current week
    for i in range(numberOfWeeks):
        for j in range(7):  # Add data for each day of the week
            days.append(addDay(startDate))  # Add data for the current day to the list
            startDate += timedelta(days=1)  # Increment start date by 1 day
    return days

# Define a function to add data for a single day
def addDay(startDate):
    day = {}  # Define an empty dictionary to store the data for the day
    for product in products:
        amount = product['amount']  # Get the range of amounts for the current product
        day[product['name']] = {
            'date': startDate.isoformat(),  # Store the date of the day as an ISO-formatted string
            'amount': randomNumber(amount[0], amount[1]),  # Generate a random amount for the product within the given range
            'price': product['price']  # Store the price of the product
        }
    return day

# Define a function to generate a random integer within a range
def randomNumber(min, max):
    return int(min + (max - min + 1) * random.random())

# Set the start date for the data
startDate = datetime(2022, 3, 22)

# Generate 52 weeks of data starting from the given start date
days = addWeek(52, startDate)

# Store the data in a dictionary
data = {'days': days}

# Write the data to a JSON file
with open('input.json', 'w') as outfile:
    json.dump(data, outfile)

print('Complete')
