# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())+1):
    # 1 = 1 * 1 , 1 = (10 ** 1 - 1) / 9
    # 121 = 11 * 11,11 = (10 ** 2 - 1) / 9

    print(((10 ** i - 1) // 9) ** 2)  # //:保证输出的是int而不是float类型
