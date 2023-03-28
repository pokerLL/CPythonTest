import cProfile
import time

def func1():
    time.sleep(1)

def func2():
    time.sleep(2)

def main():
    for i in range(5):
        func1()
    for i in range(3):
        func2()

if __name__ == '__main__':
    cProfile.run('main()')

"""
         20 function calls in 11.080 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.079   11.079 <string>:1(<module>)
        1    0.000    0.000   11.079   11.079 cprofile_test.py:10(main)
        5    0.000    0.000    5.049    1.010 cprofile_test.py:4(func1)
        3    0.000    0.000    6.031    2.010 cprofile_test.py:7(func2)
        1    0.000    0.000   11.080   11.080 {built-in method builtins.exec}      
        8   11.079    1.385   11.079    1.385 {built-in method time.sleep}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""