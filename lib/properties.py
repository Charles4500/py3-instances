

class Human:
  species = "Homo sapiens"
  
  def __init__(self,age):
    self.age = age
  
  def get_age(self):
      print("Retrieving age")
      return self._age
    
  def set_age(self,age):
    if (type(age) in (int,float)) and (0 <= age <= 120):
      print(f"Setting age to {age}")
      self._age = age 
    
    else :
      print ("Age must be a number between o  and 120")
      
   #Properties --> These are attributes controlled by methods 
  age = property(get_age,set_age) 
  
person = Human(age=67)
person.age = 0
person.age = False
person.age

  
    
 

