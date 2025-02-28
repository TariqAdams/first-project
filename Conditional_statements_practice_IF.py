'''
1. To the Ticket discount program we worked with in class, the AnyCompany Zoo is adding a new promotion:
If a user is a student and above age 20, they get a $15 discount. 
To the existing program, add this condition and test with appropriate input values.
'''
admission_price = 25
discount = 0
age = int(input("Enter your age: "))

student = input("Please let us know if you are student. Answer yes or no:")

if age > 65 or student == 'yes': # if True or False
    discount = 10
elif student == 'yes' and age > 20:
    discount = 15

ticket_price = admission_price - discount

print("Your ticket price is: ", ticket_price)

'''
2. Ask the user to input any number. Use conditions to determine if the user-entered number is even or odd and print 
if the number is even or if the number is odd. Hint: a number is even if it is completely divisible by 2.
In other words, when you divide a number by 2, if the remainder is 0, it is an even number. If not, it is an odd number.
'''
user_num = int(input("Please enter a number: "))

if user_num%2 == 0:
    print("The number you entered is even.")
else:
    print("The number you entered is odd.")

'''
You are writing a program to allocate Auditorium seating row for the user based on their favorite number. 
Get a user inputted value between 1 and 50 and save it in the variable “fav_number”. Based on this value, 
using the following seating map, print the row that the user will sit in the auditorium. 
If the user enters anything that is above 100 or below 0, the program should tell them that it is an invalid input.
Fav_number       ----            Row
1 - 10                  -----          E
11 - 20                -----          D
21 – 30               -----          C
31 – 40                ------        B
41 - 50                ------         A
'''

fav_number = int(input("Please enter a number between 1 and 50: "))

if fav_number >= 1 and fav_number <= 10:
    print("You are in row E")
elif fav_number >= 11 and fav_number <= 20:
    print("You are in row D")
elif fav_number >= 21 and fav_number <= 20:
    print("You are in row C")
elif fav_number >= 31 and fav_number <= 40:
    print("You are in row B")
elif fav_number >= 41 and fav_number <= 50:
    print("You are in row A")
elif fav_number > 100 or fav_number < 0:
    print("Invalid input!")

# greater_num = False

# while greater_num == False:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     if num1 > num2:
#         print(f"{num1} is greater than {num2}")
#         greater_num = True
   