#my comment
print("Hello, im Python")

mystring = """multi
line 
string"""
print(mystring)

myBool = True

myList = [1,2,3]
myNestedList = [[1,2,3],[4,5,6]]
print(myNestedList[0])
print(myNestedList[0][2])

myDictionary = {"myKey1": "myValue1", "myKey2": "myValue2"}
print(myDictionary)
	
def print_number_check(x,y):
	if x>y:
		print("x larger " +str(y))
	elif x==y:
		print("x is " + str(y))
	else:
		print("x less than "+str(y))

compare = 0
compareTo = 3
while compare<5:
	print_number_check(compare,compareTo)
	
	compare+=1


for n in myNestedList:
	print(n)