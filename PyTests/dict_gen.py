attributes = ['name', 'dob', 'gender']

values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]

# d = [
#     dict(zip(attributes, value))
#     for idx, value in enumerate(values)
# ]

d = [
    {k:value[i] for i,k in enumerate(attributes)}
    for _, value in enumerate(values)
]

print(d)