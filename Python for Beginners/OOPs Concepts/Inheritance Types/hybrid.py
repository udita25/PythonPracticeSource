class Base:
    def base_func(self):
        print("Base class")

class A(Base):
    def func_a(self):
        print("Class A")

class B(Base):
    def func_b(self):
        print("Class B")

class C(A, B):
    def func_c(self):
        print("Class C")

obj = C()
obj.base_func()
obj.func_a()
obj.func_b()
obj.func_c()
