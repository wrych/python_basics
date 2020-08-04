
"""
write a calculator that takes a number as a first value,
the second input is an operator (may be either + - * /)
the third input is a number again
then execute the calculation
you may use the game_input function we programmed for yatzee
"""
if __name__ == "__main__":
    input_1 = float(input("Please write The First Number: \n"))
    print('\n')
    input_operator = input("Please write an Operator, may be either + - * /: \n")
    print('\n')
    input_2 = float(input("Please write The Second Number: \n"))
    print('\n')

    operation = '{0:<5}{1:^5}{2:>5}'.format(num1, operator, num2)

    result = calculator(input_1, input_operator, input_2)   
    print("Operation is: \n" + operation)
    print('\n')
    print("Result is: \n" + str(result))

def calculator(num1, operator, num2):
    if operator == '+':
        result =  num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
            result = num1 / num2    
    return result





