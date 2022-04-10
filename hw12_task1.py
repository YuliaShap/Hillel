class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter


c = Counter()
c()
c()
c()
res = c()
print(res)


class IPAddress:
    def __init__(self, ip):
        self.ip = ip

    def __repr__(self):
        return f"IPAddress('{self.ip}')"


ip1 = IPAddress('10.1.1.1')
print(repr(ip1))


class Student(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student


print(Student.from_string('Ivan Ivanov'))


class Student(object):

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1


print(Student.is_full_name('Ivan Ivanov'))
print(Student.is_full_name('Ivan'))


class Human:
    """Человек, возраст которого не может быть больше 120 и меньше 0"""

    def __init__(self, age=0):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 120 >= age >= 0:
            self.__age = age
        else:
            self.__age = 0


h = Human(age=30)
h.age = 150
print(h.age)
