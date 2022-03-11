#I am going to create this random script to cover everything that I have learned so far about python
#For this, i will use something i love (comics, anime, cartoons) to make sense of everything

#these are variables holding a string value
#Each being the name of a power from the show as the value
#and the variable name being their ranger color
green_ranger = "Tommy"
white_ranger = "Tommy"
red_ranger = "Jason"
new_red_ranger = "Rocky"
black_ranger = "Zach"
new_black_ranger = "Adam"
yellow_ranger = "Trini"
new_yellow_ranger = "Aisha"
blue_ranger = "Billy"
pink_ranger = "Kimberly"

#these are variables holding a interger or a floating interger value
#each bring the name of a zord from the MMPR series
zero_Megazord = 0
dino_Megazord = 1
dragonzord = 2
dragonzord_Battlemode = 2.5
dino_Ultrazord = 3
white_Tigerzord = 2
thunder_Megazord = 4
mega_Tigerzord = 2.8
shogun_Megazord = 5
ninja_Megazord = 6

##Here i set variables to a boolean so that i use them in my comparision statements
megazord = True
ultrazord = True

#Here i am comparing the variable memory locations between the two variables using the "is" operator
print("Is tommy being the green ranger the same color as being the white ranger?")
print(bool(green_ranger is white_ranger))

#Here i am comparing the variable values between the two variables using the "==" operator
print("Is the green ranger and the white ranger in MMPR the same person?")
print(bool(green_ranger == white_ranger))

#Here i am comparing the variable memory locations between the two variables using the "is" operator
print("Is Jason being the red ranger the same as Rocky being the red ranger?")
print(bool(red_ranger is new_red_ranger))

#Here i am comparing the variable values between the two variables using the "==" operator
print("Is Jason and Rocky a leader even tho they are the same power ranger color?")
print(bool(red_ranger == new_red_ranger))

#Here i am adding two varaibles that hold a int value and compare it to another int using the "==" operator give me a true value
print("Is the Dino Megazord and the DragonZord combined equal the Dino Ultrazord?")
print(dino_Megazord + dragonzord == dino_Ultrazord)

#Here i am adding two varaibles that hold a int value and compare it to another int using the "==" operator giving me a false value
print("Is the Dino Megazord and the DragonZord Battle mode combined equal the Dino Ultrazord?")
print(dino_Megazord + dragonzord_Battlemode == dino_Ultrazord)

#Here i am using comparision operator ">,<,<=,>=" to compare the int values
print("Is having no megazord to fight a 20 foot tall monster greater than having no megazord?")
print(zero_Megazord > zero_Megazord)
print("Is having no megazord to fight a 20 foot tall monster not that greater than having no megazord?")
print(zero_Megazord < zero_Megazord)
print("Is having no megazord to fight a 20 foot tall monster the greater than or equal to having no megazord?")
print(zero_Megazord >= zero_Megazord)
print("Is having no megazord to fight a 20 foot tall monster the less than or equal to having no megazord?")
print(zero_Megazord <= zero_Megazord)

#Here i am comparing variables while using boolean operators "and, or, or none (not used)"
print("Is having the Dino Megazord and the Dragozord greater than having the Dino Ultrazord and Dragonzord in battle mode in a fight?")
print(dino_Megazord > dino_Ultrazord and dragonzord > dragonzord_Battlemode)
print("Is having the Dino Ultrazord and the Dragozord in Battle Mode greater than having the Dino megazord and Dragonzord in a fight?")
print(bool(dino_Ultrazord > dino_Megazord and dragonzord_Battlemode > dragonzord))


#Here i am bringing the the comparision and idendity operators together along with a boolean statement (if else)
print("Is having no megazord the same as having a Megazord?")
if zero_Megazord == megazord:
    print("This is a Zord!")
else:
    print("This is NOT a Zord. We gonna DIE!")

print("Is having the Dino Ultrazord classify as having an ultrazord to beat Lord Zedd's and Rita's most strongest monsters?")
if dino_Ultrazord == ultrazord:
    print("Oh shes a shinyyy zord")
else:
    print("Yikes, we are REALLY gonna DIE!")

print("If the Rangers summon the Shogun MegaZord and Alpha-5 summons no zord, is that enough for a fair fight between 2 or Zedd's and Rita's Monsters?")
if shogun_Megazord == megazord and zero_Megazord == ultrazord:
    print("Its time for Zedd and Rita's monster to go down!")
else:
    print("Yall must've not heard me the first time, we gonna DIE!")

print("If the rangers summon the Ninja Megazord or the Mega Tigerzord, as long as they have one zord for one of Rita's Monsters, should that be enough to take them down?")
if ninja_Megazord == ultrazord or mega_Tigerzord == zero_Megazord:
    print("WU TANG CLAN AINT NOTHING TO F WIT. Oops, this is a kid's show. Zedd, your monster's going down today")
else:
    print("ehh.......")
