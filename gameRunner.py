import boardGenerator as gen

print("RULES:",
"\n- Enter Coordinates for shots",
"\n- ~ means an empty spot",
"\n- X means a hit shot",
"\n- # means a missed shot\n")

gens = int(input("How many ships would you like?\n"))
for i in range(1, gens+1):
    gen.gen_Ship(i)
cheat = False
if input("Would you like to inable cheats? (Y/N)\n") == "Y":
    gen.cheats()
    print("cheats enabled\n")
    cheat = True
gen.printboard()
shipDestroyed = 0
while True:
    shipDestroyed += gen.shoot()
    if shipDestroyed == gens:
        print("You win!")
        if cheat == True:
            print("But i know you cheated ... -_-")
        break