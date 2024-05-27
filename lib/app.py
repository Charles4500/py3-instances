#Object oriented programming 
class Item:
    #Class
    pay_rate = 0.8 #The pay rate after 20% discount
    
    def __init__(self,name = str, price = float ,quantity = 0):
        #Run the validations to the received arguments
        assert price >= 0 
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        pass

#Instances
item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)