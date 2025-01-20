student_name={"id1":{ "Name": "Umar","Class":8},"id2":{ "Name": "Zara","Class":6},
              "id3":{ "Name": "Zara","Class":6},"id4":{ "Name": "Hi","Class":6}}

result={}

for k,v in student_name.items():
    if v not in result.values():
        result[k]=v

print(result)