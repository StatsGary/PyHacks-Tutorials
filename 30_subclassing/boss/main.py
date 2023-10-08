from BossClasses import Boss, BadBoss, GoodBoss

# Initialise a boss object
gary = GoodBoss("Gary", "Positive", "Helpful", "Smiling / Happy")

print(gary.attitude)
print(gary.get_attitude())
print(gary.nurture_talent)

andrew = BadBoss('Andrew', "Passive Aggressive", 'Self serving', 'Stern')
print(andrew.get_attitude())
print(andrew.face)
print(andrew.hoard_praise())
print(andrew.yell())