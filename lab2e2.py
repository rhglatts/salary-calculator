#Author: Rebecca Glatts
#Assignment: Lab 2
#Completed: 1/31/2022


#asks user for their name
name = input("Please enter your name: ")
#asks user for age
age = input("Please enter your age: ")
#asks user for company
company = input("Enter the company you wish to work for: ")
#asks user for monthly salary
salary = int(input("Enter monthly salary you wish to earn in dollars: "))
yearly = salary * 12
#multiplies monthly salary by 12 months to get yearly salary and prints out info given
print(f"\nMy name is {name} my age is {age} \nI hope to work for {company} and earn {salary*12} a year.")

"""Please enter your name: Jane Doe
Please enter your age: 24
Enter the company you wish to work for: Apple
Enter monthly salary you wish to earn in dollars: 9000

My name is Jane Doe my age is 24
I hope to work for Apple and earn 108000 a year."""

"""
Please enter your name: John Smith
Please enter your age: 30
Enter the company you wish to work for: Google
Enter monthly salary you wish to earn in dollars: 5000

My name is John Smith my age is 30
I hope to work for Google and earn 60000 a year.
"""