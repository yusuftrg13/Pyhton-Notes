#Lets create the Class

class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_information(self):
        print("Brand",self.brand)
        print("Model:",self.model)
        print("Year:",self.year)



#Create the Object

car1=Car("Toyota","Hilux","2022")
print(car1.brand) #Out=Toyota