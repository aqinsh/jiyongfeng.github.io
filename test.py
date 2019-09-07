def test(s):
    ss = s.split()
    lenth = len(ss)
    if lenth > 3:
        for i in range(lenth-2):
            if ss[i].isalpha() and ss[i+1].isalpha() and ss[i+2].isalpha():
                break
                return True
    else:
        return False


s = "a bb1 cc 33 ccc"
print(test(s))
