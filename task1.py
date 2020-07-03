"""
from sys import argv
NameOfProgram, NameOfFile=argv
print('Name Of Program')
print('Nmae of Fie')
while True:
    fh=open(NameOfFile)
    content=fh.read()
    print(content)
    fh.close()
    break
print('We successfully achieved it')


#weekend 1.7
str = input('Enter String: ') #initial string
reversed=''.join(reversed(str)) 
print(reversed) #print the reversed string
for vowel in 'aeiouAEIOU':
    if vowel in reversed:
        print(vowel)

#weekend 1.8

def printWords(s): 
	
	# split the string 
	s = s.split(' ') 
	
	# iterate in words of string 
	for word in s: 
		
		# if length is even 
		if len(word)%2==0: 
			print(word) 

s = "hello my name is Kinjan Shah"
printWords(s) 


#weekend 1.9
"""
"""
def divis(l=[]):
    for i in range(len(l)):
        if l[i]%5==0:
           print(l[i])
divis([1,2,5,25,50,45,55,67,75.98,100])

l=[1,2,5,25,50,45,55,67,75.98,100]
res=filter(lambda x:(x%5==0),l)
print(list(res))

import functools
res= functools.reduce(lambda x,y:x+y, [1,2,3,4,5])
print(res)

try:
    a=10
    b= '5'
    print(a+b)
except TypeError:
    print('You have entered the wrong value. Please recheck it') 
""" 
"""
try:
    print('Try Block')
    a=int(input('Enter value of a: '))
    b=int(input('Enter value of b: '))
    res=a/b
    print(res)
except ZeroDivisionError:
    print('Division by zero is not acceptable')
else:
    print("If try is working fine, I'll be working fine")
finally:
    print('This will be printed anyway')
    

x= open('test1.txt', 'w')
print(x.readlines())
x.close()
"""    """
fh=open('test1.txt', 'a')
fh.write('Hey, I am new to this file\n')
"""
"""
from sys import argv
NameOfProgram,NameofFile=argv
print('Name of Program')
print('Name of File')
while True:
    try:
        fh=open(NameofFile)
        content=fh.read()
        print(content)
        fh.close()
        break
    except:
        print('The name of the file you have given is incorect')
        try_again=input('Do you want to try again? (Y/N) ')
        if try_again=='Y' or try_again=='y':
            NameofFile=input('Please Enter the Name of the file you are lookinf for')
            continue
        else:
            break
print('We have successfully achieved it')
""" """
import json
p = '{"name": "Kinjan", "Surname": ["Shah", "Jain"]}'
res=json.loads(p) 
print(json.dumps(res, indent=4, sort_keys=True))
"""  """
import json
demo={1:'a', 2:'r', 3:'e', 4:'t', 5:'o'}
res=json.dumps(demo)
print(json.dumps(demo, indent=4, sort_keys=True))
"""
#res=[letter for letter in 'consultadd']
#print(res)
"""
sq=[]
for i in range(10):
    sq.append(i**2)
print(sq) """
"""res=[i**2 for i in range(10)]
print(res)"""
"""res=[i for i in range(20) if i%5==0]
print(res)"""

"""res=[(i*j) for i in range(2) for j in range(5)]
print(res)"""
"""for i in range(2):
    for j in range(5):
        print(i*j)"""
"""d={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
d_comp={k:v*2 for (k,v) in d.items()}
print(d_comp)"""
"""d={'a':1, 'b':2,'c':3, 'd':4, 'e':5 }
d_comp= {k:v*2 for (k,v) in d.items() if v>4}
print(d_comp)"""
"""d={}
num=range(10)
for i in num:
    if i%3==0:
        d[i]=i*3
print(d)"""
"""
def demo_gen():
    n=1
    print('This is line no 1')
    yield(n)
    n=n+1
    print('This is line no 2')
    yield(n)
    n=n+1
    print('This is line no 3')
    yield(n)
    n=n+1
    print('This is line no 4')
    yield(n)
    n=n+1
    print('This is line no 5')
    yield(n)
    n=n+1
    print('This is line no 6')
    yield(n)
Res=demo_gen()
for i in Res:
    print(i)
""" """
def deco(function):
    def inner():
        print('The inner function will be executing')
        function()
        print('After deco function you want it to be executed')
    return(inner)
def need_of_deco():
    print('I am a decorator function')
res=deco(need_of_deco())
print(res) 
""" """
from itertools import zip_longest
x=[1,2,3,4,5,6,7]
y=['a','b','c','d','e','f']
for i,j in zip_longest(x,y):
    print (i,j)
    print ('Number: ', i)
    print ('Alpha: ', j) """
