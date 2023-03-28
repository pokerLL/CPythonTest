import re

# 匹配一个由字母和数字组成的字符串，其中字母部分用括号捕获
LETTER = r'(?P<letter>[a-zA-Z]+)'
DIGIT = r'(?P<digit>\d+)'
pattern = re.compile('|'.join([LETTER, DIGIT]))
text = 'hello123world456'

scanner = pattern.scanner(text)

g = scanner.match()
print(g.group())            # hello
print(g.groups())           # ('hello', None)
print(g.groupdict())        # {'letter': 'hello', 'digit': None}
print(g.start())            # 0
print(g.end())              # 5
print(g.lastgroup)          # letter
print(g.group('letter'))    # hello
print(g.group('digit'))     # None

print('===============')
while g: # 赶紧期待3.8的:=表达式
    print(g.lastgroup, g.group())
    g = scanner.match()
"""
letter hello
digit 123
letter world
digit 456
"""
print('===============')

ls = pattern.findall(text)
print(ls)                   # [('hello', ''), ('', '123'), ('world', ''), ('', '456')]
