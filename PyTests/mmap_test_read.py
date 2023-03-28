import mmap

"""
abcdefeg
1234567
lei
"""
# with open('C:\Workspace\Program\CPythonTest\PyTests\example.txt','r') as f:
with open('example.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
        # 切片操作
        print(mm[:10])
        print("###############")
        
        # 索引操作
        print(mm[10])
        print("###############")

        # 迭代操作
        for byte in mm[:5]:
            print(byte)
        

"""
b'abcdefeg\r\n'
###############
49
###############
b'a'
b'b'
b'c'
b'd'
b'e'
b'f'
b'e'
b'g'
b'\r'
b'\n'
b'1'
b'2'
b'3'
b'4'
b'5'
b'6'
b'7'
b'\r'
b'\n'
b'l'
b'e'
b'i
"""
