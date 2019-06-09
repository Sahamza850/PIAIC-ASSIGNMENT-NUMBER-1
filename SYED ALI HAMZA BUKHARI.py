#!/usr/bin/env python
# coding: utf-8

# ## 1. Calculate Area of a Circle

#  Write a Python program which accepts the radius of a circle from the user and compute the area.
# Program Console Sample Output 1:
# ###### Input Radius: 0.5
# ###### Area of Circle with radius 0.5 is 0.7853981634

# In[2]:


from math import pi
r = float(input ("PLEASE INPUT THE RADIUS OF THE CIRCLE"))
print ("THE AREA OF THE CIRCLE WITH RADIUS " + str(r) + " is" + str(pi * r**2))


# In[ ]:





# In[ ]:





# ## 2. Check Number either positive, negative or zero

# #### Write a Python program to check if a number is positive, negative or zero
# ###### Program Console Sample Output 1:
# ###### Enter Number: -1
# ##### Negative Number Entered
# ###### Program Console Sample Output 2:
# ##### Integer: 3
# ##### Positive Number Entered
# ###### Program Console Sample Output 3:
# ##### Integer: 0
# ###### Zero Entered

# In[6]:


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# In[7]:


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# In[8]:


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")


# In[ ]:





# ## 3. Divisibility Check of two numbers

# #### Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# ##### Program Console Sample Output 1:
# ###### Enter numerator: 4
# ###### Enter Denominator: 2
# ##### Number 4 is Completely divisible by 2
# ###### Program Console Sample Output 2:
# ##### Enter numerator: 7
# 
# ##### Enter Denominator: 4
# ###### Number 7 is not Completely divisible by 4

# In[1]:


num1=int(input('Enter 1st Number: '))
num2=int(input('Enter 2nd Number: '))
if num1%num2==0:
    print('Number',num1,'is completely divisible by',num2)
else:
    print('Number',num1,'is not completely divisible by',num2)


# In[2]:


num1=int(input('Enter 1st Number: '))
num2=int(input('Enter 2nd Number: '))
if num1%num2==0:
    print('Number',num1,'is completely divisible by',num2)
