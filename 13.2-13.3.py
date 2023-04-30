import datetime

# Read the contents of the file into a string variable
with open('today.txt', 'r') as file:
    today_string = file.read()

# Parse the date from the string
date_obj = datetime.datetime.strptime(today_string.strip(), '%Y-%m-%d').date()

# Print the parsed date
print(date_obj)
