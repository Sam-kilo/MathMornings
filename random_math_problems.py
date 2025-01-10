
import random

correct_answer = 0
max_problems = 3  # Number of problems to solve

def add_problem():
    """ this program makes you answer a set of random addition problems """
    global correct_answer  # has to be global or correct_answer will reset every time
    finished_problem = False  # tracks if all problems are solved

    while correct_answer < max_problems:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        result = num1 + num2
        user_answer = int(input(f"What is the result of {num1} + {num2}?: "))

        if user_answer == result:
            print("Good job!")
            correct_answer += 1
            if correct_answer < max_problems:
                print("Here's another one...")
        else:
            print("Wrong answer, try again!")

    finished_problem = True
    return finished_problem  # Return whether all problems have been solved

#add_problem() #uncomment to test

