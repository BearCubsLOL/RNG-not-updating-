import random
import json
import time


def RulesAndSignUp():
    new_or_old = input("\n\nAre you a new or returning player: ")
    with open("PlayerData.txt") as f:
        data = json.load(f)
    if "new" in new_or_old.lower():
        print("\n\nWARNING IF YOU ALREADY HAVE A CREATED ACCOUNT SIGNING UP WILL WIPE YOUR DATA")
        print("\nSign Up")
        set_username = input("User Name: ")
        set_password = input("Password: ")
        data["username"] = set_username
        data["password"] = set_password
        data["coins"] = 0
        with open("PlayerData.txt", "w") as lol:
            json.dump(data, lol, indent=4)
        RulesAndSignUp()
    elif "returning" in new_or_old.lower():
        print("\n\nLogin")
        username_attempt = input("Username: ")
        password_attempt = input("Password: ")
        if username_attempt == data["username"] and password_attempt == data["password"]:
            print("Logging in...")
            Lobby()
        else:
            print("Invalid")
            RulesAndSignUp()
    else:
        print("Invalid")
        print(data["coins"])
        RulesAndSignUp()


def Lobby():
    print("\n\nWhat do you want to do?")
    lobbychoice = input("Gamble┃Adventure┃coming soon...\n")
    if lobbychoice.lower() == "gamble":
        Gamble()


def weaponagain():
    with open("PlayerData.txt") as f:
        data = json.load(f)
    again = input("\nWould you like to roll again for 5 coins: ")
    if again.lower() == "yes" or again.lower() == "y":
        RandomWeapon()
        data["coins"] -= 5
        with open("PlayerData.txt", "w") as lol:
            json.dump(data, lol, indent=4)
        weaponagain()
    elif again.lower() == "no" or again.lower() == "n":
        Lobby()
    else:
        print("Invalid response.")
        print("Sending to lobby.")
        Lobby()

def Gamble():
    print("\n\nWhat do you want to gamble on?")
    gamblechoice = input("Weapon┃coming soon...\n")
    if gamblechoice.lower() == "weapon":
        weaponroll()


def weaponroll():
    with open("PlayerData.txt") as f:
        data = json.load(f)
    weaponyesno = input("\n\nWould you like to roll for a weapon for 5 coins: ")
    if weaponyesno.lower() == "yes" or weaponyesno.lower() == "y":
        RandomWeapon()
        data["coins"] -= 5
        with open("PlayerData.txt", "w") as lol:
            json.dump(data, lol, indent=4)
        weaponagain()
    elif weaponyesno.lower() == "no" or weaponyesno.lower() == "n":
        Lobby()


    else:
        print("Invalid response.")
        print("Sending to lobby.")
        Lobby()


def RandomWeapon():
    random_weapon = random.randint(1,1000000000000)
    if random_weapon > 0 and random_weapon < 500000000001:
        print("\nCongrat's You Got An Excalibur!\n50%")
    elif random_weapon > 50000000000 and random_weapon < 525000000001:
        print("\nCongrat's You Got An ")

    else:
        print("\nToo Bad You Didn't Find Anything")
RulesAndSignUp()