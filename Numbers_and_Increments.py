'''
ESYST-131 IoT - Python Programming - Numbers and Increments
I. Romero
Goal: To print the numbers in the list, Ask the users for their number and tell them what operation will be used, Then print each element in the list with its modified value
variables: numAndInc - The list to hold these number 
decVal - Holding Variable for modified variables
'''
#Make new List
numbers = [5, 17, 22, 32, 44]


#print the list
print(numbers)

#Ask user for input and tell them you are going to decrease the numbers
decVal = (int(input("How much would you like to decrease the number? ")))

#Modify each element in the list
for num in numbers:
    num -= decVal
    print(num)

#Print each element
#print(newList0[0])
