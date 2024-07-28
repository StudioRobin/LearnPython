import random
money = 100
options = ["red" , "black"]
random.shuffle(options)
number = random.randrange(51)
bettingamount = int(input("how much do you want to bet?"))
while bettingamount > money:
    print("you are too broke")
    bettingamount = int(input("how much do you want to bet?"))

choices = input("what do you want to bet on")
while choices != options(0) or options(1):
    print("invalid choices lil bro")
    choices = input("what do you want to bet on")
else:
    print("you good")
    

def roulette(bettingamount, choice):
    if choices == "red":
        if options == "red":
            money = money + bettingamount * 2
        return
    else:
        money = money - bettingamount
