print("###########################################################################")
print("")
print("Part 1:")
print("This is a python program to add and subtract two numbers.")
print("Inputs are converted to floats and outputs are rounded to 3 decimal places.")
print("")
print("###########################################################################")
print("")

# Return user input and handle bad inputs
def get_num(index):
    try:
        match index:
            case 1:
                number = input("Please enter the first number: ")
            case 2:
                number = input("Please enter the second number: ")

        return float(number)

    except:
        print("Please enter a valid number")
        return get_num(index)

# add numbers
def add_numbers(number1, number2):
    return number1 + number2
    
# subtract numbers
def subtract_numbers(number1, number2):
    return number1 - number2

# multiply numbers
def multiply_numbers(number1, number2):
    return number1 * number2

# divide numbers
def divide_numbers(number1, number2):
    return number1 / number2

# Get user inputs
num1 = get_num(1)
num2 = get_num(2)

# do math
sum_num = add_numbers(num1, num2)
sub_num = subtract_numbers(num1, num2)

print()
print("You entered %s and %s." % (num1, num2))
print("The addition of (%s + %s) is %s." % (num1, num2, round(sum_num,3)))
print("The subtraction of (%s - %s) is %s." % (num1, num2, round(sub_num,3)))
print()


print("###########################################################################")
print("")
print("Part 2:")
print("This is a python program to multiply and divide two numbers.")
print("Inputs are converted to floats and outputs are rounded to 3 decimal places.")
print("")
print("###########################################################################")
print("")

# Get user inputs again
num1 = get_num(1)
num2 = get_num(2)

# do math
mult_num = multiply_numbers(num1, num2)
div_num  = divide_numbers(num1, num2)

print()
print("You entered %s and %s." % (num1, num2))
print("The multiplication of (%s * %s) is %s." % (num1, num2, round(mult_num,3)))
print("The division of (%s / %s) is %s." % (num1, num2, round(div_num,3)))
print()
