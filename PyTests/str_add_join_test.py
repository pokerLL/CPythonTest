import random
import time

def test(list_len):
    l = []
    for i in range(list_len):
        # l.append(''.join([str(random.randint(1,10)) for _ in range(random.randint(1,20))]))
        l.append(str(i))
    print(f'len(l): {len(l)}')

    start = time.time()
    s1 = ''
    for i in l:
        s1 += i
    end = time.time()
    add_time = end - start
    print(f'add: {add_time}')

    start = time.time()
    s2 = ''.join(l)
    end = time.time()
    join_time = end - start
    print(f'join: {join_time}')

    print(f'add/join: {add_time/join_time}')

for i in range(0, 7):
    test(10**i)

""" 
len(l): 1
add: 7.152557373046875e-07
join: 9.5367431640625e-07
add/join: 0.75
len(l): 10
add: 2.1457672119140625e-06
join: 9.5367431640625e-07
add/join: 2.25
len(l): 100
add: 1.33514404296875e-05
join: 2.1457672119140625e-06
add/join: 6.222222222222222
len(l): 1000
add: 7.009506225585938e-05
join: 1.5974044799804688e-05
add/join: 4.388059701492537
len(l): 10000
add: 0.0007255077362060547
join: 0.0001995563507080078
add/join: 3.6356033452807646
len(l): 100000
add: 0.006604194641113281
join: 0.0031599998474121094
add/join: 2.089935113927871
len(l): 1000000
add: 0.08632159233093262
join: 0.028325557708740234
add/join: 3.0474807669646315
"""