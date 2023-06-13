import random
pityPurple = 1

def main():
    
    ans = int(input("How many rolls? : "))
    for i in range(0, ans):
        gacha()
        global pityPurple
        pityPurple += 1

    ans = input("Again or nah? yes / no : ").lower()
    if ans == "yes":
        main()
    elif ans == "no":
        print("Keep gambling, you will win.")
    else:
        print("What")

def gacha():
    chance = random.randint(1,100)
    global pityPurple
    if pityPurple == 10:
        chance = 3
        pityPurple = 0

    if chance == 1:
        print("GG! You got a 5* Character (1%)")
    elif chance <= 4:
        print("Cool, you got a 4* Character (3%)")
    elif chance <= 8:
        print("GG! You got a 5* Spell Card (4%)")
    elif chance <= 20:
        print("Cool, you got a 4* Spell Card (12%)")
    elif chance <= 60:
        print("You got a 3* Character (40%)")
    elif chance <= 100:
        print("You got a 3* Spell Card (40%)")
main()
