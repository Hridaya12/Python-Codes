#NAME=Hridaya Bhattarai


   #PART 1
#The perimeter of a rectangle with length 9 &amp; width 7
Length=9
Width=7
perimeter=2*(Length+Width)
print(perimeter)


#Your name stored as a variable
Hridaya=(input('Enter the desired variable:' ))
print('Your stored variable is:', Hridaya)


#The maximum of 5, 2, -8, 9, 5.5, 7, and 0
list=[ 5, 2, -8, 9, 5.5, 7, 0 ]
print('The maximum value is:',max(list))

#Python is great, it’s wild!
print("Python is great, it's wild!")


#The difference between Beth’s age (57) and Tom’s (34)
Beth=57
Tom=34
print("The difference of the age of Beth and Tom is:",Beth-Tom )

#2 to the 10 th power
import math
x=math.pow(2,10)
print('2 to the 10 th power is:',x)

#7 factorial minus 5 factorial
import math
fact7 = math.factorial(7)
fact5 = math.factorial(5)
print('The value of  factorial of 7 minus  factorial of 5 is:', fact7 - fact5)

#Your forename multiplied by 5
Name=input('Enter your Forename:')
H=(Name * 5)
print(H)


#Your name left justified 15 spaces
import math
My_Name = input('Enter your name: ')
print(format(My_Name,'>15'))

#PI to 5 decimal places
import math
print("The value of PI is {:.5f}".format(math.pi))


#A variable with the name def that stores the number 7
def store(B):
    print(B)
store(7)


#200 modulus 12
print("200 modulus 12 is:",200%12)


#7.2 as an integer value
number=int(7.2)
print("interger value is :",number)


#The Unicode encoding for your name
print(ord('H'))
print(ord('R'))
print(ord('I'))
print(ord('D'))
print(ord('A'))
print(ord('Y'))
print(ord('A'))

#1. Give the following values in the exponential notation of Python, such that there is only one significant digit to the left of the decimal point.

#(a) 4580.5034
print(format(4580.5034,'.1e'))



#(b) 0.00000046004
print(format(0.00000046004,'.1e'))



#(c) 5000402.000000000006
print(format(5000402.000000000006,'.1e'))



#2. Regarding the built-in format function in Python
#(a) Use the format function to display the floating-point value in variable result with three decimal digits of precision.
print(format(12345000.987654,'.3f'))



#(b) Give a modified version of the format function in (a) so that commas are included in the displayed results.
print(format(12345000.987654,',.3f'))


#3. Give a call to print that is provided one string that displays the following address on three separate lines:
'''
John Doe
123 Dudley Street
Wolverhampton, West Midlands, WV1 4BF
'''
print('John Doe \n123 Dudley Street \nWolverhampton, West Minlands, WV1 4BF')

#4. Regarding variable assignment,
#(a) What is the value of the variable num after the following is executed?
'''
k = 5
num = 0
num1 = num + k * 2
num2 = num + k * 2 

'''
k=5
num=0
number1=num+k*2
number2=num+k*2
print("the value is",number1)
print("the values is",number2)


#(b) Are the values id(num1) and id(num2) equal after the last statement?
print("Are the values id(num1) and id(num2) equal after the last statement?");
print("Yes, They both are equal as formula for both the numbers are same")

#5. Regarding the built-in input function in Python:
#(a) Give an instruction that prompts a user for their last name and stores it in a variable named last_name.
Last_name = input('Enter your Last name: ')
print("Your last name is:" ,Last_name)


#(b) Give an instruction that prompts a user for their age and stores it as an integer in a variable named age.
Age = input('Enter your age:')
print("Your age is:",Age )

#(c) Give an instruction that prompts a user for their temperature and stores it as a float in a variable named current_temperature.
Current_Temperature = float(input('Enter the Current Temperature: '))
print("The current temperatuere is" ,Current_Temperature)



#Part 3
#(a) Write a Python program that prompts the user for two integer values and displays the results of the first number divided by the second,
#with exactly two decimal places displayed.
First_number = int(input('Enter First number: '))
Second_number = int(input('Enter Second number: '))
x=(First_number/Second_number)
print (format(x,'.2f'))

#(b) Write a Python program that prompts the user for two floating-point values and displays the results of the first number divided by the second,
#with exactly two decimal places displayed. 

First_number = float(input('Enter First number: '))
Second_number = float(input('Enter Second number: '))
x=(First_number/Second_number)
print (float(format(x,'.2f')))

#(c) Write a Python program that prompts the user for two floating-point values and displays the results of the first number divided by the second,
#with exactly two decimal places displayed in scientific notation. 

First_number = float(input('Enter First number: '))
Second_number = float(input('Enter Second number: '))
x=(First_number/Second_number)
print (format(x,'.2e'))


#(d) Write a Python program that prompts the user to enter a UTF-8 value between 32 and 126, and displays the corresponding character. 

value = int(input('Enter any UTF-8 value between 36 to 126: '))
print(chr(value))

#(e) Write a Python program that allows the user to enter two integer values, and displays the results with the following arithmetic operators
#applied to them. For example, if the user enters the values 7 and 5, the output would be:
'''
Addition: 7 + 5 = 12
Subtraction: 7 – 5 = 2
Multiplication: 7 * 5 = 35
Division: 7 / 5 = 1.40
Truncated Division: 7 // 5 = 1
Modulus: 7 % 5 = 2
Exponentiation: 7 ** 5 = 16,807
'''
First_number=float(input("Enter First number: "))
Second_number=float(input("Enter Second number: "))
print('Addition:', First_number + Second_number)
print('Subtraction:', First_number - Second_number)
print('Multiplication:', First_number *  Second_number)
print('Division;', First_number / Second_number)
print('Truncated Division;', First_number//Second_number)
print('Modulus:', First_number % Second_number)
print('Exponentiation:', First_number ** Second_number)

#(f) All floating-point results should be displayed with two decimal places of accuracy and with commas where appropriate.
First_number=float(input("Enter First number: "))
Second_number=float(input("Enter Second number: "))
print("Addition:{:.2f}".format(First_number+Second_number))
print("Substraction:{:.2f}".format(First_number-Second_number))
print("Multiplication:{:.2f}".format(First_number*Second_number))
print("Division:{:.2f}".format (First_number / Second_number))
print("Truncated:{:.2f}".format (First_number // Second_number))
print("Modulus:{:.2f}".format(First_number%Second_number))
print("Exponentiation:{:.2f}".format(First_number**Second_number))


#(g) Write a version of the Python program for question 5 above that performs all calculations using floating-point values,
#regardless of whether the user enters floating-point values or not using explicit type conversion.
First_number=float(input("Enter First number: "))
Second_number=float(input("Enter Second number: "))
print("Addition:{:.2f}".format(First_number+Second_number))
print("Substraction:{:.2f}".format(First_number-Second_number))
print("Multiplication:{:.2f}".format(First_number*Second_number))
print("Division:{:.2f}".format (First_number / Second_number))
print("Truncated:{:.2f}".format (First_number // Second_number))
print("Modulus:{:.2f}".format(First_number%Second_number))
print("Exponentiation:{:.2f}".format(First_number**Second_number))


#Part 4

print('Welcome to Time Converter')
Time_Second = int(input('Enter  time in Second:'))
Hour= (Time_Second//3600)
minute = (Time_Second)//60-Hour*60
second = Time_Second%60
print(Time_Second,"seconds is:",Hour,"Hours",minute,"Minutes",second,"Seconds")


