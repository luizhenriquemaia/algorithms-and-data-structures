"""
    Where log refers to log to the base 2. Therefore, our algorithm has the time complexity O(log N). 
    This fact is often stated as: binary search runs in logarithmic time. You can verify that the space 
    complexity of binary search is O(1).
"""

def check_location(cards: list[int], value_card: int, position: int) -> str:
    """ 
    Check if the position found is the first posible position for repeated values and if it is equal 
    to the value card   
    """
    if cards[position] == value_card:
        if position-1 >= 0 and cards[position-1] == value_card:
            return 'left'
        else:
            return 'found'
    elif cards[position] < value_card:
        return 'left'
    else:
        return 'right'

def binary_search_cards(cards: list[int], value_card: int) -> int:
    """ Returns the position of a card on the list of cards by using his value and binary search algorithm """
    low_position, high_position = 0, len(cards) - 1
    while low_position <= high_position:
        middle_position = (low_position + high_position) // 2
        result = check_location(cards, value_card, middle_position)
        if result == 'found':
            return middle_position
        elif result == 'left':
            high_position = middle_position - 1
        elif result == 'right':
            low_position = middle_position + 1
    return -1


