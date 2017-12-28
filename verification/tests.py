"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
# create Ramdoms
from random import randint
from re import findall
from my_solution import nonogram_row

random_tests = []

for _ in range(10):
    length = randint(5, 15)

    while True:
        row = ''.join('XO'[randint(0, 1)] for i in range(length))
        fa = findall(r'O+', row)
        if 1 <= len(fa) <= 4: break

    row_string = ''.join(('?'*38+'XO')[randint(0,39)]
                    if randint(0, 9) else c for c in row)
    clue_numbers = list(map(len, fa))
    answer = nonogram_row(row_string, clue_numbers)
    random_tests.append({'input': [row_string, clue_numbers],
                        'answer': answer})

TESTS = {
    "Basics": [
        {
            "input": ['??????????', [8]],
            "answer": '??OOOOOO??',
            "explanation": 'Simple boxes'
        },
        {
            "input": ['??????????', [4, 3]],
            "answer": '??OO???O??',
            "explanation": 'Simple boxes'
        },
        {
            "input": ['???O????O?', [3, 1]],
            "answer": 'X??O??XXOX',
            "explanation": 'Simple spaces'
        },
        {
            "input": ['????X?X???', [3, 2]],
            "answer": '?OO?XXX?O?',
            "explanation": 'Forcing'
        },
        {
            "input": ['O?X?O?????', [1, 3]],
            "answer": 'OXX?OO?XXX',
            "explanation": 'Glue'
        },
        {
            "input": ['??OO?OO???O?O??', [5, 2, 2]],
            "answer": 'XXOOOOOXXOOXOOX',
            "explanation": 'Joining and splitting'
        },
        {
            "input": ['????OO????', [4]],
            "answer": 'XX??OO??XX',
            "explanation": 'Mercury'
        },
        {
            "input": ['???X?', [0]],
            "answer": 'XXXXX',
            "explanation": 'Empty_01'
        },
        {
            "input": ['?????', []],
            "answer": 'XXXXX',
            "explanation": 'Empty_02'
        },
        {
            "input": ['??X??', [3]],
            "answer": None,
            "explanation": 'Wrong string'
        },
    ],
    "Edges": [
        {
            "input": ['??????????', [10]],
            "answer": 'OOOOOOOOOO',
            "explanation": ''
        },
        {
            "input": ['??????????', [3, 3]],
            "answer": '??????????',
            "explanation": ''
        },
        {
            "input": ['???????????????', [5, 5]],
            "answer": '????O?????O????',
            "explanation": ''

        },
    ],
    "Randoms": random_tests
}
