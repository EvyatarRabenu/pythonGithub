from second_test import f1
x = 10
print(x)

y = 20
print(y)

z = 30
print(z)

t = 20
print(t)



f1()



class Person:
    def __init__(self, name, age):
        if age < 0:
            raise ValueError("Age cannot be negative!")
        if age > 120:
            raise ValueError("Age is too high!")

        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"



try:
    person2 = Person("Bob", -5)
except ValueError as e:
    print(f"Error: {e}")