import json

data = {}

def addData(data, ip, error):
    if data.get(ip):
        if data[ip].get(error):
            data[ip][error] += 1
        else:
            data[ip][error] = 1
    else:
        data[ip] = {}
        data[ip][error] = 1

with open("./access.log", "r") as file_pointer:
    for file in file_pointer.readlines():
        ip = file.split(" ")[0]
        error = file.split(" ")[8]
        if error == "\"-\"":
            error = file.split(" ")[6]
        addData(data, ip, error)
print(data)

with open("data.json", "w") as json_file_pointer:
  json.dump(data, json_file_pointer, indent=4)