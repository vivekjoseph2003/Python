from tripdata import get_trip
from datetime import datetime
import json
trips=[]
n=int(input("How many trips to add?"))

for i in range(1,n+1):
    print("\nTrip",i,":")
    city=input("Enter city name:")
    date_str=input("Enter date visited (dd-mm-yyyy): ")
    comment=input("Enter a short comment:")
    trip=get_trip(city,date_str,comment)
    date_obj=datetime.strptime(trip["date"],"%d-%m-%Y")
    trip["date"]=date_obj.strftime("%B %d, %Y")
    trips.append(trip)

trips_json=json.dumps(trips)
print("\nAll trips in JSON format:")
print(trips_json)