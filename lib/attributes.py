class Human:
  #Class attribute
  species = "Homo sapiens"
  
  #Instance attribute
  def __init__(self,name ):
    print(self)
    self.name = name
    print(name)
    pass
  
person1 = Human("Charles")
person2 = Human("Daisy")
print(person1.species)
# print(person1.name)


class BookStore:
  
  genre = "Programming books"
  
  def title(self):
    return "Clean codes"
  
  def author(self):
    return "David Know"
    pass


book = BookStore
print(book.genre)
print(book.title(""))
print(book.author(""))

class Electronics:
  
  sold_by = 'Amazon'
  
  def brand(self):
    return "Samsung"
  
  def watts(self):
    return 200
  
  def prices(self,price):
    return f"The price of this product is ${price}"
  pass


kitchen = Electronics
print(kitchen.sold_by)
print(kitchen.brand(''))

sitting = Electronics()
print(sitting.watts())
print(sitting.prices(1000))
