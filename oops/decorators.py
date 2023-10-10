


class student:
    def _init_(self,name,age):
        self.name=name
        self.age=age
    @property
    def __get_name(self):
        return self.name
    @property
    def get_age(self):

        return self.age
obj=student("hari",22)

print(obj.get_name)
print(obj.get_age)