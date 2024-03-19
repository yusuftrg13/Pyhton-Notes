#Easy Example
def sayhello():
    print("Hello Welcome To Pyhton")

sayhello()

#Add The Number
def add(a,b):
    return a+b

result=add(5,8)
print(result) #Out=13


#Factorial 

def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)

number=4
print("Factorial:",factorial(number)) 


    
#WORKİNG FUNCTİON

def calculate_price(product1,product2):
    total_price=product1+product2
    return total_price

def discount(total_price):
    if total_price > 500:
        discount_price=total_price*0.85
    else:
        discount_price=total_price
    return discount_price

product1 = float(input("Please enter the product1 price: "))
product2 = float(input("Please enter the product2 price: "))

total_price=calculate_price(product1,product2)
discount_pricee = discount(total_price)

print("Total Price:", total_price)
print("Discount Price:", discount_pricee)