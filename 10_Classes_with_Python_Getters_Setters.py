# =============================================================================
# Title             PyHacks - Classes  - Getters and Setters
# Author            Gary Hutson aka hutsons-hacks.info
# Date created      12/07/2021
# =============================================================================
import numpy as np

# Classes can also contain Object Methods
class transformer:
    def __init__ (self, name, special_move):
        #Constructor objects
        self.name = name
        self.special_move = special_move
        self._lives = 3
        self._level = 1
        self._score = 0
        
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
            self._score += int(change + np.random.randint(600, 1000))
            self._level = level
        else:
            print("The level cannot be less than 1.")
            
    # Use decorators to set this
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
            
    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)
    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
        
        
        
    


# Create the Transformer object      
if __name__=='__main__':
    Optimus = transformer("Optimus Prime", "Axe Blast")
    print(Optimus)
    Optimus.lives -= 2
    print(Optimus)
    Optimus.level += 1
    print(Optimus)
    Optimus.level += 1
    print(Optimus)
    
    
       
        
        
