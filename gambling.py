money = 100
def game():
    import random
    options = ["red" , "black", "evens", "odds"]
    number = random.randrange(51)
    strnumber = str(number)
    bettingamount = int(input("how much do you want to bet?"))
    while bettingamount > money:
        print("you are too broke")
        bettingamount = int(input("how much do you want to bet?"))
    choices = input("what do you want to bet on")
    while True:
        if choices not in options:
            print("invalid choices lil bro")
            choices = input("what do you want to bet on")
        else:
            break
    options.pop(3)
    options.pop(2)
    options.pop(random.randrange(2))
    def roulette(bettingamount, choices):
        global money
        if options[0] == choices:
            money = money + bettingamount
            print(options[0] + " " + strnumber + " was picked")
            print("you won, congrats")
        else:
            money = money - bettingamount
            print(options[0] + " " + strnumber + " was picked")
            print("you lost, dont stop gambling")

    roulette(bettingamount, choices)
    print(money)
    def restart(input):
        if input == "yes":
            game()
        else:
            exit()
    while True:
        global money
        if money == 0:
            input("do you want to restart? yes or no")
            if input == "yes":
                money = 100
            else:
                exit()
game()



