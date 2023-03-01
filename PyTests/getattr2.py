class Message():
    def __init__(self, note):
        self.note = note

    def remove_note(self):
        del self.note

    def get_note(self):
        return self.note

    def __setattr__(self, key, value):
        print("setAttr key = {},value = {}".format(key, value))
        # 如果这里使用了这个方法,那么必须明确的使用dict这个方法,将属性保存在其中
        self.__dict__[key] = value

    def __getattr__(self, item):
        print("getAttr item = {}".format(item))
        # 当属性不存在的时候会调用这个方法;
        return "属性不存在"

    def __delattr__(self, item):
        print("delattr item = {}".format(item))
        # 从字典里面删除属性
        self.__dict__.pop(item)


def main():
    msg = Message("www.baidu.com")
    print("获取存在的属性 {}".format(msg.get_note()))
    print("获取不存在的属性 {}".format(msg.contant))
    msg.remove_note()


if __name__ == '__main__':
    main()

# setAttr key = note,value = www.baidu.com
# 获取存在的属性 www.baidu.com
# getAttr item = contant
# 获取不存在的属性 属性不存在
# delattr item = note
