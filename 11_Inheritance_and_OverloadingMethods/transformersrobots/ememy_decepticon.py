import random

class Decepticon():
    def __init__ (self, name, transformation_type, damage_points=0, lives=1):
        #Constructor objects
        self.name = name
        self.transformation_type = transformation_type
        self.damage_points = damage_points
        self.lives = lives
        self.alive = True
               
    def take_damage(self, damage):
        remaining_damage_points = self.damage_points - damage
        if remaining_damage_points >=0:
            self.damage_points = remaining_damage_points
            print("The Decepticon {} took {} damage and has {} health points remaining".format(self.name,damage, self.damage_points))
        else:
            self.lives -=1
            if self.lives >0:
                print("{0.name} lost a life".format(self))
            else:
                print("{0.name} is dead.".format(self))
                # Make the boolean switch equal False
                self.alive = False

    def __str_(self):
        return "Name: {0.name}, Lives: {0.lives}, Damage Points: {0.damage_points}".format(self)

# Inherit properties of the Decepticon 

class Predicon(Decepticon): #Predicons descend from Deceptions
    def __init__(self, name, transformation_type):
        #super(Decepticon, self).__init__(name=name, lives=1, damage_points=45)
        super().__init__(name=name, transformation_type=transformation_type, lives=1, damage_points=45)

    # Extend the base class it is inheriting from to add beast mode
    def beast_mode(self, beast_mode):
        beast_mode = beast_mode
        print("Beast mode is {}".format(beast_mode))

class Seeker(Decepticon):
     def __init__(self, name, transformation_type):
         super().__init__(name=name, transformation_type=transformation_type, lives=1, damage_points=67)

    # Create a new method to add a defense method to the seeker to defend some attacks
     def defends(self):
        if random.randint(1,3)==3:
            print("[Defends] {0.name} defends against the attack".format(self))
            return True
        else:
            return False

    # Override our main super class i.e. Decepticon to allow all 
    # Decepticons in the bunch to be able to defend attacks
     def take_damage(self, damage):
        if not self.defends():
            super().take_damage(damage=damage)

