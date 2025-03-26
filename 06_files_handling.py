### Files Handlig ###
import os

# .txt file

# txt_file = open("my_file.txt","w+") # Leer y Escribir
# txt_file.write("Mi nombre es Jose\nMi apellido es Casanueva\n42 años\nY mi lenguaje favor es Python\nAunque tambien me gusta PHP")
# txt_file.write("\nAunque tambien me gusta PHP")
# print(txt_file.readline())
# txt_file.close()
# os.remove("my_file.txt")


#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readline())
#print(txt_file.readlines())
# for line in txt_file.readlines():
#     print(line)

# txt_file.write("\nAunque tambien me gusta PHP")
# print(txt_file.readlines())

#.json 

import json

json_file = open("my_file.json", "r+")
json_text = {
    "name":"Bruno",
    "surname":"Casanueva",
    "age":"8",
    "languages": ["CatCode", "DogCode","Python"],
    "website": "brucethecat.com"}

json.dump(json_text,json_file,indent=2)
json_file.close()
# json.dump(json_text,json_file,indent=2)

# with open("my_file.json") as jaison:
#     for line in jaison.readlines():
#         print(line)
        
json_dict = json.load(open("my_file.json"));
print(type(json_dict))
print(json_dict["name"])


#csv file
import csv
son_text = {
    "name":"Bruno",
    "surname":"Casanueva",
    "age":"8",
    "languages": ["CatCode", "DogCode","Python"],
    "website": "brucethecat.com"}

csv_file = open('csv_file.csv', "+w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname","age","language","website"])
csv_writer.writerow(["Bruno","Casanueva",8,"CatCode","brucethecat.com"])
csv_writer.writerow(["Oso","Casanueva",3,"DogCode","OzzyOsburne.com"])
csv_file.close()

with open("csv_file.csv") as jaison:
    for line in jaison.readlines():
        print(line)

#xlsx file
# import xlsrd  debe instalarse el modulo


#xml file
# import xml













