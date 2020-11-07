print("Hello world!")
a = 5
print(a)

PI = 3.14
print(PI)

list = [1, 2, 3]
print(list)

tuple = (10, 20, 30)
print(tuple)

dict = {'foo': 2, 'bar': 3}
print(dict)

if a > 5:
    print(a)
else:
    print('else')

while a < 10:
    print(a)
    a += 1

for n in range(3):
    print(n)

for v in tuple:
    print(v)


def abc(a: int, b: int) -> int:
    return a + b


print(abc(1, 3))


class MyClass:
    def __init__(self, value):  # コンストラクタ
        self.value = value

    def abc(self):
        return self.value * self.value


obj = MyClass(5)
print(obj.abc())

if __name__ == '__main__':
    print(abc(5, 7))
