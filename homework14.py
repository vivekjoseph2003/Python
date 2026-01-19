import random
import math
names_input=input("Enter the names of customers:")
names=[name.strip() for name in names_input.split(",") if name.strip()]
unique_names=list(set(names))
if len(unique_names)<2:
    print("Not enough unique participants to pick 2 winners.")
else:
    random.shuffle(unique_names)
    winners=random.sample(unique_names,2)
    reversed_winners=[winner[::-1] for winner in winners]
    total_participants=len(unique_names)
    rounded_sqrt=round(math.sqrt(total_participants))
    print("\nLucky Draw Winners")
    print(f"Winner 1 (reversed):{reversed_winners[0]}")
    print(f"Winner 2 (reversed):{reversed_winners[1]}")
    print(f"\nTotal unique participants:{total_participants}")
    print(f"Rounded square root of participants:{rounded_sqrt}")
