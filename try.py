#coding=utf-8

class Person():
    hobby = "play game"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "my name is %s \nmy age is %d" % (self.name, self.age)

print(__name__, "yefy")

if __name__ == "__main__":
    person = Person('yefy', 24)
    print(person)
    print(dir(person))
    print(person.hobby)
    person1 = Person("panmin", 23)
    person1.hobby = "working"
    person1.hobby1 = "walking"
    print(person1.hobby1)