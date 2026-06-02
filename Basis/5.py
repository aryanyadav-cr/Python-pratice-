#While loop example
'''
i=1
while i<=5:
    print(i)
    i+=1

#to print hello 5 times
i=1
while i<=5:
    print("Hello")
    i+=1

#1 Print 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#2Print 100 to 1
i=100
while i>=1:
    print(i)
    i-=1

#3print multiplication table of a number   
i=1
n=2
while i<=10:
    print(i*n)
    i+=1

#4print the list using loop
n=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(n):
    print(n[i])
    i+=1

#5 search for a number x in tuple using loop
tup = (1,4,56,3,7,22,55,88,78)

n = int(input("enter a number : "))
i=0
while i<len(tup):
    if tup[i]==n:
        print("search number is found in that index: ", i)
        break
    i+=1
else:
    print("element was not found")

# For break and continue
for i in range(1, 11):
    if i == 5:
        #break
        continue
    print(i)
'''
#loops in python
#for loop 
list = [1,2,3,4] 
'''
for el in list:
    print(el)

for el in list:
    print(el)
else:
    print("End")

#1print the list using for loop
n=[1,4,9,16,25,36,49,64,81,100]

for el in n:
    print(el)

#2 search for a number x in tuple using loop
tup = (1,4,56,3,7,22,55,88,78)

n = int(input("enter a number : "))
i=0
for i in range(len(tup)):
    if tup[i]==n:
        print("index value",i)
        break
else:
    print("element was not found")


#Range EX
for el in range(11):
    print(el)

for el in range(1 , 22):
    print(el)

for el in range(1 , 11 , 2):
    print(el)

#Pass statement
for el in range(1 , 11):
    pass

#last question 
i=1
sum =0
while i<=10:
    sum = sum+i
    i+=1
    print(sum)
'''
#factorial of n number
n = 5
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)