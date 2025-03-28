#Week 7 Programming Homework
#Badge C5-1 (Return Function)
#Badge C5-2 (Using Functions)
#Badge C5-3 (Module)
#Badge C5-4 (Scope)

import random

def random_num():
        return random.randint(1,50)   #(C5-1)

def choose_symbol():
    return random.choice(['+', '-'])   

def calc_answer(number1, number2, operation):
    if operation == '+':
        return number1 + number2       
    elif operation == '-':
        return number1 - number2      

def question(number1, number2, operation):    #(C5-3)
    if operation == '-' and number1 < number2:
        number1, number2 = number2, number1
    number_input = int(input(f"Please enter {number1} {operation} {number2} : "))
    return number_input, number1, number2    

def quiz():    #(C5-4)
    number1 = random_num()
    number2 = random_num()

    operation = choose_symbol()

    right_answer =  calc_answer(number1, number2, operation) #(C5-2)

    user_answer, number1, number2 = question(number1, number2, operation)

    if user_answer == right_answer:
        print("You got the right answer. Amazing Job!")
    else:
        print(f"I'm sorry that is not the right answer. The correct answer is {right_answer}.")

quiz()