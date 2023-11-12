import unittest
from math_quiz import random_number_generator, operation_selector, problem_statement


class TestMathGame(unittest.TestCase):

    def test_random_number_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for counter in range(1000):  # Test a large number of random values
            rand_num = random_number_generator(min_val, max_val)
            #self.assertTrue() checks the condition passed and the test is successful if the condition is true. 
            #checked for 1000 for being on the safer side and to not miss any single exception cases.
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_operation_selector(self):
        # TODO
        operators = ['+', '-', '*']
        for counter in range(1000):
             rand_operator = operation_selector()
             #self.assertIn(a,b) checks if the value a exists in the range of values of b
             self.assertIn(rand_operator, operators)

    def test_problem_statement(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 3, '-', '3 - 3', 0),
                (2, 6, '*', '2 * 6', 12)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                gen_problem, gen_answer = problem_statement(num1, num2, operator)
                #self.assertEqual(a,b) checks if the value of a equals to that of b
                self.assertEqual(gen_problem, expected_problem)
                self.assertEqual(gen_answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
