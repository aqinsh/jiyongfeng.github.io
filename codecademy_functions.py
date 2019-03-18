def factorial(x):
    total = 1
    for i in range(1, x + 1):
        total *= i
    return total


def is_prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
         #   break
    else:
        return True


def reverse(text):
    reverse_list = []
    str_lenth = len(text)
    return_reverse = ''
    for i in range(str_lenth):
        reverse_list.append(text[str_lenth - 1])
        str_lenth -= 1
        return_reverse = return_reverse + reverse_list[i]
    return return_reverse


def anti_vowel(text):
    text_list = []
    for i in text:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            if i not in ['A', 'E', 'I', 'O', 'U']:
                text_list.append(text[text.index(i)])
    return ''.join(text_list)


def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    lower_word = word.lower()
    total_score = 0
    for i in lower_word:
        total_score += score[i]
    return total_score


def censor(text, word):
    # Write a function called censor that takes
    #  two strings, text and word, as input. It
    # should return the text with the word you
    # chose replaced with asterisks.
    text_split = text.split()
    for i in text_split:
        if i == word:
            text_split[text_split.index(word)] = '*' * len(word)
    return ' '.join(text_split)


def count(sequence, item):
    # Return the number of times the item occurs in the list
    sum_item = 0
    for i in sequence:
        if i == item:
            sum_item += 1
    return sum_item


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def purify(num_list):
    my_list = []
    for i in num_list:
        if is_even(i):
            my_list.append(i)
    return my_list


def remove_duplicates(parameter_list):
    result_list = []
    for i in parameter_list:
        if i not in result_list:
            result_list.append(i)
    return result_list


def median(sequence_list):
    sorted_list = sequence_list.sort()
    location_value = 0
    list_lenth = len(sequence_list)
    if list_lenth % 2 == 0:
        location_value = (
            sequence_list[list_lenth / 2 - 1] + sequence_list[list_lenth / 2]) / (2.0)
    else:
        location_value = sequence_list[(list_lenth + 1) / 2 - 1]
    return location_value


x = [1]
y = 7
for i
print(censor(x, y))
