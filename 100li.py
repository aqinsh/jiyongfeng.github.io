
l = int(input('Please input the total count of this month:'))
sum = 0
if l <= 100000:
    sum = l*0.1
elif l <= 200000:
    l -= 100000
    sum = 10000+l*0.075
elif l <= 400000:
    l -= 200000
    sum = 17500+l*0.05
elif l <= 600000:
    l -= 400000
    sum = 27500+l*0.03
elif l <= 1000000:
    l -= 600000
    sum =33500+l*0.015
else:
    l -= 1000000
    sum = 39500+l*0.01
print(sum)


