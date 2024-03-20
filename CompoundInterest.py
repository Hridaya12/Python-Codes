# Coding Challenge 1, compound_interest.py
# Name:Hridaya Bhattarai
# Student No: 2065693

# Compound Interest Calculator

"""
Requirements:
    You will develop a program to calculate compound interest.

    • Print a welcome message explaining the purpose of the program.
    • Prompt the user for the necessary inputs (see formulae and brief)
    • Convert input values to suitable data types.
    • Perform compound interest calculation using the forumlae provided.
    • Print the result to the terminal using appropriate formatting.
    
    • Your program should be as close as possible to the example shown in the assessment brief.

Constraints:
    • Ensure that the interest rate is entered as a percentage and not a decimal.
    • Ensure that all monetary values are formatted to two decimal places.

Hints:
    • Think about what data types are the most appropriate for each input value.
    • Order of operations will be important, make sure you use parenthesis.
    • Review lecture two for more information on string formatting.
    • Your programs output should be as close as possible to the example in the assessment brief.
"""

# TODO: Write your code here!
#Code for Compound Interest Calculator
print("Welcome to the Hridaya Compound Interest Calculator.")
print("This program calculates your  returns if you invest with us")
input("Press Enter: to proceed further!")

#  taking Input

Principal= float(input("What is the principal amount ?:"))
Rate= float(input("What is the interest rate ?:"))
Time= float(input("Time period of investment? (in years):"))
Times_per_year=int(input("Your Interest times per year:"))

# use of formula

Compound_Interest=(Principal)*(1+Rate/(100*Times_per_year))**(Times_per_year*Time)

#print in .2f format
print("£",int(Principal),'invested at', Rate,'% for', Time,'years compounded', Times_per_year,'times per year is','£{:.2f}'.format(Compound_Interest))


#Extra code  continue
input("Press Enter: to proceed and use table interest calculator")

#extra code

print("Welcome to the Hridaya Compound Interest Calculator.")
print("This program calculates your  returns if you invest with us")
input("Press Enter: to proceed further!")

#  taking Input

Principal= float(input("What is the principal amount?:"))
Rate= float(input("What is the interest rate:"))
Time= float(input("Time period of investment (in years):"))
Times_per_year=int(input("Your Interest times per year:"))
Amount=Principal
New_Balance=0
#table Format code

print('Year', 'Peroid', 'Old_Balance', '   Interest', '    New_Balance')
for year in range( int(Time)):
    for x in range(Times_per_year):
         Old_Balance= Amount+New_Balance
         Amount= Old_Balance*(Rate/(100*Times_per_year))
         New_Balance= Old_Balance+Amount
         
         if x==0:
            print('  ',year+1,'     ',x+1,'  ','    £{:.2f}'.format(Old_Balance),'  ','   £{:.2f}'.format(Amount),'  ','     £{:.2f}'.format(New_Balance))
         else:     
            print('  ','        ',x+1,'  ','      £{:.2f}'.format(Old_Balance),'  ','   £{:.2f}'.format(Amount),'  ','    £{:.2f}'.format(New_Balance))
         Amount=0   
    Amount=0 


#print in .2f format
print("£",int(Principal),'invested at', Rate,'% for', Time,'years compounded', Times_per_year,'times per year is','£{:.2f}'.format(New_Balance))





