class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        return self.a + other.a

obj1= A(1)
obj2= A(2)

print(A.__add__(obj1, obj2))
print(obj1.__add__(obj2))

