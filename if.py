#User Control
# username="admin"
# password="1923"

# input_user=input("Please Enter Your Username")
# input_password=input("Please enter your password")

# if input_user == username and input_password == password:
#     print("Welcome the application")

# else:
#     print("Please try again")


#Driving Licence Control


name=input("Please Enter Your Name:")
vehicles=input("What kind of Vehicles Licence Do you want the Get:")



age=int(input("Please Enter Your Age"))

if vehicles == "Automobil" and age>=18:
    print("You can get the automobil licence")

else:
    print("You can not get the automobil licence")

if vehicles == "Truck" and age>21:
    print("You can get the Truck licence")

else:
    print("Your age is not suitable for truck")

if vehicles == "Motorcycle" and age>=17:
    print("You can get the motorcycle")