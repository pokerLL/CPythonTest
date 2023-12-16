class TestMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f'cls: {cls} - name: {name} - bases: {bases} - attrs: {attrs}')
        if 'process' not in attrs and name != 'TestBase':
            raise AttributeError('process not found')
        else:
            print('process found')
        return super().__new__(cls, name, bases, attrs)


class TestBase(metaclass=TestMeta):
    pass


class Test(TestBase):
    def process(self):
        pass


t = Test()
