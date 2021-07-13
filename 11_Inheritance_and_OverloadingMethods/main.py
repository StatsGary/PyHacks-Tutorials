from transformersrobots.transformer_autobot import Autobot
from transformersrobots.ememy_decepticon import Decepticon, Predicon, Seeker

def create_line_break(centre_text,line_num):
    line_num = 40
    print(str("-" * line_num + " " + centre_text + " " + "-"*line_num))

#Use Autobot class
create_line_break("Autobot", 40)
optimus = Autobot("Optimus Prime", "HGV")
print("The transformation type for Optimius is {}".format(optimus.trans_type)) # Access the transformation type property
optimus.score += 40
optimus.lives -= 1
print(optimus)

# Use Decepticon object
create_line_break("Decepticon", 30)
megatron = Decepticon("Megatron", "Tank", 30, 1)
# Play with decepticon object
megatron.take_damage(29)
print(megatron)
megatron.take_damage(1)
print(megatron)
megatron.take_damage(2)
print(megatron)

""" #Inheritsll the parameters from """
create_line_break("Predicon", 40)
scorpionox = Predicon("Scorpinox", "Scorpion")
scorpionox.take_damage(20)
scorpionox.beast_mode = "Scorpion"
print(scorpionox.beast_mode)
print(scorpionox) 


starscream = Seeker("Starscream", "Fighter Jet")
#Without overriding super method
while starscream.alive:
    if not starscream.defends():
        starscream.take_damage(1)
        print(starscream)

