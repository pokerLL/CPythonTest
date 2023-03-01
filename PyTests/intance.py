class A:
    a = 1

    def __init__(self) -> None:
        self.a = 2

print(A.__dict__)
# {'__module__': '__main__', 'a': 1, '__init__': <function A.__init__ at 0x000001B21FFA9040>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
print(A().__dict__)
# {'a': 2}
print(A.__dict__)
# {'__module__': '__main__', 'a': 1, '__init__': <function A.__init__ at 0x000001B21FFA9040>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}