"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? if number is not a whole integer
2. When will a ZeroDivisionError occur? if you try divide by zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    while True:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Can't divide by zero!")
        else:
            break

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
    # print("Cannot divide by zero!") these are no longer needed
print("Finished.")