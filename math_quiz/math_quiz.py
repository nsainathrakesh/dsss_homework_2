import random


def random_number_generator(min, max):
    """
    Random integer.
    
    Parameters -
    min - lower limit for the random number generator
    max - upper limit for the random number generator

    Returns -
    int : Random integer value between min and max values
    """
    #selects a random number (random.randint) between the input min and max values
    return random.randint(min, max)


def operation_selector():
    """
    Chooses a random operator from the available options.

    Parameters - 
    none

    Returns -
    string : Randomly selected operator from the provided list
    """
    #selects a random character (random.choice) from the choice of math operator strings
    return random.choice(['+', '-', '*'])


def problem_statement(n1, n2, operator):
    """
    Generates a problem statement and also the answer required to score the quiz

    Parameters -
    int : n1 and n2 using randint 
    string : operator required for the mathematical calculation

    Returns - 
    string : problem to display
    int : answer to the problem
    """
    #generating the math problem for the quiz
    problem = f"{n1} {operator} {n2}"
    if operator == '+': answer = n1 + n2
    elif operator == '-': answer = n1 - n2
    else: answer = n1 * n2
    return problem, answer

def math_quiz():
    """
    Poses the question to the user and requests the answers from user as user input and scores against the system generated answers.

    Parameters - 
    none

    Returns -
    prints the correctness of the answer and score at the end of the test
    """
    score = 0
    pi_value = 3.14159265359
    # in a for loop, only integer values can be used with the keyword range, the value provided here, 3.14159265359, is an approximation
    #of pi, which is irrational and this throws an error
    number_of_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for question in range(number_of_questions):
        n1 = random_number_generator(1, 10); n2 = random_number_generator(1, 5); o = operation_selector()
        #problem statement is generated
        PROBLEM, ANSWER = problem_statement(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            #try except is used so that an exception is caught if the user enters any value other than a numeric value
            #handles the exception in the except block when, for example, the answer is entered as 'three' instead of 3
            useranswer = int(useranswer)
        except:
            print("please enter meaningful and NUMERIC values only! Point lost for incorrect answer")
        #scoring based on the correctness of the answer
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
            score -= 1

    print(f"\nGame over! Your score is: {score}")

if __name__ == "__main__":
    math_quiz()
