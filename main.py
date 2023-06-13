import random
pityPurple = 1

def main():
    
    jawab = int(input("Lakukan gacha berapa kali? : "))
    for i in range(0, jawab):
        gacha()
        global pityPurple
        pityPurple += 1

    jawab = input("Gacha lagi gak bang? ya / tidak : ").lower()
    if jawab == "ya":
        main()
    elif jawab == "tidak":
        print("ok bang")
    else:
        print("wakaranai")

def gacha():
    chance = random.randint(1,100)
    global pityPurple
    if pityPurple == 10:
        chance = 3
        pityPurple = 0

    if chance == 1:
        print("Gokil dapet 5* Character (1%)")
    elif chance <= 4:
        print("Keren dapet 4* Character (3%)")
    elif chance <= 8:
        print("Gokil dapet 5* Spell Card (4%)")
    elif chance <= 20:
        print("Keren dapet 4* Spell Card (12%)")
    elif chance <= 60:
        print("Dapet 3* Character (40%)")
    elif chance <= 100:
        print("Dapet 3* Spell Card (40%)")
main()