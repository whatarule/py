
class Base:
    basevalue = "base"
    def spam(self):
        print("Base.spam()")
    def ham(self):
        print("ham")

class Derived(Base):
    def spam(self):
        print("Derived.spam()")
        self.ham()

derived = Derived()
derived.spam()
print("{0}".format(derived.basevalue))
derived.ham()


class A:
    def method(self):
        print("class A")

class B:
    def method(self):
        print("class B")

class C(A):
    def __method(self):
        print("class C")
    def methodP(self):
        self.__method()

class D(B,C):
    pass

a = A()
b = B()
c = C()
d = D()


a.method()
b.method()
c.method()
c.methodP()
d.method()

