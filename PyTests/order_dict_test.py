d = dict()

items = (
    ('name', 'Gumby'),
    ('age', 42),
    ('height', 172),
    ('weight', 70)
)

for key, value in items:
    d[key] = value

for k,v in d.items():
    print(f'{k}: {v}')

d['age'] = 18

for k,v in d.items():
    print(f'{k}: {v}')

""" 
name: Gumby
age: 42
height: 172
weight: 70
name: Gumby
age: 18
height: 172
weight: 70
"""