import struct


"""
`struct.pack(format, v1, v2, ...)`: 根据给定的格式`format`将一组值打包成二进制数据，并返回一个包含打包数据的bytes对象。其中，`format`是一个字符串，用于指定打包的数据类型及其顺序；`v1, v2, ...`是要打包的数据值。
`struct.unpack(format, buffer)`: 根据给定的格式`format`从二进制数据中解包出一组数据，并返回一个包含解包数据的元组。其中，`format`和`buffer`分别表示解包的数据格式和数据源。

在下面的示例中，我们使用`pack`函数将一个字符串、一个整数和一个浮点数打包成二进制数据，然后使用`unpack`函数从这个二进制数据中解包出这三个值，并将它们打印出来。`'3s i f'`是`pack`和`unpack`中的格式字符串，表示打包和解包的数据类型及其顺序。`3s`表示一个长度为3的字符串，`i`表示一个整数，`f`表示一个浮点数。
"""

# 将一组值打包成二进制数据
data = struct.pack('3s i f', b'abc', 100, 3.14)

# 解包出一组数据
values = struct.unpack('3s i f', data)

# 打印解包后的数据
print(values)  # 输出: (b'abc', 100, 3.140000104904175)
