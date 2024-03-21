#Student Name= Hridaya Bhattarai



#part 1
#Select: Start > All Programs > IDLE (Python GUI)
#Evaluate the following Boolean expressions in IDLE:
'''
7 and 5
5

True and True
True


True and False or True
True

False or False and True
False

False or 0
0

not (False) and True
True

not (True or not (False and False))
False

(10 > 14) and (4 == 5)
False

True and 5
5

(3 * 4) != (14 - 2) or ('C' >= 'D')
False

(12 * 2) == (3 * 8)
True

14 * 2) != (3 * 8)
True


#part 2

#1. Evaluate the following expressions for num1 = 10 and num2 = 20.

a)not (num1 < 1) and num2 < 10
not(10<1) and 20<10
False
b)not (num1 < 1) and num2 < 10 or num1 + num3 < 100
not(10<1) and 20<10 or 10 + num3 < 100
NameError: name 'num3' is not defined
c)not (num2 > 1) or num1 > num2 - 10
not (20 > 1) or 10 > 20 - 10
False
'''


#2 Give an appropriate if statement for each of the following(the value of num is not important):
#(a) Displays 'within range' if num is between 0 and 100, inclusive.

number=int(input("enter any number:"))
if (number >=0) and (number <=100):
    print ("within range")
        
     
    
#(b) Displays 'within range' if num is between 0 and 100, inclusive, and displays 'out of range' otherwise.

number=int(input("enter any number:"))
if (number >=0) and (number <=100):
    print ("within range")
else: 
    print("out of range")



#3 Rewrite the following if-else statements using a single if statement and elif:
'''
if temperature >= 85 and humidity > 60:
print ('muggy day today')
else:
if temperature >= 85:
print ('warm, but not muggy today')
else:
if temperature >= 65:
print ('pleasant today')
else:
if temperature <= 45:
print ('cold today')
else:
print ('cool today')
'''


humidity=float(input("enter humidity"))
temperature=float(input("enter current temperature"))
if(temperature >=85) and (temperature>60):
    print("muggy day today")
elif (temperature >= 85):
    print("warm,but not muggy today")
elif(temperature >= 65):
    print("pleasant today")
elif (temperature <= 45):
    print ("cold today")
else:
    print("cool today")






#4. Write a Python program in which:
#(a) The user enters either 'A', 'B', or 'C'. If 'A' is entered, theprogram should display the word 'Apple'; if 'B' is entered, it displays 'Banana'; and if 'C' is entered, it displays 'Coconut'. Use nested if statements for this.

fruit=input("enter any letter")
if fruit=="A":
        print("Apple")
else:
    if fruit=="B":
        print("Banana")
    if fruit=="C":
        print("coconut")



#b Repeat question (a) using an if statement with elif headers instead.        


fruit=input("enter any letter")
if fruit=="A":
        print("Apple")
elif fruit=="B":
        print("Banana")
elif fruit=="C":
        print("coconut")
else:
        print("invalid entry")




#(c) A student enters the number of college credits earned. If the number of credits is greater than or equal to 90, 'Senior Status' is displayed; if greater than or equal to 60, 'Junior Status' is displayed; if greater than or equal to 30, 'Sophomore Status' is displayed; else, 'Freshman Status' is displayed.


 
credit=float(input('enter your college credit'))
if (credit>=90):
    print("senior status")
elif(credit>=60):
    print("junior status")
elif (credit>=30):
    print("sophomore stauts")
else:
    print("freshman status")


#(e) The user enters a number. If the number is divisible by 3, the word ‘Fizz’ should be displayed; if the number is divisible by 5 the word ‘Buzz’ should be displayed and if the number is divisible by both ‘FizzBuzz’ should be displayed.


number=int(input("enter any number:"))
if (number % 3==0) and (number % 5==0):
    print("fizzbuzz")
elif (number % 3==0):
    print("fizz")
elif (number % 5==0):
    print("buzz")
elif (number % 3==0) and (number % 5==0):
    print("fizzbuzz")




#Part 3

# (a) Uses a loop to add up all the even numbers between 100 and 200, inclusive

total = 0
for number in range(100,200+1):
        if(number % 2 == 0):
            total = total + number
print("The Sum of Even Numbers from 100 to 200 is",total)            


#(b) Sums a series of (positive) integers entered by the user, excluding all numbers that are greater than 100.
total=0
num=int(input("enter any number"))
for num1 in range(0,num+1):        
    total=total+num1
    if num1>=100:
        break
    else:
        continue
print("sum of numbers are",total)


#2. The following while loop is meant to multiply a series of integers input by the user, until a sentinel value of 0 is entered. Indicate any errors in the code given. See if you can fix the program and get it running.


product=1
num=int(input('enter first number:'))
while num !=0:
    product=product*num
    print('product=',product)
    num=num+1











