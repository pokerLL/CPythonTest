import cProfile
import pstats

def func1():
    for i in range(1000000):
        pass

def func2():
    for i in range(2000000):
        pass

def main():
    for i in range(5):
        func1()
    for i in range(3):
        func2()

if __name__ == '__main__':
    cProfile.run('main()', 'result.stats')
    p = pstats.Stats('result.stats')
    p.strip_dirs().sort_stats('cumulative').print_stats()

