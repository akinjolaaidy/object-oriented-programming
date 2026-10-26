class student :
    grade = 10
    name = "John"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("my name is",self.name)
        print("I study in Grade",self.grade)


ob = student()
ob.introduction()
ob.details()