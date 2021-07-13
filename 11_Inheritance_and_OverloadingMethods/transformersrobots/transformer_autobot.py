import numpy as np

# Classes can also contain Object Methods
class Autobot:
    def __init__ (self, name, transformation_type):
        #Constructor objects
        self.name = name
        self._transformation_type = transformation_type
        self._lives = 3
        self._level = 1
        self.score = 0
               
    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >=0:
            self._lives = lives
        else:
            print("If negative lives, you are dead!")
            self._lives = 0
            
    def _get_level(self):
        return(self._level)
    
    def _set_level(self, level):
        if level > 0:
            change = level - self._level
            self.score += int(change + np.random.randint(600, 1000))
            self._level = level
        else:
            print("The level cannot be less than 1.")
            
    # Use decorators to set this
    @property
    def trans_type(self):
        return self._transformation_type
    
    @trans_type.setter
    def trans_type(self, trans_type):
        self._transformation_type = trans_type
            
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)

        

    
    
       
        
        