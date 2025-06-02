class Grandparent:
    def legacy(self):
        print("Grandparent's legacy")

class Parent(Grandparent):
    def guide(self):
        print("Parent's guidance")

class Child(Parent):
    def future(self):
        print("Child's vision")

obj = Child()
obj.legacy()
obj.guide()
obj.future()