"""class Training:
    domain='Python'
    day='Saturday'
    def demo(self):
        print('The domain of the training is: ',self.domain)
        print('The day of the training os :',self.day)

consultadd=Training()
consultadd.demo()"""
"""
class candidate:
    def _init_(self, name, add):
        self.name=name
        self.add=add
    def printing(self):
        print('Hello my name is :',self.name)
        print('Hello my address is :', self.add)
x=candidate('Kinjan', 'NJ')
x.printing()"""
"""
print('I will always pop up here')
def demo():
    print(__name__)
demo()"""
"""#weekend 1.10
#Create two different lists as in even_list and odd_list
total1=total2=0
even=[]
odd=[]
n = int(input("Enter number of elements in range 1-50 : "))
for i in range(0,n):
    element = int(input())
    if element <=50:
        if i%2==0:
            even.append(element)
        if i%2!=0:
            odd.append(element)
print('Even_List: ',even)
print('Odd_List: ',odd)
for ele in range(0, len(even)):
    total1 = total1 + even[ele]
print("Sum of all elements in even list: ", total1)
for ele in range(0, len(odd)):
    total2 = total2 + odd[ele]
print("Sum of all elements in odd list: ", total2)
"""  """
def countOccurences(str, char): 
       
    a = str.split() 
  
    
    count = 0
    for i in range(0, len(a)): 
          
        # if match found increase count  
        if (char == a[i]): 
           count = count + 1
             
    return count        
  
# Driver code 
str ="12abcbacbaba344ab"
char ="a"
print(countOccurences(str, char)) 
"""
"""#weekend 1.12 
t1=(1,2,3,4,5,6,7,8,9,10)
li=[]
t2=()
for i in t1:
    if i%2==0:
        li.append(i)
        t2=tuple(li)
print(t2)
"""
"""
#Task4.1
def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

# given string
mystr = "1234abcd"
print("Given String: ", mystr)

# reversed string
print("Reversed String: ", reverse(mystr))
"""  """
#Task4.2
def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (u,l))
up_low("kinjan Is SHAH")   """
"""
#Task4.3
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,1,2,3,3,3,3,4,4,5])) """
"""
#Task4.4
items=[n for n in input('Enter words in - seperated form: ').split('-')]
items.sort()
print('-'.join(items))]
"""  """
#Task4.5
lines = []
while True:
    l = input('Enter sequence of lines: ')
    if l:
        lines.append(l.upper())
    else:
        break;
for l in lines:
    print(l)  """
"""#Task-4.6
def calculateSum (a,b):
	s = int(a) + int(b)
	return s

num1=input('Insert num1: ')
num2=input('Insert num2: ')
sum = calculateSum(num1,num2)

print('Sum:= ',sum)"""
"""
#Task4.7
def length_of_string(str1, str2):
	if (len(str1) == len(str2)):
		print(str1)
		#print("\n")
		print(str2)

	elif (len(str1) < len(str2)):
		print(str2)
	
	else:
		print(str1)

stri1 = input(str("enter First String: "))
stri2 = input(str("enter Second String: "))

print("\n")

length_of_string(stri1, stri2)  """

"""#Task4.8

def printValues():
    l = list()
    for i in range(1,21):
        l.append(i**2)
    print(l)
printValues()
"""
#Write a function called showNumbers that takes a parameter called limit. 
"""#Task4.9 
def showNumbers(limit):
    for i in range(0,limit +1):
        if i % 2 == 0:
            print(str(i) + ":" +'EVEN')
        else:
            print(str(i) + ":"+ 'ODD')
limit = int(input("Give me a number. "))
showNumbers(limit)
"""
"""#Task4.10
def printValues():
	l = list()
	for i in range(1,21):
            if i%2==0:
		l.append(i)
	print(l)
		
printValues()"""
"""
#Task4.11
li = [1,2,3,4,5,6,7,8,9,10]
eve_num = map(lambda x: x**2, filter(lambda   x: x%2==0, li))
print(eve_num) """

"""#Task4.12
try:
    a= input('Enter value of a: ')
    b= input('Enter value of b: ')
    print 'Division of a/b is: ',a/b
except ZeroDivisionError:
    print('You are trying to divide by zero')"""
"""
#Task4.13
from functools import reduce 
List1= [[1,2,3],[4,5],[6,7,8]] #into [1,2,3,4,5,6,7,8]
combiner= lambda x,y : x+y
joinlist= reduce(combiner, List1)
print(joinlist) """
"""
#Task4.14
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)
"""
"""
#Task4.15
def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')
    a()
"""
"""#Task5.1 Not divisible by 3 but multiple of 7
li = [1,2,3,4,5,6,7,8,9,10]
eve_num = map(lambda x: x, filter(lambda   x: x%3!=0 and x%7==0, li))
print(eve_num) """

