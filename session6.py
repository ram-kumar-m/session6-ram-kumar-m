import random

vals = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

cards = [i+j for i in suits for j in vals]

cards_with_lambda_map_zip = list(
    map(lambda x: x[0]+x[1], zip(suits*13, vals*4)))

royal_flush = ['heartsace', 'heartsking',
            'heartsqueen', 'heartsjack', 'hearts10']

straight_flush = ['clubs'+str(i) for i in range(10, 5, -1)]

four_kind = [i+'queen' for i in ['clubs',
                                'hearts', 'spades', 'diamonds']] + ['clubs5']

full_house = [i+'ace' for i in ['hearts', 'spades', 'diamonds']] + ['spadesking', 'heartsking']

flush = ['hearts'+i for i in ['king', '8', '6', '4', '2']]

straight = ['hearts8', 'clubs7', 'diamonds6', 'spades5', 'hearts4']

three_kind = [i+'queen' for i in ['clubs', 'hearts', 'spades']] + ['hearts7', 'clubs2']

one_pair = ['spadesjack', 'diamondsjack', 'diamonds9', 'spades9', 'clubs5']

high_card = ['heartsace', 'clubsqueen', 'hearts6', 'spades4', 'diamonds2']


value_pair_list = [
                royal_flush,
                straight_flush,
                four_kind,
                full_house,
                flush,
                straight,
                three_kind,
                one_pair,
                high_card]

precedences = tuple((i, set(_list)) for i, _list in zip(
    range(len(value_pair_list), 0, -1), value_pair_list))


def create_deck(suits: list, vals: list) -> list:
    """Generate a deck of cards, with the given suits and vals.

    Args:
        suits (list): eg. cloves, spades etc..
        vals  (list): 1, 2, jack etc..

    Returns:
        list: cloves1, spades2 etc.. 52 elements for a normal deck
    """
    deck = []
    for i in suits:
        for j in vals:
            deck.append(i+j)
    return deck


def return_n_cards(n: int) -> list:
    """Returns a list of n cards

    Args:
        n (int): Number of cards to return

    Returns:
        list: 'n' number of Shuffled Cards
    """

    if n not in [3, 4, 5]:
        raise ValueError('you can get only 3, 4 or 5 cards.')
    else:
        return random.sample(cards, n)


def find_rank(hand: list) -> int:
    """Returns the rank of a hand. Better the hand, higher the rank
    for eg rank of full house < royal flush

    Args:
        a (list): hand of a player

    Returns:
        int: value associated with a hand.
    """

    if not isinstance(hand, list):
        raise TypeError('Hand must be a list of cards')
    elif len(hand) not in [3, 4, 5]:
        raise ValueError('Number of cards must be either 3, 4 or 5.')
    else:
        num = len(hand)
        rank = 0
        for _rank, values in precedences:
            counter = 0
            for card in hand:
                if card in values:
                    counter += 1

            if counter > num//2:
                rank = _rank
                break
        # Special case for three of a kind, since three of a kind and
        # four of a kind are very similar
        if set(hand) == set(three_kind):
            rank = len(value_pair_list) - 6
        return rank


def return_winner(a: list, b: list) -> list:
    """Returns the winner of cards deemed winner

    Args:
        a (list): Cards of a
        b (list): Cards of b

    Returns:
        list: Winner, list , Cards of a / Cards of b

    """
    if not isinstance(a, list) and not isinstance(b, list):
        raise TypeError('Hands must be a list of cards')
    elif len(a) != len(b):
        raise ValueError('Both player Should have equal number of cards.')
    elif len(a) not in [3, 4, 5]:
        raise ValueError('Number of cards must be either 3, 4 or 5.')
    else:
        rank_a = find_rank(a)
        rank_b = find_rank(b)

        if rank_b > rank_a:
            return b
        elif rank_b < rank_a:
            return a
        else:
            return 'There are no winners in life, just Idiots.'
