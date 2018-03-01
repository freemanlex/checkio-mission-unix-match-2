"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        
        {
            "input": ['log1.txt', 'log[1234567890].txt'],
            "answer": True,
            "explanation": "[seq] matches any character in seq. \"1\" is in \"1234567890\""
        },
        {
            "input": ['log1.txt', 'log[!1].txt'],
            "answer": False,
            "explanation": "!1 matches any single character except 1"
        }
    ],
    "Extra": [
        
        {
            "input": ['name.txt', 'name.exe'],
            "answer": False,
            "explanation": "filename matches itself"
        },
        {
            "input": ['name.txt', 'name[.]txt'],
            "answer": True,
            "explanation": "seq with one character works the same as just a one char"
        },
        {
            "input": ['name.txt', 'name[]txt'],
            "answer": False,
            "explanation": "seq without any chars will never match"
        },
        {
            "input": ['nametxt', 'name[]txt'],
            "answer": False,
            "explanation": "seq without any chars will never match"
        },
        {
            "input": ['name.txt', '[!abc]name.txt'],
            "answer": False,
            "explanation": "[!seq] matches any character not in seq"
        },
        {
            "input": ['1name.txt', '[!abc]name.txt'],
            "answer": True,
            "explanation": "[!seq] matches any character not in seq"
        },
        {
            "input": ['1name.txt', '[!1234567890]name.txt'],
            "answer": False,
            "explanation": "filename should not start with number"
        },
        {
            "input": ['name.txt', '[!1234567890]ame.txt'],
            "answer": True,
            "explanation": "filename should not start with number"
        },
        {
            "input": ['a1name.txt', '[!1234567890]1name.txt'],
            "answer": True,
            "explanation": "filename should not start with number"
        },
        
        {
            "input": ['name....', 'name.[!.][!.][!.]'],
            "answer": False
        },
        {
            "input": ['name.exe', 'name.[!.][!.][!.]'],
            "answer": True
        },
        {
            "input": ['[!]check.txt', '[!]check.txt'],
            "answer": True,
            "explanation": "[!] is not class"
        },
        {
            "input": ['check.txt', '[[c]heck.txt'],
            "answer": True,
            "explanation": "unmatched brackets"
        },
        
        {
            "input": ["checkio", "[c[]heckio"],
            "answer": True
        }

    ]
}
