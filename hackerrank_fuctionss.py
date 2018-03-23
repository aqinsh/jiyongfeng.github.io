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


