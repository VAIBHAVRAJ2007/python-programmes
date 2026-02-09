# import os 
# print("hello world")
# print("hello world2. "," hello")
# print(2+6)
# _name ="Vaibhav Raj"
# ag_e = -20
# price_ =25.33

# print(type(_name))
# print(type(ag_e))
# print(type(price_))
# name1='vaibhav'
# name2="vaibhav"
# name3='''vaibhav'''
# print(name3)
# print(name2)
# print(name1)

# name=None
# false=False
# print(type(name))
# print(type(false))
# print(false)
# print(name)

# print('hello'+str(56))
# def fun():
#     name=str(input('Enter your name: '))
#     roll=int(input('Enter your roll no.: '))
#     cls=str(input('Enter your class: '))
#     return name,roll,cls
# name,roll,cls=fun()
# print(name,str(roll),cls,sep='-')
# print(type(name))
# print(type(roll))
# print(type(cls))

# def myfunc1():
#     x='Jane'
#     def myfunc2():
#         nonlocal x
#         x='Hello'
#     myfunc2()
#     return x
# print(myfunc1())

# a=int(input("Enter:"))
# while a>5:
#     a-=1
#     print(a)
#     break
# else:
#     print(a+10)

# num=(input(("Enter a number: ")))

# if num.isdigit():
#   num = int(num)
#   if num>0:
#     print(num,"is positive")
#   elif num<0:
#     print(num," is negative")
#   elif num==0:
#     print("Number is zero")
# else:
#   print("Invalid input")

# a = 10
# b = 14
# c = 12
# m = a if (a >= b and a >= c) else (b if b >= c else c)
# print(m)

# Input the range values
# num1 = int(input('Enter lower limit of range: '))
# num2 = int(input('Enter heigheer limit of range: '))
# #print the outcome of operators
# sum = 0
# i = num1
# while i <= num2:
#   if i % 2 == 0:
#     print(i)
#     sum += i
#   i += 1
# print(f"Sum of all the even numbers is {sum}")

# Input the two number values
# a = int(input('Enter the first number: '))
# b = int(input('Enter the second number: '))
#define the swap function and print the outcome
# def swap_arithmetic(a, b):
#     print(f"Before swapping: a = {a}, b = {b}")
#     a = a + b
#     b = a - b
#     a = a - b
#     print(f"After swapping: a = {a}, b = {b}")
# swap_arithmetic(a, b)

# import datetime and set the format
# import datetime
# now = datetime.datetime.now()
# formatted_date = now.strftime("%a %d %H:%M:%S %Y")
# #print the outcome
# print(formatted_date)


# define the functions
# def celsius_to_fahrenheit(celsius):
#     """Converts Celsius to Fahrenheit."""
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit
# def fahrenheit_to_celsius(fahrenheit):
#     """Converts Fahrenheit to Celsius."""
#     celsius = (fahrenheit - 32) * 5/9
#     return celsius
# # Get user input
# choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").upper()
# #print the outcome
# if choice == 'C':
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = celsius_to_fahrenheit(celsius)
#     print(f"{celsius}°C is equal to {fahrenheit}°F")
# elif choice == 'F':
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = fahrenheit_to_celsius(fahrenheit)
#     print(f"{fahrenheit}°F is equal to {celsius}°C")
# else:
#     print("Invalid choice. Please enter C or F.")



# n=int(input("Enter number of character in string:"))
# str1=input("Enter a string:")
# for i in range(0,n):
#         for j in range(n):
#             if str1[i]==str1[j]:
#                 break
#         else:                           # Run this block only if no duplicate was found for this character.
#             print('First unique character is',str1[i],'at',i+1)
#             break

#use range() function to print list elements using while loop
# age=20
# if age<18:
#     print("eligible")
# elif age<=20:
#     print("Eligible")
# elif age>19:
#     print("eleg")
# else:
#     print("Not eligible")
# print("good")
# x=['ab','cd']
# y=[]
# for i in x:
#     y.append(i.upper())
# print(y)    

# List=["vaIbhAv",'rAj']
# Dict={"Number":x.capitalize() for x in List if len(List)<4}
# print(type(Dict))
# print(Dict)

# list1=[54,74,26,87,45]

# list2=list1.copy()
# list2[0]=40
# list1[0]=44
# print(list2)
# print(list1)

str1="banana"
str2=str1.rjust(10)
str3="is a fruit"
print(str2,str3)