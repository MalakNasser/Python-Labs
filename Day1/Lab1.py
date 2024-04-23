#!/usr/bin/env python3


# -----------------------------1----------------------------- #
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name_reversed = last_name + " " + first_name
print("Your full name reversed is:", full_name_reversed)


# -----------------------------2----------------------------- #
number = int(input("Enter a number: "))
result = number + number * 11 + number * 111

print("The result is:", result)


# -----------------------------3----------------------------- #
print(
    """a string that you "don't" have to escape 
This 
is a ....... multi-line 
heredoc string --------> example"""
)


# -----------------------------4----------------------------- #
import math

radius = 6

volume = (4 / 3) * math.pi * pow(radius, 3)
print("The volume of the sphere is:", volume)


# -----------------------------5----------------------------- #
base = int(input("Enter the base of a triangle: "))
height = int(input("Enter the height of a triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)


# -----------------------------6----------------------------- #
for i in range(-4, 5):
    num = 5 - abs(i)
    print(num * "*")


# -----------------------------7----------------------------- #
word = input("Enter a word: ")
word_reversed = word[::-1]
print("The word reversed is:", word_reversed)


# -----------------------------8----------------------------- #
for i in range(0, 6):
    if i == 3 or i == 6:
        pass
    else:
        print(i)


# -----------------------------9----------------------------- #
fibonacci_series = []
a, b = 0, 1

while a < 50:
    fibonacci_series.append(a)
    a, b = b, a + b

print("The Fibonacci series is:", end=" ")
for i in range(len(fibonacci_series)):
    print(fibonacci_series[i], end="")
    if i < len(fibonacci_series) - 1:
        print(", ", end="")
print("")


# -----------------------------10----------------------------- #
number_of_digits = 0
number_of_letters = 0

string = input("Enter a string: ")
for char in string:
    if char.isdigit():
        number_of_digits += 1
    elif char.isalpha():
        number_of_letters += 1

print(
    "The number of digits is: %d and the number of letters is: %d"
    % (number_of_digits, number_of_letters)
)
