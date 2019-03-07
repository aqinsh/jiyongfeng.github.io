def furthestDistance(arr):
    #Code goes here
    fur_distance = 0.0
    for i in arr:
        for j in arr:
            distance = sqrt((i[0] - j[0])^2 + (i[1] - j[1])^2)
            fur_distance = distance if distance > fur_distance
    return fur_distance

array1 =[[3,8],[10,4]]
print(furthestDistance(array1))