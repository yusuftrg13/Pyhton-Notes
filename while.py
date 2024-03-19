# i=1
# while i<20:
#     print(i)
#     i+=1
# else:
#     print("Loop Completed")

#Lets make the Example
i=1
while i<15:
    print(i)
    i +=1


#Put the limit and try while
Stop=int(input("Please enter the stop"))
i=1
while i <= Stop:
    if i %2==0:
        print(i)
    i +=1

#GET NAME AND PASSWORD FROM USER
username="John"
password="1486"

input_u=input("Please enter the name:")
input_p=input("Please enter the password:")

while input_u != username or input_p != password:
    print("Username or Password Wrong")
    input_u = input("Please enter the name: ")
    input_p = input("Please enter the password: ")

print("Everything is ok Carry on!")


