from utils import debug

@debug
def fun(*args):
    p = []
    for q in args:
        p.append(q)
    print(f'{args}')
    return p


fun(*tuple([1,2,3,4]))