import mmap

# 打开文件并创建mmap对象
with open("example.txt", "r+b") as f:
    with mmap.mmap(f.fileno(), 0) as mm:
        print(mm[:])    # b'abcdefeg\r\n1234567\r\nlei'

        # 在mmap对象上修改文件内容
        mm[0:4] = b"1111"

        mm.flush()
        print(mm[:])    # b'1111efeg\r\n1234567\r\nlei'

        # 关闭mmap对象
        mm.close()