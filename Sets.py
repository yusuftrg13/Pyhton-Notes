#In Python, a set is a data structure that contains a collection of unique elements. Each item can only be found once in sets. Sets are not sorted and do not contain any specific order between items

myset={10,10,20,20,30,40,50}

print(myset) #Out:10,20,30
myset.add(40) #Add the 40
myset.remove(30) #Remove the 30
myset.discard(50) #Remove the 50


set_one={5,6,7,8,9}
set_two={10,11,12,13,8}

union=set_one |  set_two
intersecction = set_one & set_two
difference= set_one - set_two

print(union) #Out:5,6,7,8,9,10,11,12
print(intersecction) #Out:8
print(difference) #Out:5
