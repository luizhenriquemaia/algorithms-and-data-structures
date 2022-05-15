"""
    For linear search algorithm the time complexity is O(N)
    and the space complexity is O(1)
"""


def linear_search_cards(cards: list[int], value_card: int) -> int:
    """ 
        Returns the position of a card on the list of cards using his value
        and linear search algorithm
    """
    position = 0
    while position < len(cards):
        if cards[position] == value_card:
            return position
        position += 1
    return -1