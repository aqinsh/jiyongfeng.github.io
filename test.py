def test(s):
    ss = s.split()
    lenth = len(ss)
    if lenth > 3:
        for i in range(lenth-2):
            if ss[i].isalpha() and ss[i+1].isalpha() and ss[i+2].isalpha():
                break
                print("good!")
                # return True
        
        print("not good!")
    else:
        print("bad!")
        # return False


s11 = "a bb1 cc"
test(s11)
