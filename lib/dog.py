#Class
class Dog:
      #Class attributes
      species = "Canis familiaris"
      def __init__(self,name,age):
        self.name = name
        self.age = age
        
      #instance methods
      def description(self,name,age):
        return f"This dog's name is {name} and its age is {age}"
  
  
  
      
rakes = Dog("Rakes",12)
print(rakes.description("Rakes",12))
boom = Dog("Boom",10)
print(boom.description("Boom",10))