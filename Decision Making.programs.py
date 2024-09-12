#!/usr/bin/env python
# coding: utf-8

# # Decision making

# # 1. check the number is Even or odd

# In[15]:


def check(n):
    if n%2==0:
        print(f"{n} is Even")
    else:
        print(f"{n} is odd")
n=int(input())
check(n)       


# # 2. check the number is palindrome or not

# In[22]:


def is_palindrome(n):
    # Convert number to string and check if it's equal to its reverse
    return str(n) == str(n)[::-1]

#driver code
n=int(input("enter your number"))
if is_palindrome(n):
    print(f"{n} is palindrome")
else:
    print(f"{n} is not palindrome")


# In[26]:


def check(s):
    return s == s[::-1]


s=input("enter your string :")
if check(s):
    print(f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")
    


# In[28]:


# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)

if ans:
    print("palinndrome")
else:
    print("Not palindrome")


# In[30]:


def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = "malayalam"
ans = isPalindrome(s)
print(ans)


# # 3.check the number is positive negative or zero

# In[40]:


def check(num):
    if num==0:
        return 0
    elif num>1:
        print("positive")
    else:
        print("Negative")
num=int(input("Enter your number :"))

check(num)


# # 4.simple calculator

# In[43]:


# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")


# In[46]:


# Function to perform the chosen operation
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Take input from the user
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")

# Run the calculator function
calculator()


# # 5.check the year is leap or not

# In[59]:


def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
year=2028
if is_leap(year):
    print(f"{year} is leap")
else:
    print(f"{year} is not leap")



# In[53]:


def is_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 4, and
    # 2. It is not divisible by 100, unless it is divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# # 6.check a number is prime or not

# In[5]:


def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    
    # Check if number has any divisors other than 1 and itself
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# In[ ]:




