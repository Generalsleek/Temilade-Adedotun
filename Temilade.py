"""
#1. Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math

radius = input("Enter the radius of the circle:")  #This is the command for calling up user input
radius = float(radius) #This is used to convert the user input to number 
area = 3.14159 * (radius ** 2)  #Im using this as the formula for area of a cicle
print("The area of the circle is:",area)   #This is used to print the result
"""
"""
#2. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

first_name = input("Enter your first name: ")  #used to call up First Name input
last_name = input("Enter your last name: ") #used to call up Last Nmae input
print("Your name in reverse order is:", last_name, first_name)    #Printing in reverse as instructed
"""
"""
#3. Write a Python program to display the first and last colors from the following list.color_list = ["Red","Green","White" ,"Black"]

colour_list = ["Red", "Green", "White", "Black"] #Defining the list of colours as instructed.
print("First Colour:", colour_list[0]) #Print first colour
print("Last Colour:", colour_list[3])  #print the last colour
"""
"""
#4. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

numbers = [] # This is used to create an empty list to store the numbers
for number in range(1500, 2701):  #2701 is used because the range stops at 2700
    if number % 7 == 0 and number % 5 == 0:  # This is used to Check if it is divisible by both 7 and 5
        print(number)  # Print the number
"""
"""
#5. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]Expected Output :60°C is 140 in Fahrenheit45°F is 7 in Celsius6.

print("Do you want to convert from Celsius or Fahrenheit?")  # Ask the user if they want to convert from Celsius or Fahrenheit
choice = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ")

if choice.upper() == "C":     # If the user wants to convert from Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))  # Get Celsius value from user
    fahrenheit = (celsius * 9/5) + 32  # Convert to Fahrenheit
    print(celsius, "°C is", fahrenheit, "°F")  #Printing the Display result


elif choice.upper() == "F":        # If the user wants to convert from Fahrenheit to Celsius
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Get Fahrenheit value from user
    celsius = (fahrenheit - 32) * 5/9  # Convert to Celsius
    print(fahrenheit, "°F is", round(celsius, 1), "°C")  # Printing the Display result

# If the user enters something else
else:
    print("Invalid choice! Please enter 'C' or 'F'.")  #Printing for Error message
"""
"""
# 6. Write a Python program to create a class representing a Circle.
#Include methods to calculate its area and perimeter.
"""
"""
class Circle:  # Create a Circle class
    def __init__(self, radius):   #Constructor method to store radius
        self.radius = radius  #Save the radius

    def area(self):   #Method to calculate the area
        return 3.14159 * (self.radius ** 2)  # Formula: π * r^2

    def perimeter(self):    #Method to calculate the perimeter (circumference)
        return 2 * 3.14159 * self.radius  # Formula: 2 * π * r

radius = float(input("Enter the radius of the circle: "))     #Ask the user for the radius

my_circle = Circle(radius)     #Create a Circle object using the radius

print("The area of the circle is:", round(my_circle.area(), 2))  #Print to  Show area
print("The perimeter of the circle is:", round(my_circle.perimeter(), 2))  #Print to Show perimeter
"""
