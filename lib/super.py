#Super method is a built function in python that allows us to manipulate the attributes and methods of a superclass(parent) from the body of its subclass(child)

class User:
  
  def __init__(self,name):
    self.name  = name
   
  def log_in(self):
    print("User.login is called")
    self.logged_in = True
   

class Student(User):
  def __init__(self, name,grade):
    print("Student init called")
    super().__init__(name)
    self.grade = grade
  
  def log_in(self):
    print("Student log in function is called")
    super().log_in()
    self.in_class = True

guido = Student("Guido",10)
print(guido.log_in())
