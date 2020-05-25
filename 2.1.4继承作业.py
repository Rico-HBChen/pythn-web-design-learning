#coding:utf-8

class SchoolKid:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def change_name(self,newname):
        self.name = newname
        return self.name

    def change_age(self,newage):
        self.age = newage
        return self.age

class ExaggeratingKid(SchoolKid):
    def __init__(self,name,age):
        SchoolKid.__init__(self,name,age)
        

    def get_age(self):
        newage = self.age + 2
        return newage

sc_father_class = SchoolKid('rico',12)
print(sc_father_class.get_age())
print(sc_father_class.get_name())

ex_son_class = ExaggeratingKid('chb',12)
print(ex_son_class.get_age())
print(ex_son_class.get_name())