
class Base():
    prop1='Something'
    __prop2='Somtehing2'


class Derived(Base):
   pass

obj=Derived()

print(obj.prop1)
print(obj.prop2)    # error verir cunki miras olaraq oturulmeyib



