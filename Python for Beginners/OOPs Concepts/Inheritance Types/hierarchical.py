class Parent:
    def values(self):
        print("Parent: Honest and hardworking")

class Child1(Parent):
    def skill1(self):
        print("Child1: Good at coding")

class Child2(Parent):
    def skill2(self):
        print("Child2: Good at design")

obj1 = Child1()
obj2 = Child2()

obj1.values()
obj1.skill1()

obj2.values()
obj2.skill2()
