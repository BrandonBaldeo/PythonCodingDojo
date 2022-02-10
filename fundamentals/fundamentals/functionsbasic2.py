# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    arr=[]
    for i in range(num,-1,-1):
        arr.append(i)
    return arr
print(countdown(5))

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
newList=[1,2,3,4,5]
def PrintReturn(list):
    for i in range(0,len(list)):
        print(list[i])
PrintReturn(newList)
# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def FirstPlus(list):
    return list[0]+len(list)
print(FirstPlus(newList))
# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def GreaterSecond(list):
    count=0
    List=[]
    if(len(list)<2):
        return False
    for i in range(0,len(list)):
        if(list[i]>list[1]):
            List.append(list[i])
            count+=1
    return count, List

print(GreaterSecond([1]))
print(GreaterSecond([7,2,3,4,5,6]))

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def lenVal(length,value):
    newList=[]
    for i in range(0,length):
        newList.append(value)
    return newList
print(lenVal(10,5))