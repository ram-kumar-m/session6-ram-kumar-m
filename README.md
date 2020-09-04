# Assignment 6
``` python
vals = ['2', '3', '4', '5', '6', '7', '8',
        '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
```

**1.Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck - 50 pts**
``` python 
list(map(lambda x: x[0]+x[1], zip(suits*13, vals*4))) 
```
**2.Write a normal function without using lambda, zip, and map function to create 52 cards in a deck - 50 pts**
```python 
def create_deck(suits: list, vals: list) -> list:
    """Generate a deck of cards, with the given suits and vals.

    Args:
        suits (list): eg. cloves, spades etc..
        vals (list): 1, 2, jack etc..

    Returns:
        list: cloves1, spades2 etc.. 52 elements for a normal deck
    """
    deck = []
    for i in suits:
        for j in vals:
            deck.append(i+j)
    return deck
```
**Using List Comprehension**
```python
cards = [i+j for i in suits for j in vals]
```

# __Something like Poker__ 

Here's a little simulation of a game 'just like poker'.


This is an image of what beats what.

<p align='center'>
   <img src='images\6b1ff73716c14139c951241f3c1d7c46.jpg'>
</p>


### __Rules__:
1. You get dealt either 3, 4 or 5 cards. 
2. The person with the best set wins.
3. Since the chances of getting all the cards in the row makes for rounds where 
no one wins. *__If alteast half your cards match with any of the above. Your hand will get upgraded to that set__*.
> Since four of a kind and three of a kind shares half of their cards, you will only get a three of a kind if all your cards match with the three of a kind. ie *three of a kind only exists when you're drawing 5 cards and all the cards are the same as the three of a kind shown above.* 
<br>

## __Functions__:

### __return_n_cards__:
```python
    """Returns a list of n cards

    Args:
        n (int): Number of cards to return

    Returns:
        list: 'n' number of Shuffled Cards
    """
```
### __find_rank__:
```python 
    """Returns the rank of a hand. Better the hand, higher the rank
    for eg rank of full house < royal flush

    Args:
        a (list): hand of a player

    Returns:
        int: value associated with a hand.
    """
```
### __return_winner__
```python
    """Returns the winner of cards deemed winner

    Args:
        a (list): Cards of a
        b (list): Cards of b

    Returns:
        list: Winner, list , Cards of a / Cards of b

    """
```
> if both sets have equal rank it returns *'There are no winners in life, just Idiots.'*

## **Test Cases (Pytest)**
>The names of the tests are so that `'test_'` prefix is added to the function it tests, suffied by the what the test does.

### test_readme_exists
   Checks if there is a README.md file in the same folder.

### test_readme_contents
   Checks if the README.md file has alteast 500 words.

### test_readme_proper_description
   Checks if the required functions are present in the README.md file.

### test_readme_file_for_formatting
   Checks if there are adequete headings present in the README.md file.

### test_indentations
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

### test_function_name_had_cap_letter
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.
   
### ***Annotation tests***
tests if any of the functions have annotations:

1. `test_annotations_return_n_cards`
2. `test_annotations_find_rank`
3. `test_annotations_return_winner`
4. `test_annotations_create_deck`


### ***Doc String tests***
tests if any of these functions have doc strings
1. `test_doc_return_n_cards`
2. `test_doc_find_rank`
3. `test_doc_return_winner`
4. `test_doc_create_deck`

### test_check_compare_lists 
   Checks if the comapre lists function made to test other functions works as expected.

### test_lambda_map_zip_expression
   Checks if the single line expression using map zip and lambda to make a deck works as expected 

### test_create_deck
   Checks if the function made without using map zip lamda to make a deck works as expected

### ***Checks cards present as expected in each of the sets.***

1. `test_vals`
2. `test_suits`
3. `test_cards`
4. `test_royal_flush`
5. `test_straight_flush`
6. `test_four_kind`
7. `test_full_house`
8. `test_flush`
9. `test_straight`
10. `test_three_kind`
11. `test_one_pair`
12. `test_high_card`

### ***Validates the rank each of the sets.***
1. `test_precedence_royal_flush`
2. `test_precedence_straight_flush`
3. `test_precedence_four_kind`
4. `test_precedence_full_house`
5. `test_precedence_flush`
6. `test_precedence_straight`
7. `test_precedence_three_kind`
8. `test_precedence_one_pair`
9. `test_precedence_high_card`

### ***Tests winner function***
> Random choice of 3, 4, 5 cards are used.
> The function should return the winner, in this case the first set.
1. `test_royal_flush_vs_straight_flush`
2. `test_royal_flush_vs_four_kind`
3. `test_royal_flush_vs_full_house`
4. `test_royal_flush_vs_flush`
5. `test_royal_flush_vs_straight`
6. `test_royal_flush_vs_three_kind`
7. `test_royal_flush_vs_one_pair`
8. `test_royal_flush_vs_high_card`
9. `test_straight_flush_vs_four_kind`
10. `test_straight_flush_vs_full_house`
11. `test_straight_flush_vs_flush`
12. `test_straight_flush_vs_straight`
13. `test_straight_flush_vs_three_kind`
14. `test_straight_flush_vs_one_pair`
15. `test_straight_flush_vs_high_card`
16. `test_four_kind_vs_full_house`
17. `test_four_kind_vs_flush`
18. `test_four_kind_vs_straight`
19. `test_four_kind_vs_three_kind`
20. `test_four_kind_vs_one_pair`
21. `test_four_kind_vs_high_card`
22. `test_full_house_vs_flush`
23. `test_full_house_vs_straight`
24. `test_full_house_vs_three_kind`
25. `test_full_house_vs_one_pair`
26. `test_full_house_vs_high_card`
27. `test_flush_vs_straight`
28. `test_flush_vs_three_kind`
29. `test_flush_vs_one_pair`
30. `test_flush_vs_high_card`
31. `test_straight_vs_three_kind`
32. `test_straight_vs_one_pair`
33. `test_straight_vs_high_card`
34. `test_three_kind_vs_one_pair`
35. `test_three_kind_vs_high_card`
36. `test_one_pair_vs_high_card`



