attendance=[18,20,19,15,21]
daycount=0
total_attendance=0
for x in attendance:
    if x>=20:
        print("Full")
    else:
        print("Not Full")

for x in attendance:
    if x>=20:
        daycount=daycount+1
print("total no: of days the class was full",daycount)
    
for x in attendance:
    total_attendance=total_attendance+x
print("total attendance of 5 days=",total_attendance)