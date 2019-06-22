import textwrap


def swap_case(s):
    """ 
    You are given a string and your task is to swap cases. 
    In other words, convert all lowercase letters to uppercase
    letters and vice versa. 
    """
    new_s = []
    for i in s:
        if i.islower():
            new_s.append(i.upper())
        elif i.isupper():
            new_s.append(i.lower())
        else:
            new_s.append(i)
    return ''.join(new_s)


def split_and_join(line):
    """ 
    You are given a string. Split the string on a " " (space) 
    delimiter and join using a - hyphen.
    """
    return '-'.join(line.split(' '))


def print_full_name(a, b):
    print("Hello {firstname} {lastname}! You just delved into python.".format(
        firstname=a, lastname=b))


def mutate_string(string, position, character):
    """ 
    Read a given string, change the character at a 
    given index and then print the modified string.

    Args:
        string: given a string
        position: the position where need to change
        character: the character that to be changed

    Returns:
        the modified string
    """
    return string[:position] + character + string[(position + 1):]


def count_substring(string, sub_string):
    """ 
    the user enters a string and a substring. You have to 
    print the number of times that the substring occurs in
    the given string.
     """
    count = 0
    while sub_string in string:
        count += 1
        string = string[(string.index(sub_string)+1):]
    return count


def wrap(string, max_width):
    """ 
    You are given a string  and width . 
    Your task is to wrap the string into a paragraph of width .
    """
    return textwrap.fill(string, max_width)


def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(
            i, width=width))


def print_rangoli(size):
    """ 
    You are given an integer, . Your task is to print an alphabet rangoli of size . 
    (Rangoli is a form of Indian folk art based on creation of patterns.)
    """
    for i in range(size):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))

    for i in range(size-1):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(size-i-1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))


def capitalize(string):
    return ' '.join(i.capitalize() for i in string.split(' '))


def minion_game(string):
    l = ['A', 'E', 'I', 'O', 'U']
    s = list(string)
    total_stuart = total_kevin = 0
    for i in range(len(s)):
        if s[i] in l:
            total_kevin += len(s) - i
        else:
            total_stuart += len(s) - i
    if total_stuart > total_kevin:
        print('Stuart',total_stuart)
    elif total_stuart < total_kevin:
        print('Kevin',total_kevin)
    else:
        print('Draw')   


def average(array):
    """ 
    Introduction to Sets
    https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
     """
    return sum(set(array)) / len(set(array))
    
