#Classes and instances
#Attributes which are just variables of an object
class Dog:
  
  
  def __init__(self,name):
    self.name = name
   
   
   #This  now the instance methods
  def bark(self):
    print("Woof!")
    
  def showing_self(self):
    return self
  
  def get_adopted(self,owner_name):
    self.owner = owner_name
    pass
    
   


#Here we have three instances or objects
fido = Dog("Fido")
print(fido.get_adopted("Sophie"))
print(fido.owner)








