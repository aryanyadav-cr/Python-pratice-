#Lists
'''
Lists = [1,2,3,5,6,7,8]
print(Lists)
print(type(Lists))
print(Lists[4])

student = ["aryan",56,"Delhi"]
print(student)
print(student[0])
print(len(student))
'''

#lists slicing
'''
marks = [1,2,3,4,5,7,6]
print(marks[1:4])
print(marks[1:9])
print(marks[1:])
print(marks[:3])

print(len(marks[:3]))

print(marks[-3:])
'''

#lists methods
marks = [1,2,55,43,59,777,6]
'''
marks.append(77)
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)

marks.insert(1,69)
print(marks)

marks.remove(1)
print(marks)
marks.pop(1)
print(marks)
'''
#Tuples

tup = (3,45,5,86,7,8,44)
'''
print(type(tup),tup)
print(tup[1])

print(tup)
print(tup.index(3))
print(tup.count(5))
print(tup[1:2])
'''
#pratice questions
#1WAP to check the user to enter names of their 3 favorite movies and share them in a list
'''
tpp=[]
for i in range (1,4):
    t=input("enter your fav movie : ")
    tpp.append(t)
print(tpp)
'''
#2 WAP to check if a list contains a palindrome of elements 
'''
li = []
print("______Enter three number______")
for i in range(1,4):
    t=int(input("enter the number : "))
    li.append(t)
print(type(li))
cpo1 = li.copy()
cpo1.reverse()

if li==cpo1:
    print("this is a palindrome list")
else:
    print("not  Palindrome list")
'''
#3 WAP tp count the number of students with the A grade in the following tuple
tup = ("C","D","B","A","A","B","C",)

print(tup.count("A"))
