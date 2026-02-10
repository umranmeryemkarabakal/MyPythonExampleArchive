import json

person_string = '{"name":"Ali", "languages": ["python", "C#"]}'

person_dict = {
    "name":"Ali",
    "languages":["python","C#"]
}

with open("person.json","w") as file:
    json.dump(person_dict, file)

with open("person.json") as file:
    data = json.load(file)
    print(data["name"])
    print(data["languages"])


result = json.dumps(person_dict)
print(type(result))


person_dict = json.loads(person_string)
print(person_string)

result = json.dumps(person_dict, indent =4, sort_keys=True)
print(result)