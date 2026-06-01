#Dictionary in python
'''
dict = {
    "name" : "aryan",
    "Roll no" : 21,
    "percentage" :78,
}
dict["marks"]=90
dict["name"]="etc"

print(dict["name"])
print()
print(dict["Roll no"])
print(dict["percentage"])
print(dict)'''
#Nested dictionaries
'''
students = {
    "name" : "aryan",
    "score":{
        "chem":89,
        "math":78,
         "phy":89,
    },
    "Roll no" : 21,
    "percentage" :78,
}
print(students)
print(students["score"])

students["score"]["math"] = 74
print(students)
'''
#Dict methods
'''
dict = {
    "name" : "aryan",
    "Roll no" : 21,
    "percentage" :78,
}

print(dict.keys())

print(dict.values())

print(dict.items())
print(dict.get("key"))
newdict = {
    "city": "Dehradun"
}

dict.update(newdict)

print(dict)
'''
#Set in python
num = {1,2,3,4}
num1 = {1,2,3,4,1,2,4,5}
print(type(num))
print(num1)

num2 = {}
print(num2)

#Set methods
set1 = {1,2,3,4}
set2 = {1,3,5,2,6,7}
'''
num.add(77)
num.remove(1)
num.clear()
num.pop()
print(num)

Result = set1.union(set2)
Result2 = set1.intersection(set2)
print(Result)
print(Result2)
'''
#Q1

subject= {
    "python", "java", "C++", "python", "javascript",
    "java", "python", "java", "C++", "C"
} 
print("number of classes to store : ", len(subject))

#Q2

dict = {}

for i in range(3):
    dict[i] = input("Enter the subject name : ")
print(dict)

values = {9, "9.0"}
print(values)