else:
    print('Number',num1,'is not completely divisible by',num2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 4. Calculate Volume of a sphere

# ##### Write a Python program to get the volume of a sphere, please take the radius as input from user

# ##### Program Console Output:
# ##### Enter Radius of Sphere: 1
# ###### Volume of the Sphere with Radius 1 is 4.18

# In[3]:


from math import pi
r = float(input ("PLEASE INPUT THE RADIUS OF THE CIRCLE"))
V= 4.0/3.0*pi* r**3
print('The volume of the sphere is: ',V)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 5. Copy string n times
# #### Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# ##### Program Console Output:
# ##### Enter String: Hi
# ###### How many copies of String you need: 4
# ###### 4 Copies of Hi are HiHiHiHi

# In[5]:


string=input('Enter String: ')
copies=int(input('How many copies you need? '))
print(copies,'copies of' ,string, 'are',string*copies)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 6. Check if number is Even or Odd
# ### Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
# #### Program Console Output 1:
# ##### Enter Number: 4
# ###### 4 is Even
# #### Program Console Output 2:
# ##### Enter Number: 9
# ###### 9 is Odd

# In[4]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[5]:


num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")


# In[ ]:





# In[ ]:





# In[ ]:





# ## 7. Vowel Tester
# ### Write a Python program to test whether a passed letter is a vowel or not
# #### Program Console Output 1:
# ##### Enter a character: A
# ###### Letter A is Vowel
# #### Program Console Output 2:
# ##### Enter a character: e
# ###### Letter e is Vowel
# #### Program Console Output 2:
# ##### Enter a character: N
# ###### Letter N is not Vowel

# In[3]:


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
    print("%s is a vowel." % l)
elif l == 'v':
    print("Sometimes letter v stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l) 


# In[ ]:


l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
     print("%s is a vowel." % l)
elif l == 'v':
    print("Sometimes letter v stand for vowel, sometimes stand for consonant.")
else:
    print("%s is a consonant." % l) 


# In[ ]:





# In[ ]:





# ## 8. Triangle area
# ### Write a Python program that will accept the base and height of a triangle and compute the area
# ###### Reference:
# https://www.mathgoodies.com/lessons/vol1/area_triangle

# In[6]:


b = int(input("Input the base : "))
h = int(input("Input the height : "))
area = b*h/2
print("area = ", area)


# In[ ]:





# In[ ]:





# In[ ]:





# ## 9. Calculate Interest
# ### Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# #### Program Console Sample 1:
# ##### Please enter principal amount: 10000
# ###### Please Enter Rate of interest in %: 0.1
# ###### Enter number of years for investment: 5
# ###### After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1

# In[7]:


p_amount=int(input('Enter principal amount: '))
rate=float(input('Please Enter rate of interest: '))
time=int(input('Enter number of years for investment: '))
total=p_amount*((1+rate)**time)   #Formula of compound interest
print(f'After {time} years your principle amount {p_amount} over an interest rate {rate}% will be {total}')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ## 10. Euclidean distance
# ### write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# #### Program Console Sample 1:
# ###### Enter Co-ordinate for x1: 2
# ###### Enter Co-ordinate for x2: 4
# ###### Enter Co-ordinate for y1: 4
# ###### Enter Co-ordinate for y2: 4
# ###### Distance between points (2, 4) and (4, 4) is 2

# ###### Reference:
# https://en.wikipedia.org/wiki/Euclidean_distance

# In[9]:


x1=float(input('Enter co=ordinate for x1: '))
x2=float(input('Enter co-ordinate for x2: '))
y1=float(input('Enter co-ordinate for y1: '))
y2=float(input('Enter co-ordinate for y2: '))
dist=(((x2-x1)**2)+((y2-y1)**2))**0.5
print(f'Distance between points ({x1},{y1}) and ({x2},{y2}) is {dist}')


# In[ ]:





# In[ ]:





# In[ ]:





# ## 11. Feet to Centimeter Converter
# ### Write a Python program to convert height in feet to centimetres.
# ##### Program Console Sample 1:
# ###### Enter Height in Feet: 5
# ###### There are 152.4 Cm in 5 ft
# ###### Reference:
# https://www.rapidtables.com/convert/length/feet-to-cm.html

# In[10]:


h_in_feet=int(input('Enter Height in feet: '))
h_in_cm=30.48*h_in_feet 
print('There are',h_in_cm,'cm in',h_in_feet,'ft')


# In[ ]:





# In[ ]:





# In[ ]:





# ## 12. BMI Calculator
# ### Write a Python program to calculate body mass index
# ##### Program Console Sample 1:
# ###### Enter Height in Cm: 180
# ###### Enter Weight in Kg: 75
# ###### Your BMI is 23.15

# In[2]:


h_in_cm=float(input('Enter Height in cm: '))
weight=float(input('Enter weight in kg: '))
h_in_meters=h_in_cm/100
bmi=weight/(h_in_meters**2)   #Formula of BMI
print('Your BMI is',bmi)


# In[ ]:





# In[ ]:





# ## 13. Sum of n Positive Integers
# ### Write a python program to sum of the first n positive integers
# #### Program Console Sample 1:
# ###### Enter value of n: 5
# ###### Sum of n Positive integers till 5 is 15

# In[1]:


n=int(input('Enter value of n: '))
sum_=0
for i in range(1,n+1):
    sum_=sum_+i
print('Sum of n positive integers till',n,'is',sum_)


# In[ ]:





# In[ ]:





# ## 14. Digits Sum of a Number
# ### Write a Python program to calculate the sum of the digits in an integer
# #### Program Console Sample 1:
# ##### Enter a number: 15
# ###### Sum of 1 + 5 is 6
# #### Program Console Sample 2:
# ##### Enter a number: 1234
# ###### Sum of 1 + 2 + 3 + 4 is 10

# In[3]:


num=input('Enter an Integer: ')
sum_=0
for i in num:
    sum_=sum_+int(i)
print('Sum of 1+5 is ',sum_)    
    


# In[ ]:


num=input('Enter an Integer: ')
sum_=0
for i in num:
    sum_=sum_+int(i)
print('Sum of 1+2+3+4 is ',sum_)    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




