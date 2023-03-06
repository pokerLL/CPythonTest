x = [[1,2,3]]
y =  x * 2
print(y)    # [[1, 2, 3], [1, 2, 3]]
print(y[0] is y[1]) # True
y[0].append(4)
print(y)    # [[1, 2, 3, 4], [1, 2, 3, 4]]