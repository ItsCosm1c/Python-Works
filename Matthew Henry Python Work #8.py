import random

def random_num():
        return random.randint(1,50) 

def choose_symbol():
    return random.choice(['+', '-'])   

def calc_answer(number1, number2, operation):
    if operation == '+':
        return number1 + number2       
    elif operation == '-':
        return number1 - number2      

def question(number1, number2, operation):  
    if operation == '-' and number1 < number2:
        number1, number2 = number2, number1
    number_input = int(input(f"Please enter {number1} {operation} {number2} : "))
    return number_input, number1, number2    

def quiz():  
    number1 = random_num()
    number2 = random_num()

    operation = choose_symbol()

    right_answer =  calc_answer(number1, number2, operation)

    user_answer, number1, number2 = question(number1, number2, operation)

    if user_answer == right_answer:
        print("You got the right answer. Amazing Job!")
    else:
        print(f"I'm sorry that is not the right answer. The correct answer is {right_answer}.")

quiz()
