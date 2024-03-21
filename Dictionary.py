#Name: Hridaya Bhattarai

#Part 1
#1. Create three dictionaries:
'''
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
'''
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

#(a) Write code to concatenate these dictionaries to create a new one. Create a variable called nums to store the resulting dictionary.
#There are multiple ways to do this,however, one of the easiest is to convert each of the dictionaries items to a list (which can be added together)
#and pass them to the dict() constructor.

dic = {}
dic.update(dic1)
print(dic)
dic.update(dic2)
print(dic)
dic.update(dic3)
print(dic)

#(b) Write code to add a new key/value pair to the dictionary nums: (7, 70)

dic[7] = 70
print(dic)

#(c) Write code to update the value of the item with key 3 in nums to 80

dic[3] = 80
print(dic)

#(d) Write code to remove the third item from dictionary nums.

del dic[3]
print(dic)

#(e) Write code to sum all the items in the dictionary nums

values = dic.values()
total = sum(values)
print(total)

#(f) Write code to multiply all the items in the dictionary nums
my_dict = {'data1':15,'data2':-5,'data3':20}
result=1
for key in my_dict:    
    result=result * my_dict[key]

print(result)



#2. Create two sets:
#set1 = {20, 40, 60}
#set2 = {10, 20, 30, 40, 50, 60}

set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

#(a) Write code to perform a union of these sets. Print the length of the resulting set.

print(set1 | set2)

#(b) Write code to perform an intersection of set1 and set2.

print(set1 & set2)

#(c) Write code to compute the symmetric difference between set1 and set2

print(set1 - set2)

#(d) Write code to add the value 40 to set1, did the set change?
set1.add(40)
print (set1)

#(e) Write code to remove value 20 from set2
sets.discards(20)
print (sets)

#Part 2
#1. Create a dictionary named password_lookup that contains usernames as keys and passwords as associated string values. Make up data for five entries.
password_lookup = {"hridaya":"hridaya123"}

print("Sign up \n")

name = str(input("Please enter your preferred username.\n"))

passcode = str(input("Thank you, now enter a password as well.\n"))

password_lookup[name] = passcode

print(password_lookup)    

    
#2. Write a program that creates an initially empty dictionary named password_lookup, prompting one-by-one for usernames and passwords
#(until a username of 'z' is read) entering each into the dictionary.

password_lookup = {}
name = input("Enter username:")
while name !='z':
    pwd = input("Enter your password:")
    password_lookup[name] = pwd
    name = input("Enter username:")

print(password_lookup)

#3. Create a dictionary named password_hint that contains email addresses as keys, and associated values that contain both the users’
#“password security question,” and the answer to the question. Make up data for dictionary entries.

#4. Create a dictionary named member_table that contains users’ email addresses as keys, and answers to their password hints as the associated values,
#and a function that generates a temporary new password and stored in the table.

#5. Declare a set named vowels containing the strings 'a','e','i','o','u'. Create a function called count_vowels that prompts the user for any
#English word and displays how many vowels it contains.

vowels = {'a','e','i','o','u'}
def count_vowels():
    name = input('Enter any word')
    vow_lst = [x for x in name if x in vowels]
    print(len(vow_lst))
count_vowles()

#6. Create a function called word_intersection that prompts the user for two English words, and displays which letters the two words have in common.
#Convert each string to a set type in order to solve this problem.
from collections import Counter 
  
def word_intersection(str1,str2): 
    dict1 = Counter(str1) 
    dict2 = Counter(str2) 

    commonDict = dict1 & dict2 
  
    if len(commonDict) == 0: 
        print (-1)
        return

    commonChars = list(commonDict.elements()) 

    commonChars = sorted(commonChars) 

    print (''.join(commonChars)) 
  

word_intersection('hello','Hridayab') 

#7. Create a function called word_difference that prompts the user for two English words, and displays which letters are in the first word but not the
#second. Convert each string to a set type in order to solve this.
def word_difference(a,b):
    setA = set(a)

    setB = set(b)

    result = setA-setB

    print(result)

word_difference('hridaya', 'test')

#8. Create a function called get_missing_letters that prompts the user for two English words, and displays which letters of the alphabet are in neither of
#the two words. Convert each string to a set type in order to solve this.
def get_missing_letters():
    a = input("Enter a text:\n")
    b = input("Enter a second text:\n")
  

    e = list(set(a) ^ set(b))

    print("The letters are:")
    for i in e:
        print(i)

get_missing_letters()

#9. Create a function called word_sdifference that prompts the user for two English words, and displays which letters are in either the first word or the
#second word, but not both words. Convert each string to a set type in order to solve this.
def word_sdifference():
    a = input("Enter a text:\n")
    b = input("Enter a second text:\n")
  

    e = list(set(a) - set(b))

    print("The letters are:")
    for i in e:
        print(i)

word_sdifference()
