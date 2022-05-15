"""
    Problem 1 
    Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
    and lays them out face down in a sequence on a table. She challenges Bob to pick out the card 
    containing a given number by turning over as few cards as possible. Write a function to help 
    Bob locate the card.
"""

# 1. State the problem clearly. Identify the inputs and outputs formats
"""
    Problem 1
    We need to write a program to find the position of a given number in a list of numbers arranged in 
    decreasing order. We also need to minimize the number of times we access elements from the list.

    Input
    1. Cards: A list of numbers sorted in decreasing order. Ex.: [13, 11, 10, 7, 4, 3, 1, 0]
    2. Value_card: A number, whose position in the array is to be determined. Ex.: 7

    Output
    1. Position: The position of the value_card in the list cards. Ex.: 3 
"""

# 2. Come up with some examples of input and output. Try to cover all edge cases
"""
    cards = [13, 11, 10, 7, 4, 3, 1, 0]
    value_card = 7
    output = 3
"""
"""
    List of possible variations
    1. The number card_value occurs somewhere in the middle of the list cards.
    2. card_value is the first element in cards.
    3. card_value is the last element in cards.
    4. The list cards contains just one element, which is card_value.
    5. The list cards does not contain number card_value.
    6. The list cards is empty.
    7. The list cards contains repeating numbers.
    8. The number card_value occurs at more than one position in cards.
"""

# 3. Come up with a correct solution for the problem.
# 4. Implement the solution and test it using example inputs
"""
    linear search
"""

# 5. Analyse the algorithm's complexity and identify inefficiencies
"""
    Using the linear search algorithm we need to check all of cards if the card_value is the last element
    For linear search algorithm the time complexity is O(N)
    and the space complexity is O(1)
"""

# 6. Apply the right technique to overcome the inefficiency
"""
    The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine 
    whether the target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce 
    the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the 
    process with each half.
"""


from jovian.pythondsa import evaluate_test_cases
from search_functions.linear_search import linear_search_cards
from search_functions.binary_search import binary_search_cards

test_cases = [
    # card_value occurs in the middle
    {
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
            'value_card': 7
        },
        'output': 3
    },
    # card_value occurs in first element
    {
        'input': {
            'cards': [4, 2, 1, -1],
            'value_card': 4
        },
        'output': 0
    },
    # card_value occurs in the last element
    {
        'input': {
            'cards': [3, -1, -9, -127],
            'value_card': -127
        },
        'output': 3
    },
    # card_value occurs in a list with 1 element
    {
        'input': {
            'cards': [6],
            'value_card': 6
        },
        'output': 0 
    },
    # cards doesn't contain card_value
    {
        'input': {
            'cards': [9, 7, 5, 2, -9],
            'value_card': 4
        },
        'output': -1
    },
    # cards is empty
    {
        'input': {
            'cards': [],
            'value_card': 7
        },
        'output': -1
    },
    # numbers can repeat in cards
    {
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'value_card': 3
        },
        'output': 7
    }

]


evaluate_test_cases(linear_search_cards, test_cases)
evaluate_test_cases(binary_search_cards, test_cases)