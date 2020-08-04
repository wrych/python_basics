
import scripts.calculator


def test_addition_calculator():
    num1 = 50
    num2 = 50
    operator = '+'
    assert scripts.calculator.calculator(num1, operator, num2) == 100

def test_subtraction_calculator():
    num1 = 150
    num2 = 50
    operator = '-'
    assert scripts.calculator.calculator(num1, operator, num2) == 100 

def test_multiplication_calculator():
    num1 = 25
    num2 = 4
    operator = '*'
    assert scripts.calculator.calculator(num1, operator, num2) == 100  

def test_division_calculator():
    num1 = 400
    num2 = 4
    operator = '/'
    assert scripts.calculator.calculator(num1, operator, num2) == 100     