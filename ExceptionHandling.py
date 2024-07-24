# EXCEPTION HANDLING (TRY WITH MULTIPLE EXCEPT)

# print("Line 1")
# print("Line 2")
# print("Line 3")
# print("Line 4")
# try :
#     print(100/0)               #if this generates exception then pointer will directly moce to except and move on
#     open("pqr.txt")
# except ZeroDivisionError as e:
#     print(e)
# except FileNotFoundError :
#     print("File does not exist")
# print("Line 6")
# print("Line 7")
# print("Line 8")
# print("Line 9")
# print("Line 10")


# question - 1
# program to handle ZeroDivisionError 

# def divide(dividend, diviser):
#     return dividend/diviser

# try :
#     divide(20,0)
# except ZeroDivisionError as e:
#     print(e)


# question - 2
# input an integer and raise a value error if invalid
# try:
#     num = int(input("Enter an integer : "))
# except ValueError :
#     print("Invalid input , please enter an integer")


# question - 3
# handle FileNotFoundError 

# try:
#     open('abc.txt')
# except FileNotFoundError :
#     print("File not found ..")


# question - 4
# input two numbers and raise exception if inputs are not numerical

def add_numbers(a, b):
    try:
        result = a + b
        print(f"The result is {result}")
    except TypeError as e:
        print(f"TypeError: {e}")
        print("Please ensure both inputs are numbers.")

# Test cases
add_numbers(10, 5)       # Valid input
add_numbers(10, 'five')  # Invalid input, raises TypeError

