def another_generator():
    yield 1
    yield 2

def my_generator():
    yield from another_generator()

for value in my_generator():
    print(value)