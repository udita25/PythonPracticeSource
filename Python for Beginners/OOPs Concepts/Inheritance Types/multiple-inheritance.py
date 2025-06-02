class Father:
    def skill(self):
        print("Father: Skilled in carpentry")

class Mother:
    def talent(self):
        print("Mother: Talented in painting")

class Child(Father, Mother):
    def interest(self):
        print("Child: Loves technology")

obj = Child()
obj.skill()
obj.talent()
obj.interest()
