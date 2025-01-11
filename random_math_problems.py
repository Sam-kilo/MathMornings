
import random

correct_answer = 0
max_problems = 3  # Number of problems to solve
operator = ["+","-","*"]

def generate_problem():
    """ Generate a problem with random operator and"""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    random_operator = random.choice(operator)
    result = None

    # Perform the operation based on the operator
    if random_operator == "+":
        result = num1 + num2
    elif random_operator == "-":
        result = num1 - num2
    elif random_operator == "*":
        result = num1 * num2


    return num1, num2, random_operator, result
def math_problem():
    """ this program makes you answer a set of random addition problems """
    global correct_answer  # has to be global or correct_answer will reset every time
    finished_problem = False  # tracks if all problems are solved

    while correct_answer < max_problems:
        num1, num2, random_operator, result = generate_problem()

        user_answer = int(input(f"What is the result of {num1} {random_operator} {num2}?: "))

        if user_answer == result:
            print("Good job!")
            correct_answer += 1
            if correct_answer < max_problems:
                print("Here's another one...")
        else:
            print("Wrong answer, try again!")

    finished_problem = True
    return finished_problem  # Return whether all problems have been solved


#math_problem() #uncomment to test

