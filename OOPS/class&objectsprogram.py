#create a class for student and create one object
class Student:
    def m1(self):
      print("welcome")
s = Student()
s.m1()


#create a patient class and create 2 patient objects with values pno=1, 
#pname=ramesh, disease = fever. pno=2, pname=suresh, disease=cold. 
#This requires students to create init method also with appropriate parameters.
class Patient:
    def setDetails(self, pno, pname, disease):
        self.pno = pno
        self.pname = pname
        self.disease = disease
    def display(self):
        print("Patient No:", self.pno)
        print("Patient Name:", self.pname)
        print("Disease:", self.disease)
        print("-" * 20)
p1 = Patient()
p2 = Patient()
p1.setDetails(1, "Ramesh", "Fever")
p2.setDetails(2, "Suresh", "Cold")
p1.display()
p2.display()
