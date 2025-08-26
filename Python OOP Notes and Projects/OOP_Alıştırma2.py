#OOP 2
from abc import ABC, abstractmethod

class Person(ABC):

    @abstractmethod
    def displayInfo(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self,value):
        pass

    @name.deleter
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def age(self):
        pass

    @age.setter
    @abstractmethod
    def age(self,value):
        pass

    @age.deleter
    @abstractmethod
    def age(self):
        pass

class Student(Person):
    count = 0

    def __init__(self,name,age,ID):
        self.__name = name
        self.__age = age
        self.__ID = ID
        Student.count += 1

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, ID: {self.__ID}"

    @classmethod
    def getCount(cls):
        return cls.count

    def displayInfo(self):
        return f"Name: {self.__name}, Age: {self.__age}, ID: {self.__ID}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if not value:
            raise ValueError("İsim Boş Olamaz")
        self.__name = value

    @name.deleter
    def name(self):
        self.__name = None
        print("Name Attribute'si Silinmiştir")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if not value:
            raise ValueError("Yaş Boş Olamaz")
        self.__age = value

    @age.deleter
    def age(self):
        self.__age = None
        print("Age Attribute'si Silinmiştir")

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self,value):
        if not value:
            raise ValueError("ID Boş Olamaz")
        self.__ID = value

    @ID.deleter
    def ID(self):
        self.__ID = None
        print("ID Attribute'si Silinmiştir")

class Teacher(Person):
    count = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.__students =[]
        Teacher.count += 1

    @classmethod
    def getCount(cls):
        return cls.count

    def displayInfo(self):
        studentsName = [item.name for item in self.__students]
        return f"Name: {self.__name}, Age: {self.__age}\nStudents: {studentsName}"

    def addStudents(self,value):
        self.__students.append(value)

    def updateStudents(self,Name,value):
        if not value:
            raise ValueError("Students Boş Olamaz")
        for i in range(len(self.__students)):
            if self.__students[i].name == Name:
                self.__students[i] = value
                print(f"{Name} isimli öğrenci yerine {value.name} isimli öğrenci başarıyla eklendi")
                return
        else:
            raise ValueError(f"{Name} isminde bir öğrenci bulunamadı")

    def __setitem__(self,index,value):
        self.__students[index] = value
    def __getitem__(self,index):
        return self.__students[index]
    def __delitem__(self,index):
        del self.__students[index]


    def __len__(self):
        return len(self.__students)


    def __repr__(self):
        studentsName = [item.name for item in self.__students]
        return f"Name: {self.__name!r}, Age: {self.__age!r}\nStudents: {studentsName!r}"


    def __iter__(self):
        self.index = 0
        return self
    def __next__(self):
        if(self.index >= len(self.__students)):
            raise StopIteration
        v = self.__students[self.index]
        self.index+= 1
        return v

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("İsim Boş Olamaz")
        self.__name = value

    @name.deleter
    def name(self):
        self.__name = None
        print("Name Attribute'si Silinmiştir")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not value:
            raise ValueError("Yaş Boş Olamaz")
        self.__age = value

    @age.deleter
    def age(self):
        self.__age = None
        print("Age Attribute'si Silinmiştir")

    @property
    def students(self):
        studentsName = [item.name for item in self.__students]
        return studentsName

    @students.setter
    def students(self,value):
        if not value:
            raise ValueError("Students Boş Olamaz")
        self.__students = value

    @students.deleter
    def students(self):
        self.__students = []
        print("Student Listesi Boşaltılmıştır")



s1 = Student("Furkan",19,2364933)
s2 = Student("Miray",17,1234567)
s3 = Student("Berat",14,9876543)
t1 = Teacher("Yeliz",37)
t1.addStudents(s1)
t1.addStudents(s2)

print(t1.displayInfo())
print()

t1.updateStudents("Miray",s3)
print()

print(t1.displayInfo())

print()
print(f"Okulda Bulunan Toplam Öğrenci Sayısı: {Student.getCount()}")
print(f"Okulda Bulunan Toplam Öğretmen Sayısı: {Teacher.getCount()}")
print(f"{t1.name} Öğretmenin Öğrencilerinin Sayısı: {len(t1)}")

print()
print(f"{t1.name} Öğretmeinin Öğrencilerini İsimleri:")
for item in t1:
    print(item.name)




