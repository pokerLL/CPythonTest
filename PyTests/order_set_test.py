s = set()

items = (
    ('name', 'Gumby'),
    ('age', 42),
    ('height', 172),
    ('weight', 70)
)

for k,v in items:
    s.add(k)

for k in s:
    print(k)

s.add('name')

for k in s:
    print(k)
"""
height
name
weight
age
height
name
weight
age

"""