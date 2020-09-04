import session6 as main
import pytest
import random
import os
import inspect
import re

vals = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

cards = [i+j for i in suits for j in vals]
royal_flush = ['heartsace', 'heartsking',
               'heartsqueen', 'heartsjack', 'hearts10']

straight_flush = ['clubs'+str(i) for i in range(10, 5, -1)]

four_kind = [i+'queen' for i in ['clubs',
                                 'hearts', 'spades', 'diamonds']] + ['clubs5']

full_house = [i+'ace' for i in ['hearts', 'spades', 'diamonds']] + \
    ['spadesking', 'heartsking']

flush = ['hearts'+i for i in ['king', '8', '6', '4', '2']]

straight = ['hearts8', 'clubs7', 'diamonds6', 'spades5', 'hearts4']

three_kind = [i+'queen' for i in ['clubs',
                                  'hearts', 'spades']] + ['hearts7', 'clubs2']

one_pair = ['spadesjack', 'diamondsjack', 'diamonds9', 'spades9', 'clubs5']

high_card = ['heartsace', 'clubsqueen', 'hearts6', 'spades4', 'diamonds2']


value_pair_list = [royal_flush, straight_flush,
                   four_kind, full_house, flush, straight, three_kind,
                   one_pair, high_card]


num_cards = random.choice([3, 4, 5])

def compare_lists(list1, list2):
    for a in list1:
        if a not in list2:
            return False
    return True

def test_check_compare_lists():
    assert compare_lists([1,2],[2,1]) == True

def test_lambda_map_zip_expression():
    assert compare_lists(main.cards_with_lambda_map_zip, cards) == True, 'Invalid Deck Creation'

def test_create_deck():
    deck = main.create_deck(main.suits, main.vals)
    assert compare_lists(deck, cards) == True, 'Invalid Deck Creation'

def test_vals():
    assert main.vals == vals, 'Different vals.'

def test_suits():
    assert main.suits == suits, 'Different suits.'

def test_cards():
    assert main.cards == cards, 'Diffrent Cards.'

def test_royal_flush():
    assert main.royal_flush == royal_flush, 'Check elements in Royal flush'

def test_straight_flush():
    assert main.straight_flush == straight_flush, 'Check elements in Straight flush'

def test_four_kind():
    assert main.four_kind == four_kind, 'Check elements in Four of a kind'

def test_full_house():
    assert main.full_house == full_house, 'Check elements in Full house'

def test_flush():
    assert main.flush == flush, 'Check elements in flush'

def test_straight():
    assert main.straight == straight, 'Check elements in straight'

def test_three_kind():
    assert main.three_kind == three_kind, 'Check elements in Three of a kind'

def test_one_pair():
    assert main.one_pair == one_pair, 'Check elements in One-Pair'

def test_high_card():
    assert main.high_card == high_card, 'Check elements in High Card'


def test_precedence_royal_flush():
    assert main.find_rank(main.royal_flush) == len(main.value_pair_list)

def test_precedence_straight_flush():
    assert main.find_rank(main.straight_flush) == len(main.value_pair_list)-1

def test_precedence_four_kind():
    assert main.find_rank(main.four_kind) == len(main.value_pair_list)-2

def test_precedence_full_house():
    assert main.find_rank(main.full_house) == len(main.value_pair_list)-3

def test_precedence_flush():
    assert main.find_rank(main.flush) == len(main.value_pair_list)-4

def test_precedence_straight():
    assert main.find_rank(main.straight) == len(main.value_pair_list)-5

def test_precedence_three_kind():
    assert main.find_rank(main.three_kind) == len(main.value_pair_list)-6

def test_precedence_one_pair():
    assert main.find_rank(main.one_pair) == len(main.value_pair_list)-7

def test_precedence_high_card():
    assert main.find_rank(main.high_card) == len(main.value_pair_list)-8

