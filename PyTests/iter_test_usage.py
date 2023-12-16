""" 
判断一个序列是否是另一个序列的子序列
例如：
    1. [1, 2, 3]是[1, 2, 3, 4, 5]的子序列
    2. [1, 2, 3]是[1, 2, 3]的子序列
    3. [1, 3, 5]是[1, 2, 3, 4, 5]的子序列
    4. [1, 5, 3]不是[1, 2, 3, 4, 5]的子序列
"""

def is_subseq(seq, subseq):
    """判断subseq是否是seq的子序列"""
    it = iter(seq)
    return all(i in it for i in subseq)

print(is_subseq([1, 2, 3, 4, 5], [1, 2, 3]))
print(is_subseq([1, 2, 3], [1, 2, 3]))
print(is_subseq([1, 2, 3, 4, 5], [1, 3, 5]))
print(is_subseq([1, 2, 3, 4, 5], [1, 5, 3]))

""" 
True
True
True
False
"""