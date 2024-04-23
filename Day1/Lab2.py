#!/usr/bin/env python3


# -----------------------------1----------------------------- #
def reduce_adjacent_duplicates(sequence):
    result = []

    for i in range(len(sequence) - 1):
        if i == 1:
            result.append(sequence[i])
        elif sequence[i] != sequence[i - 1]:
            result.append(sequence[i])

    return result


# Test
sequence = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(reduce_adjacent_duplicates(sequence))


# -----------------------------2----------------------------- #
def divide_string(str):
    if len(str) % 2 == 0:
        str_front = str[: len(str) // 2]
        str_back = str[len(str) // 2 :]
    else:
        str_front = str[: len(str) // 2 + 1]
        str_back = str[len(str) // 2 + 1 :]

    return str_front, str_back


def divide_two_strings(a, b):
    a_front, a_back = divide_string(a)
    b_front, b_back = divide_string(b)

    return f"{a_front}{b_front}{a_back}{b_back}"


# Test
print(divide_two_strings("Malak", "Nasser"))


# -----------------------------3----------------------------- #
def is_unique_sequence(sequence):
    unique_set = set()

    for i in sequence:
        if i not in unique_set:
            unique_set.add(i)
            result = True
        else:
            result = False
            break
    return result


# Test
print(is_unique_sequence([1, 5, 7, 9]))
print(is_unique_sequence([2, 4, 5, 5, 7, 9]))


# -----------------------------4----------------------------- #
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Test
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", unsorted_list)
print("Sorted list:", bubble_sort(unsorted_list))


# -----------------------------5----------------------------- #
import random


def guess_game():
    random_number = random.randint(1, 100)
    trials = 10
    entries = []
    wins = False

    while trials > 0:
        number = int(input("Enter a number between 1 and 100: "))

        if number > 100 or number < 1:
            print("That's not allowed. Please enter a number between 1 and 100.")
            continue

        if number in entries:
            print("You already entered this number.")
            continue

        entries.append(number)
        trials -= 1

        if number > random_number:
            print("The number is too high.")
        elif number < random_number:
            print("The number is too low.")
        else:
            print("Congratulations! You guessed the right number.")
            wins = True

        if not wins and trials == 0:
            print(f"Game over! The correct number was {random_number}.")
        elif wins and trials > 0:
            random_number = random.randint(1, 100)
            entries = []
            wins = False
            print("\nLet's play again with a new number!\n")
            continue

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        guess_game()
    else:
        print("Thanks for playing!")


# Start the game
guess_game()
