first_dictionaries={
    "Brand":"Toyota",
    "Model":"Corolla",
    "Year":2019,
    "Colors":["red","white","blue"]
}
print(first_dictionaries)
#Get the Brand
print(first_dictionaries["Brand"])
#Get the Length
print(len(first_dictionaries))

#Access the Items
x=first_dictionaries["Model"]
print(x)

#Get Key
z=first_dictionaries.keys()
print(z)

#Change the Items
first_dictionaries["Model"]=2023

#Adding Items
first_dictionaries["MotorEngine"]=1.8

#Remove ıtems
first_dictionaries.pop("Colors")

print(first_dictionaries)