import datetime
# 1. Ask for the full date as one string
user_input = input("Enter date (DD MM YYYY): ")
# 2. Split the string into a list of words
parts = user_input.split()
# 3. Convert each part to an integer manually
day = int(parts[0])
month = int(parts[1])
year = int(parts[2])
# 4. Create the date and print the result
date_obj = datetime.date(year, month, day)
print(date_obj.strftime("%A").upper())
