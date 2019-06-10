from collections import Counter

number_shoes = int(input("Please input the number of shoes:"))
number_size = Counter(map(int, input().split()))
number_customer = int(input("Please input the number of customers:"))

income = 0

for i in range(number_customer):
    size, price = map(int, input().split())
    if number_size[size]:
        print(number_size)
        print(number_size[size])
        income += price
        number_size[size] -= 1
print(income)
