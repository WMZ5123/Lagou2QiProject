class Animal:
    def __init__(self, name, age, color, gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    def sound(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


class Cat(Animal):
    def __init__(self, name, age, color, gender, hair='短毛'):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.hair = hair

    def sound(self):
        print("猫会喵喵叫")

    def catch(self):
        print("猫会抓老鼠")


class Dog(Animal):
    def __init__(self, name, age, color, gender, hair='长毛'):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender
        self.hair = hair

    def sound(self):
        print("狗会汪汪叫")

    def watch(self):
        print("狗会看家")


if __name__ == "__main__":
    cat = Cat('皮皮', 2, '橘色', '母')
    cat.catch()
    print(f"{cat.name},{cat.age}岁,{cat.color},{cat.gender}猫,{cat.hair},抓到了老鼠")

    dog = Dog('旺财', 2, '黑色', '公')
    dog.watch()
    print(f"{dog.name},{dog.age}岁,{dog.color},{dog.gender}狗,{dog.hair}")
