class Person():
    # constrcutor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi my name is {self.name}")
        print(f"I am {self.age} year old")

person1 = Person("Tung", 11)
person2 = Person("Chau", 11)
person3 = Person("Anh Ky", 10)
person4 = Person("Khoi", 11)

person1.introduce()