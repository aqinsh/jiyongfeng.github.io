def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    if begin in text:
        begin_index = text.find(begin) + len(begin)
    else:
        begin_index = 0
    if end in text:
        end_index = text.find(end)
    else:
        end_index = len(text)
    
    return text[begin_index:end_index]

s = between_markers('What is >apple<', '>', '<')
print(s)
