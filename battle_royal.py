
import time
import random


def play_game():
    list = ['ak47', 'machette', 'M16A4', 'M416', 'M24', 'Kar98']
    weapon = random.choice(list)
    weapons = []
    intro()
    battle_royal(weapons, weapon)


def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)


def string_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Option {option} is invalid. Try again!')


def int_input(prompt, min, max):
    while True:
        option = input(prompt).lower()
        if option.isnumeric():
            option = int(option)
            if min <= option <= max:
                return option
            else:
                print_pause(f'Option must be>={min}and<= {max}.Try again!', 1)
        else:
            print_pause(f'Option {option} must be numeric. Try again!', 1)


def replay():
    play_again = string_input("""Would you like to play again?
        reply with y for yes and n for no.
        """, ['y', 'n'])
    if play_again == "y":
        print_pause("restarting game")
        play_game()
    else:
        print("bye")


def battle_royal(weapons, weapon):
    print_pause("Please enter a number to decide what to do:")
    response = int_input("""Enter 1 to Take the flight.
        Enter 2 to remain at the airport.
        What would you like to do?
        Please enter 1 or 2! """, 1, 2)
    if response == 1:
        take_flight(weapons, weapon)
    else:
        airport(weapons, weapon)


def take_flight(weapons, weapon):
    print_pause("You get on the flight")
    print_pause("You are asked to jump off the plane"
                "at any point of your choise with a parachute")
    print_pause("you dive and you find yourself in a battle royale")
    print_pause("You are expected to fight to the death!")
    response = int_input("""Will you fight or run away? select:
    1. To fight
    2. To Run
    """, 1, 2)
    if response == 2:
        run()
    else:
        fight(weapons, weapon)


def run():
    print_pause("You decide to run")
    print_pause("But all you have is a frying pan")
    print_pause("You get caught up trying to run")
    print_pause("You are defeited", 1)
    print("GAME OVER")
    replay()


def fight(weapons, weapon):
    print_pause("You fight ")
    print_pause("But you realize now that you need a better weapon")
    decision = int_input("""You have a decision to make, to return
    to the airport by foot or commence the battle. Press:
    1. continue battle
    2. return to the airport
    """, 1, 2)
    if weapons != []:
        if decision == 1:
            for weapon in weapons:
                print_pause(f"You have a weapon, {weapon}")
            print_pause("you struggle to be the last person standing")
            print_pause("but u prevail, You survived")
            print_pause("You wake up, it was only but a scary dream")
            print_pause("it felt too real")
            print_pause("You WIN")

        if decision == 2:
            print_pause("You decide to return to the airport")
            print_pause("You trek for hours")
            print_pause('you are exhausted, but u make it to the airport')
            airport(weapons, weapon)

    else:
        if decision == 1:
            print_pause("You attempt fighting with your frying pan")
            print_pause("You struggle through, but somehow it is no good")
            print_pause("You obviously needed a better weapon!")
            print_pause("You are defeited")
            replay()
        if decision == 2:
            print_pause("You decide to return to the airport")
            print_pause("You trek for hours")
            print_pause('you are exhausted, but u make it to the airport')
            airport(weapons, weapon)


def airport(weapons, weapon):
    print_pause("You decide to remain at the airport")
    print_pause("just to understand whats going on.")
    print_pause("this was a good idea")
    print_pause("because you just found someone who explained it all to you")
    print_pause("now you know you have to purchase a weapon")
    decision = int_input("""press 1 to purchase a weapon from the
    airport store, or 2 to return to the landing area
    and take the flight
    """, 1, 2)
    if decision == 1:
        print_pause("You just got a weapon")
        print_pause("Your only other option now is to take the flight")
        print_pause("all purchased weapons will "
                    "be giving to you on arrival to your destination")
        weapons.append(weapon)
        print_pause("taking flight")
        take_flight(weapons, weapon)
    if decision == 2:
        print_pause("taking flight")
        take_flight(weapons, weapon)


def intro():
    print_pause("You find yourself standing "
                "at an airport with 99 other people.")
    print_pause("Rumor has it that people "
                "find themselves in battle royals like this...")
    print_pause("In your hand is a frying pan")


if __name__ == '__main__':
    play_game()