""" #Task 5.2 
def multiplyList(myList):
# Multiply elements one by one 
    result = 1
    for x in myList: 
         result = result * x  
    return result  
list1=[1,2,3,4,10]
print(multiplyList(list1))  """

"""#Task5.3
test_str = "Jay Jinendra" 
print("The original string is : " + str(test_str)) 
 
res = [char for char in test_str if char.isupper()] 
  
print("The uppercase characters in string are : " + str(res)) """

"""#Task5.4 
Student = ["Smit", "Jaya", "Rayyan"]
capital = ['CSE', 'Networking', 'Operating System']

print ("Original key list is : " + str(Student)) 
print ("Original value list is : " + str(capital)) 
# to convert lists to dictionary 
res = {} 
for key in Student: 
	for value in capital: 
		res[key] = value 
		capital.remove(value) 
		break

# Printing resultant dictionary 
print ("Resultant dictionary is : " + str(res)) 
"""
#Task5.5
"""# generator to reverse a string
def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

# using for loop to reverse the string
for char in reverse_string("Consultadd Training"):
    print(char)
"""
"""#Task5.6
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
@make_bold
def hello():
    return "hello world"
print(hello()) """

"""#Task6.1
#raise SyntaxError("oops wrong syntex try correcting")
try:
    while True:
        print('Hello World')
        break
    ^
except SyntaxError:
    print('oops wrong syntax')
"""
"""
#task6.2
import os
filename = input("Enter file name: ")
 
try:
    f = open(filename, "r")
 
    for line in f:
        print(line, end="")
 
    f.close()
 
except FileNotFoundError:
    print("File not found")
 
except PermissionError:
    print("You don't have the permission to read the file")
 
except FileExistsError:
    print("You don't have the permission to read the file")
 
except:
    print("Unexpected error while reading the file")
 
else:
    print("Program ran without any problem") """ 

""" #task6.3
Number= input('Enter the number of four digits: ')
if len(Number)>4 or len(Number)<4 :
   print('Please length is too short/long !!! Please provide only four digits')

else:
    print('Entered 4 digit number is: ', Number) """
"""    
#Task 6.4
print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='shah' and username=='kinjan':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1  """
"""
#Task 6.6
fobj = open("test.txt")
for x in fobj:
    x= x.split(" ")
    for word in x:
        if len(word)%2==0:
            print(word)
"""

"""#Task7.1 
from math import sqrt
C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)

print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))  """

"""#Task7.2
class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self,length = 0):
        Shape.__init__(self)
        self.length = length

    def area(self):
        return self.length*self.length

Asqr = Square(5)
print(Asqr.area())      # prints 25 as given argument

print(Square().area())  # prints zero as default area
"""
"""#Task7.3
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
"""
"""#Task7.4.1    
class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
"""
"""
#7.4.2
class A:
    def __init__(self, x= 1):
        self.x = x
class der(A):
    def __init__(self,y = 2):
        super().__init__()
        self.y = y

def main():
    obj = der()
    print(obj.x, obj.y)
main()
"""
"""
#Task7.4.3
class A:
    def __init__(self,x):
        self.x = x
    def count(self,x):
        self.x = self.x+1
class B(A):
    def __init__(self, y=0):
        A.__init__(self, 3)
        self.y = y
    def count(self):
        self.y += 1     
def main():
    obj = B()
    obj.count()
    print(obj.x, obj.y)
main()
"""
"""#Task7.4.4
class A:
    def __init__(self):
        self.multiply(15)
        print(self.i)

def multiply(self, i):
    self.i = 4 * i;
class B(A):
    def __init__(self):
        super().__init__()
    
    def multiply(self, i):
        self.i = 2 * i;
obj = B()
""" 
"""#Task7.5
class Time():

    def __init__(self, hours, mins): 
        self.hours = hours
        self.mins = mins
    
    def addTime(t1,t2):
        t3 = Time(0,0)
        if t1.mins+t2.mins > 60:
            t3.hours= (t1.mins+t2.mins)/60
        t3.hours = t3.hours+t1.hours+t2.hours
        t3.mins = (t1.mins+t2.mins)-(((t1.mins+t2.mins)/60)*60)
        return t3

    def displayTime(self):
        print ("Time is",self.hours,"hours and",self.mins,"minutes.")

    def displayMinute(self):
        print (self.hours*60)+self.mins

a= Time(2,50)
b = Time(1,20)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
"""
#Task7.6
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.initialAge = age
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age <= 0:
            age is 0
            print("Age is not valid, setting age to 0")

        elif age < 13:
            print("You are young.")

        elif 13 <= age < 18:
            print("You are teenager.")

        else:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        return age+1
t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")