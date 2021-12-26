print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Story sections 

st_1 = 'You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n'
st_2 = 'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'
st_3 = "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
st_3a = "It's a room full of fire.\nGame Over."
st_3b = "You found the treasure! \nYou Win!"
st_3c = "You enter a room of beasts. \nGame Over."
st_3d ="You chose a door that doesn't exist. \nGame Over."
stu_2b = "You get attacked by an angry trout. \nGame Over."

#st = stage; sta = stage answer

sta_1 = input(st_1).lower()
if sta_1 == "left":
  sta_2 = input(st_2).lower()
  if sta_2 == "wait":
    sta_3 = input(st_3).lower()
    if sta_3 == "red":
      print(st_3a)
    elif sta_3 == "yellow":
      print(st_3b)
    elif sta_3 == "blue":
      print(st_3c)
    else:
      print(st_3d)
  else:
    print(stu_2b)
else:
  print("A tree falls down on you, leaving you paralysed from the neck down. No one helps you and you die of starvation. \nTHE END")