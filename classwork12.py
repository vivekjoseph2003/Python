import re
try:
    title=input("Enter book title:")
    year=input("Enter publication year:")

    if not re.search(r'^[A-Za-z ]+$',title):
        raise ValueError("Only letters and spaces are allowed")

    if not re.search(r'^(19|20)\d{2}$',year):
        raise ValueError("should start with 19 or 20 and be 4 digits.")

    print("Book details accepted")
    print("Title:",title)
    print("Publication Year:",year)

except ValueError as e:
    print("Error:",e)

finally:
    print("Program execution completed.")