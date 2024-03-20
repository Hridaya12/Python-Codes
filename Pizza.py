#Name= Hridaya Bhattarai
#Student ID= 2065693


'''
Question 1
A) Write a program to evenly divide pizzas.

Prompt the user to enter:

The number of people
The number of pizzas ordered
The number of slices per pizza
Ensure that the number of pieces comes out even. Display the number of slices of pizza each person should get. If there are leftovers, show the number of leftover slices.
'''


#Question ans 1
def hridaya():
    number=int(input("Enter the number of people:\n"))
    pizza=int(input("Enter the number of pizza:\n"))
    slices=int(input("Enter the slice per pizza:\n"))
    perslice=pizza*slices//number
    perpeople=pizza*slices%number
    print(f"Each person gets{perslice} slices")
    print(f"There are {perpeople} leftover slices of pizza")
hridaya()



'''
Question 2
B) Revise the program to ensure that inputs are entered as numeric values.
The user should be prompted repeatedly until they enter a numeric value for each of the three inputs.
You will need to make use of a loop and explicit type conversion.
'''

#question 2 ans



def hridaya():    
    try:
        number=int(input("enter number of people \n"))
        pizza= int(input("enter number of pizza \n"))
        slices=int(input("enter number of slices per person \n"))
        perslice=pizza*slices//number
        perpeople=pizza*slices%number
        print(f"Each person gets {perslice} pizza")
        print(f"There are {perpeople} leftover slices of pizza")
    except:
        print("Invalid entry! You must enter a numeric value...\n")
        hridaya()
hridaya()




'''
C) Create a second version of the program that prompts users to select a pizza size instead of entering the number of slices.
Your program should offer users the following sizes to choose from:
'''


#question 3 ans

def hridaya():
    try:
        number=int(input("Enter the number of people:\n"))
        pizza=int(input("Enter the number of pizza:\n"))
        slices=input("Choose slice of pizza :\nsmall(4) medium(8) large(12) \n")
        if slices=='small':
            pz=4
        elif slices=='medium':
            pz=8
        elif slices=='large':
            pz=12
        perslice=pizza*pz//number
        perpeople=pizza*pz%number
        print(f"Each person get {perslice} slices")
        print(f"There are {perpeople} leftover slices of pizza")
    except:
        print("Invalid Entry! You must enter a numeric value....\n")
        hridaya()    
hridaya()

