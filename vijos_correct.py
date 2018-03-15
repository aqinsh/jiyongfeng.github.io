def correct(text):
    text_list = list(text)
    text_new = []
    if text_list[0].islower():
        text_new.append(text_list[0].upper())
    else:
        text_new.append(text_list[0])
    for i in range(1, len(text_list)):
        text_new.append(text_list[i])
    if text_new[-1] != '.':
        text_new.append('.')
    return ''.join(text_new)


def first_word(text):
    old_list = list(text)
    j = []
    for i in range(len(old_list)):
        if old_list[i].isalpha():
            j.append(old_list[i])
            print(i)
    return ''.join(j)


def first_word2(text):
    """
        returns the first word in a given text.
        https://py.checkio.org/mission/first-word/solve/
    """
    m = text.lstrip(' ,.').split()[0]
    n = m.split('.')[0].split(',')[0]
    return n



def best_stock(data):
    """ 
    You are given the current stock prices. 
    You have to find out which stocks cost more. 
    https://py.checkio.org/mission/best-stock/
    """
    n = data.values()
    m = max(n)
    for i in data.keys():
        if data[i] == m:
            return i


def popular_words(text, words):
    """ 
    determine the popularity of certain words in the text
    https://py.checkio.org/mission/popular-words/solve/
     """
    new_text = (text.lower()).split()
    d = dict()
    sum = [0 for x in range(len(words))]
    for i in range(len(words)):
        for j in new_text:
            if words[i] == j.split(',')[0].split('.')[0]:
                sum[i] += 1
        d[words[i]] = sum[i]
    return d



