import random
import math
names_input=input("Enter the names of invited guests:")
names=[name.strip() for name in names_input.split(",") if name.strip()]
unique_names=list(set(names))
chosen_name=random.choice(unique_names)
reversed_name=chosen_name[::-1]
total_unique=len(unique_names)
rounded_sqrt=round(math.sqrt(total_unique))
print(f"\nRandomly selected name:{chosen_name}")
print(f"Reversed name:{reversed_name}")
print(f"Total unique names:{total_unique}")
print(f"Rounded square root of total:{rounded_sqrt}")