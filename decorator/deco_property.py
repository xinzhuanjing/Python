class Student:
    def __init__(self):
        self._age = None

    def get_age(self):
        print("Run when read the attribute")
        return self._age

    def set_age(self, age):
        print("Run when set the attribute")
        self._age = age

    def del_age(self):
        print("Run when delete the attribute")
        del self._age

    age = property(get_age, set_age, del_age, "Students' age")


student = Student()
print("Doc of age is %s" % Student.age.__doc__)
student.age = 18
print("Age of student: %s" % str(student.age))
del student.age


class Student:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        '''Students' age'''
        print("Run when read the attribute")
        return self._age

    @age.setter
    def age(self, age):
        print("Run when set the attribute")
        self._age = age

    @age.deleter
    def age(self):
        print("Run when delete the attribute")
        del self._age


student = Student()
print("Doc of age is %s" % Student.age.__doc__)
student.age = 18
print("Age of student: %s" % str(student.age))
del student.age
