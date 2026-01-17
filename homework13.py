import os
n=int(input("How many names"))
if os.path.exists("students.txt"):
    f=open("students.txt","r")
    print("Existing student names:")
    print(f.read())
    f.close()
    f=open("students.txt","a")
else:
    f=open("students.txt","w")
for i in range(n):
    name=input("Enter student name:")
    f.write(name+"\n")
f.close()
f=open("students.txt","r")
print("Updated student names:")
print(f.read())
f.close()