import random
money = 100
options = ["red" , "black", "evens", "odds"]
random.shuffle(options)
number = random.randrange(51)
bettingamount = int(input("how much do you want to bet?"))
while bettingamount > money:
    print("you are too broke")
    bettingamount = int(input("how much do you want to bet?"))

choices = input("what do you want to bet on")

def roulette(bettingamount, choices):
    if choices == options:
            money + (bettingamount * 2)
            print("the number was" + options + number)
            print("you won, congrats")
            return
    else:
        money - bettingamount
        print("")

while True:
    if choices not in options:
        print("invalid choices lil bro")
        choices = input("what do you want to bet on")
    else:
        money = money
roulette(bettingamount, choices)
