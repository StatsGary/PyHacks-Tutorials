# =============================================================================
# Title             PyHacks - Classes
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      12/07/2021
# =============================================================================

# Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

class simple_example:
    x = 10
    
# Use the class, or instantiate, to create objects of the class

new_obj = simple_example()
print(new_obj)

# This does not have much use, but shows how to create a simple object from a class
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Classes can also contain Object Methods
class transformer:
    """"Class to represent a Transformer object
    
    Attributes: 
        name (str): The name of the transformer
        special_move (str): The Transformer's special move
        damage (int): Damage taken in battle. May be zero. 
    
    """
    def __init__ (self, name, special_move, damage):
        #Constructor objects
        self.name = name
        self.special_move = special_move
        self.damage = damage
        self.damage_track = []
        
    def damage_added(self, damage_taken):
        if damage_taken > 0:
            self.damage += int(damage_taken)
            self.damage_level()
            self.damage_track.append(damage_taken)
            
    def damage_reduced(self, damage_taken):
        if damage_taken > 0:
            self.damage -= int(damage_taken)
            self.damage_level()
            self.damage_track.append(-damage_taken)
            
    def damage_level(self):
        if self.damage == 100:
            print("The transformer has been defeated!")
        else:
            print("The current damage level is {}".format(self.damage))
            
    def get_damage_list(self):
        for list_item in self.damage_track:
            if list_item <0:
                print("Health restored to {} transformer. Value:{}".format(self.name, list_item))
            else:
                print("Damage added to {} transformer. Value: {}.".format(self.name, 
                                                                          list_item))


# Create the Transformer object      
if __name__=='__main__':
    Bumblebee = transformer("Bumblebee", "Stingshot", 0)
    Bumblebee.damage_added(40)
    # Show with health bonus
    Bumblebee.damage_reduced(40)
    # Add more 
    Bumblebee.damage_added(100)
    Bumblebee.get_damage_list()
    
       
        
        