from tracker import get_record
from datetime import datetime
import json
records=[]
for i in range(1,4):
    print("\nRecord",i,":")
    city=input("Enter city name:")
    comment=input("Enter your comment:")
    date_str=input("Enter visit date (dd-mm-yyyy):")

    record=get_record(city,comment,date_str)
    date_obj=datetime.strptime(record["date"],"%d-%m-%Y")
    record["date"]=date_obj.strftime("%B %d, %Y")
    records.append(record)

records_json=json.dumps(records)
print("\nAll travel records in JSON format:")
print(records_json)
parsed_records = json.loads(records_json)
print("\nParsed travel records:")
for rec in parsed_records:
    print(rec)