"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

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
    ],
}
