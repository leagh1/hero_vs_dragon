import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))
try:
    hero_hp = int(input("how many hp does the hero have?"))
    dragon_hp = int(input("how many hp does the dragon have?"))
    hero_max_dmg = int(input("how much damage does the dragon sustain?"))
    dragon_max_dmg = int(input("how much damage does the hero sustain?"))

except ValueError:
    print("Please give me a proper number")
except:
    print("Some other exception i did not see coming")
else:
    print("The dragon with", dragon_hp, "hp attacks our hero with", hero_hp, "hp")

# add a While for an infinite block
while True:
    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    hero_hp = hero_hp-dragon_attack

    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    # add an if condition to check if the hero was killed by the dragon
    if hero_hp<=0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break

    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    dragon_hp = dragon_hp-hero_attack

    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    # add an if condition to check if the dragon was killed by the hero
    if dragon_hp<=0:
        print("Our valiant hero has slain the dragon!")
        break
    input("Round over. Press any key")