def test_royal_flush_vs_straight_flush():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(straight_flush, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats straight flush'

def test_royal_flush_vs_four_kind():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(four_kind, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats four of a kind'

def test_royal_flush_vs_full_house():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(full_house, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats a full house'

def test_royal_flush_vs_flush():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(flush, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats a flush'

def test_royal_flush_vs_straight():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(straight, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats a straight'

def test_royal_flush_vs_three_kind():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(three_kind, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats a three_kind'

def test_royal_flush_vs_one_pair():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats a one_pair'

def test_royal_flush_vs_high_card():
    a = random.sample(royal_flush, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'Royal flush beats a high_card'

def test_straight_flush_vs_four_kind():
    a = random.sample(straight_flush, num_cards)
    b = random.sample(four_kind, num_cards)
    assert main.return_winner(a, b) == a, 'straight flush beats four of a kind'

def test_straight_flush_vs_full_house():
    a = random.sample(straight_flush, num_cards)
    b = random.sample(full_house, num_cards)
    assert main.return_winner(a, b) == a, 'straight flush beats a full house'

def test_straight_flush_vs_flush():
    a = random.sample(straight_flush, num_cards)
    b = random.sample(flush, num_cards)
    assert main.return_winner(a, b) == a, 'straight flush beats a flush'

def test_straight_flush_vs_straight():
    a = random.sample(straight_flush, num_cards)
    b = random.sample(straight, num_cards)
    assert main.return_winner(a, b) == a, 'straight flush beats a straight'

def test_straight_flush_vs_three_kind():
    a = random.sample(straight_flush, 5)
    b = random.sample(three_kind, 5)
    assert main.return_winner(a, b) == a, 'straight flush beats a three_kind'

def test_straight_flush_vs_one_pair():
    a = random.sample(straight_flush, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'straight flush beats a one_pair'

def test_straight_flush_vs_high_card():
    a = random.sample(straight_flush, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'straight flush beats a high_card'

def test_four_kind_vs_full_house():
    a = random.sample(four_kind, num_cards)
    b = random.sample(full_house, num_cards)
    assert main.return_winner(a, b) == a, 'four kind beats a full house'

def test_four_kind_vs_flush():
    a = random.sample(four_kind, num_cards)
    b = random.sample(flush, num_cards)
    assert main.return_winner(a, b) == a, 'four kind beats a flush'

def test_four_kind_vs_straight():
    a = random.sample(four_kind, num_cards)
    b = random.sample(straight, num_cards)
    assert main.return_winner(a, b) == a, 'four kind beats a straight'

def test_four_kind_vs_three_kind():
    a = random.sample(four_kind, 5)
    b = random.sample(three_kind, 5)
    assert main.return_winner(a, b) == a, 'four kind beats a three_kind'

def test_four_kind_vs_one_pair():
    a = random.sample(four_kind, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'four kind beats a one_pair'

def test_four_kind_vs_high_card():
    a = random.sample(four_kind, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'four kind beats a high_card'

def test_full_house_vs_flush():
    a = random.sample(full_house, num_cards)
    b = random.sample(flush, num_cards)
    assert main.return_winner(a, b) == a, 'full house beats a flush'

def test_full_house_vs_straight():
    a = random.sample(full_house, num_cards)
    b = random.sample(straight, num_cards)
    assert main.return_winner(a, b) == a, 'full house beats a straight'

def test_full_house_vs_three_kind():
    a = random.sample(full_house, 5)
    b = random.sample(three_kind, 5)
    assert main.return_winner(a, b) == a, 'full house beats a three_kind'

def test_full_house_vs_one_pair():
    a = random.sample(full_house, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'full house beats a one_pair'

def test_full_house_vs_high_card():
    a = random.sample(full_house, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'full house beats a high_card'


def test_flush_vs_straight():
    a = random.sample(flush, num_cards)
    b = random.sample(straight, num_cards)
    assert main.return_winner(a, b) == a, 'flush beats a straight'

def test_flush_vs_three_kind():
    a = random.sample(flush, 5)
    b = random.sample(three_kind, 5)
    assert main.return_winner(a, b) == a, 'flush beats a three_kind'

def test_flush_vs_one_pair():
    a = random.sample(flush, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'flush beats a one_pair'

def test_flush_vs_high_card():
    a = random.sample(flush, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'flush beats a high_card'

def test_straight_vs_three_kind():
    a = random.sample(straight, 5)
    b = random.sample(three_kind, 5)
    assert main.return_winner(a, b) == a, 'straight beats a three_kind'

def test_straight_vs_one_pair():
    a = random.sample(straight, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'straight beats a one_pair'

def test_straight_vs_high_card():
    a = random.sample(straight, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'straight beats a high_card'

def test_three_kind_vs_one_pair():
    a = random.sample(three_kind, num_cards)
    b = random.sample(one_pair, num_cards)
    assert main.return_winner(a, b) == a, 'three of a kind beats a one_pair'

def test_three_kind_vs_high_card():
    a = random.sample(three_kind, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'three of a kind beats a high_card'

def test_one_pair_vs_high_card():
    a = random.sample(one_pair, num_cards)
    b = random.sample(high_card, num_cards)
    assert main.return_winner(a, b) == a, 'one pair beats a high_card'


README_CONTENT_CHECK_FOR = [
    'return_n_cards',
    'find_rank',
    'return_winner',
    ]

CHECK_FOR_THINGS_NOT_ALLOWED = []

def test_doc_return_n_cards():
    assert main.return_n_cards.__doc__ , 'Return n cards function has no docstring'

def test_doc_find_rank():
    assert main.find_rank.__doc__ , 'find rank function has no docstring'

def test_doc_return_winner():
    assert main.return_winner.__doc__ , 'return winner function has no docstring'

def test_doc_create_deck():
    assert main.create_deck.__doc__ , 'create deck function has no docstring'

def test_annotations_return_n_cards():
    assert main.return_n_cards.__annotations__ , 'Return n cards function has no annotations'

def test_annotations_find_rank():
    assert main.find_rank.__annotations__ , 'find rank function has no annotations'

def test_annotations_return_winner():
    assert main.return_winner.__annotations__ , 'return winner function has no annotations'

def test_annotations_create_deck():
    assert main.create_deck.__annotations__ , 'create deck function has no annotations'


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for count, space in enumerate(spaces):
        assert len(space) % 4 == 2, f"Your script contains misplaced indentations at \
n'th postion {count+1} starting \n with {space}"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
