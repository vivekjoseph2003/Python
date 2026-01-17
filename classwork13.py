import os
item=input("Enter item:")
if os.path.exists("items.txt"):
    f=open("items.txt","a")
    f.write(item)
    f.close()
else:
    f=open("items.txt","w")
    f.write(item)
    f.close()
f=open("items.txt","r")
print("\nList of items in the shop:")
print(f.read())
f.close()