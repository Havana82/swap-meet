from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, condition=0, fabric= "Unknown", age= 0):
        super().__init__(id, condition,age)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        type = self.get_category()
        return f"An object of type {type} with id {self.id}. It is made from {self.fabric} fabric."