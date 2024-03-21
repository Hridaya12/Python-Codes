#NAME= Hridaya Bhattarai

#PART1

'''
def avg(n1,n2,n3):
    return (n1+n2+n3)/3

n1,n2,n3=37,108,67

#1.
result = avg(n1, n2, n3)
missning positional argument'n3'

#2.
avg(n1, n2, n3)
Blank

#3.
result = (n1+n2, n3+n4, n5+n6)
n4, n5, and n6 are not defined.

#4.
print(avg(n1, n2, n3))

#5.
result = avg(n1, n2, avg(n3, n4, n5))
n4 and n5 are not defined
'''


 #part2
  #A:types that prints a given value both as a float and an integer

def types():
    x = input('Enter a number:')
    print(float(x))
    print(int(x))
types()


#B: 
def squared():
    x=int(input("enter a number:"))
    return x**2
print(squared())

#C: int_to_string that takes an integer value and returns it as a string.

def int_to_string():
    variable= int(input('Enter a number:'))
    print(str(variable))
int_to_string()
               

#D: hello_world that takes a parameter name and displays the following output to the console: "Hello World, my name is name".
def hello_world():
    name= input("Enter your name:")
    print("Hello world!, My name is ", name)
hello_world()

#E: print_ast that takes an integer value n and a string value symbol, with a default value of "*". This character should be printed n times to the console.
def print_ast(a):
    return a*"*"
n=int(input('Enter any number:'))
print(print_ast(n))

#(F) improved_average that takes five integer parameters. It should return the mode, median and mean values of the numbers passed to the function.  
#from os import stat
import statistics
def improved_average(n):
    return(statistics.mean(n),
    statistics.mode(n),
    statistics.median(n))
    
n=[1,21,3,43,2]
print(improved_average(n))

#G either_side which when passed an integer value also prints the values which are one less and one more than that value e.g.
def either_side(a):
    low_number = a - 1
    high_number = a + 1
    print ("You typed",a,",one less than",a,"is",low_number,",one more",a,"is.",high_number)
a = int(input("Enter a number:"))
result = either_side(a)


#H  print_multiline_heading that takes two parameters: name and years. It should output the following message using a single print statement. Make sure that the indentation and spacing matches the example below.
'''
Dear Feline Fanatic,
Your cat has been arrested for:
1. Catnapping
2. Cat burglary
3. Extortion.
It will be sentenced to years in prison.
Sincerely, name
'''

def print_multiline_heading(name, year):
    print("Dear Feline Fanatic, \nYour cat has been arrested for: \n\n\t1.Catnapping \n\t2.Cat burglary \n\t3.Extortion \n\nIt will be sentenced to", year, "years in prison. \n\nSincerely,", name)
name = input("Enter a name: ")
year = input("Enter a year: ")
result = print_multiline_heading(name, year)


#Part3:
#1.Create a function that prompts the user for two integer values and displays the results of the first number divided by the second to two decimal places.
def hridaya():
    divide = number1/number2
    print ('Divide is {:.2f}'.format(divide))
number1 = int(input("Enter first number:"))
number2 = int(input("Enter  Second number:"))
result = hridaya()


#2. Create a Python program called calculator with functions to perform the following arithmetic calculations, each should take two decimal parameters and return the result of the arithmetic calculation in question.
#A: Addition
#B: Subtraction
#C: Multiplication
#D: Division
#E: Truncated division
#F: Modulus
#G: Exponentiation

#Addition
def Sum(x,y):

    return x + y

#Substraction
def Subtraction(x,y):

    return x - y


#Multiplication
def Multiplication(x,y):
  
    return x * y


#Division
def Division(x,y):
    
    return x / y


#Truncated Division
def Tdivsion(x,y):
    
    return x // y


#Modulus
def Modulus(x,y):

    return x % y



#Exponentation
def Exponentation(x,y):
 
    return (x * y)

x = float(input("Enter your First number: "))
y = float(input("Enter your Second number: "))
calc = input ("Enter the operation symbol:")

if calc == '+':
    print (Sum(x,y))
elif calc == '-':
    print (Subtraction(x,y))
elif calc == '*':
    print (Multiplication(x,y))
elif calc == '/':
    print (Division(x,y))
elif calc == '//':
    print (Tdivsion(x,y))
elif calc == '%':
    print (Modulus(x,y))
else:
    print (Exponentation(x,y))

#Part 4 Create a function multiplication_table. It should take a single parameter n, which determines the size of the grid to be output e.g.
def main():

    rows = int(input('Enter a number : '))
    counter = 0
    multiplicationTable(rows,counter)

def multiplicationTable(rows,counter):

    size = rows + 1

    for i in range (1,size):
        for nums in range (1,size):
            value = i*nums
            print(value,sep=' ',end="\t")
            counter += 1
            if counter%rows == 0:
                print()
            else:
                counter
main()
    
#2. Modify your existing function to take an additional parameter: power, with a default value of False. If a value of True is provided, your multiplication table should instead apply the top row as powers instead of multiplying the numbers.

def multiplication_table(n,power):
    i = 0 
    j = 1
    if power == "False":
        while i<= n:
            print(i, end = " ")        
            while j <= n:
                if i < 2 :
                 print(j, end = " ")
                else:
                    print(j*i, end = " ")
                j = j+1
            print('\n')
            j = 1
            i += 1
    elif power == "True":
        while i<= n:
            print(i, end = " ") 
            while j <= n:
                if i < 1:
                    print(j, end = " ")
                else:
                    print(i**j, end = " ")
                j = j + 1    
            print('\n')
            j = 1 
            i += 1    
    else:
        print('Error')
n= int(input('Enter the integer:'))
power=input("Enter True or False:")  
multiplication_table(n,power)
