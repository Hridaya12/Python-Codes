#1.Write a Python program that prompts the user for a series of integers and stores in a list only the values between 1-100, and displays the resulting list.

'''
lst=[]
running=True
while running:
    num=int(input("enter any num:"))
    if num==200:
        running=False
    if num>0 and num<100:
        lst.append(num)
print(lst)
'''



#3. Write a Python program that prompts the user to enter a list of names and stores them in a list. The program should display how many times the letter 'a' appears within the list.




lst=[]
count=0
running = True
while running:
    x=input('Enter a name:')
    lst.append(x)
    yes=input('you want to enter another value(yes or no):\n')
    if yes=='no':
        running =False
    a=x.count('a')
    count=count+a
print(' letter a appears in',count,'times')


#4

def hridaya():
    lst=[]
    running = True
    while running:
        name = input('Enter sequence of words')
        name2=input("If u wanna end program enter end or press enter:\n")
        if name2 == 'end':
            running = False
        lst.append(name)
        lst.sort()
    print(lst)
hridaya() 

#5. Write a Python program that prompts the user to enter integer values to  populate two lists, then print messages to determine the following:
'''
(a) Whether the lists are of the same length.
(b) Whether the elements in each list sum to the same value.
(c) Whether there are any values that occur in both lists.
'''

lst1 = [1, 2, 9, 6, 5]
lst2 = [7, 5, 8, 3, 4]
lst3=[]


if len(lst2)==len(lst1):
    print('Both list are of same length')

if sum(lst1)==sum(lst2):
    print('sum are same')
else:
    print('sum are different')
for i in lst1:
    if i in lst2:
        lst3.append(i)
print(lst3)


#7
lst=[]
def moderate_days(dic_temp):
    for key,value in dic_temp.items():
        if value>70 and value<79:
            lst.append(key)
    print(lst)

d={'sun':75,'mon':80,'tue':72,'wed':77,'thu':90,'fri':65,'sat':74}
moderate_days(d)


#####
lst=[]
def moderate_days(dic_temp):
    sum=0
    for value in dic_temp.values():
        sum=sum+value
    print(sum/len(dic_temp))

d={'sun':75,'mon':80,'tue':72,'wed':77,'thu':90,'fri':65,'sat':74}
moderate_days(d)





