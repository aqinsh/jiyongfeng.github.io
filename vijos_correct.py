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
             
x = first_word(',,, good morning ...')
print(x)
