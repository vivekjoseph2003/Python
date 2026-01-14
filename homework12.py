import re
try:
    name=input("Enter your name:")
    feedback=input("Enter your feedback:")

    if not re.search(r'\S',name):
        raise ValueError("Name cannot be empty")

    if not re.search(r'\S',feedback):
        raise ValueError("Feedback cannot be empty")

    print("Thank you for your feedback")
    print("Name:",name)
    print("Feedback:",feedback)

except ValueError as e:
    print("Error:",e)

finally:
    print("Feedback submission process completed")