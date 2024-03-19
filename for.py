#We can navigate through arrays using the for loop.

#Easy Example
number=[12,69,23,20,5,19]
for x in number:
    print(x)


#Product number with range
    
for i in range(1,20):
    print(i)


#Write the String
    
for word in "Çekoslavakyalilastiramadiklarimizdanmisiniz":
    print(word)

#Work with dictionaries
dct={
    "Name":"Toyota",
    "Model":"Hilux",
    "Year":2020
}
for key,value in dct.items():
    print(key, ":" ,value)