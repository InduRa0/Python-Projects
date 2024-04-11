from datetime import date, datetime

# ask the user for their date of birth
dob_str = input("Enter your date of birth in the format mm/dd/yyyy: ")

# attempt to parse the input into a date object
try:
    dob = datetime.strptime(dob_str, "%m/%d/%Y").date()
except ValueError:
    print("Error: invalid date format. Please use the format mm/dd/yyyy.")
    exit()

# check if the date is in the future
if dob > date.today():
    print("Error: date of birth cannot be in the future.")
    exit()

# calculate the age
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

# output the age and the date in European format
print("Your age is:", age)
print("Your date of birth in European format is:", dob.strftime("%d/%m/%Y"))
