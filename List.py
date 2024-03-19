#Right now I gonna try the make a list

myCar=["Ford","Toyota","Wolsvagen","Skoda"]

print(myCar)

#Show to how  many long the list
print(len(myCar))

#List items can be anything type look down:
list_number=[5,9,6,1,7,5,3]
list_true=[True,False,True]
list_random=["abc",15,True]

#How to Access List Items look at see

mycar=["Skoda","Toyota","Ford","Fiat","BMW"]
print(mycar[2])  #Out:Ford
print(mycar[-1]) #Negative İndex-Out:Fiat
print(mycar[1:3]) #Get from Skoda to Ford
print(mycar[:3]) #Get from Skoda to Fiat

#Change the Items
mycar[0]="Haci Murat"
mycar.insert(2,"MG")

#Append Items
mycar.append("Audi")

#Remove Items
mycar.remove("Ford")

#Pop Items
mycar.pop(1)

#Use the for function 
for x in mycar:
    print(x)

#Use the sort 
mycar.sort()
print(mycar)

#Use the reverse
mycar.reverse()

#Clear the List
mycar.clear()

print(mycar)