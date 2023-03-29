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

"""
Tue Mar 28 18:23:46 2023    result.stats

         12 function calls in 0.259 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.259    0.259 {built-in method builtins.exec}      
        1    0.000    0.000    0.259    0.259 <string>:1(<module>)
        1    0.000    0.000    0.259    0.259 cprofile_test_pstats.py:12(main)     
        3    0.149    0.050    0.149    0.050 cprofile_test_pstats.py:8(func2)     
        5    0.110    0.022    0.110    0.022 cprofile_test_pstats.py:4(func1)     
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


"""