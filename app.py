# Define a function to get a valid choice from the user
def get_valid_choice(prompt, choices, max_attempts):
    """
    The user can make a choice from a given list of options, allowing a specified number of attempts to input a valid choice.
    If the user exceeds the maximum attempts without providing a valid choice, it returns None.
    """
    for attempt in range(max_attempts):
        print(prompt)
        print(f"Type one of the choices: {', '.join(choices)}")
        choice = input()
        if choice in choices:
            return choice
        else:
            print('WRONG: Invalid choice. Please try again.')

    print(f'You exceeded the maximum number of attempts ({max_attempts}).')
    return None

# Define the function to choose a creature
def choose_creature():
    """
    The choose_creature function allows the user to select a creature from a predefined list (dragon, fairy, witch) and provides corresponding descriptions for each choice.
    """
    creature_choices = ["1", "2", "3"]
    # Definition of max_attempts locally to ensure the script runs standalone
    max_attempts = 3 
    choice = get_valid_choice('''
    You are in a wonderful (but dangerous) world, and you can choose which creature you will be.
    1. A dragon,
    2. A fairy,
    3. A witch,
    Which option do you choose?''', creature_choices, max_attempts)

    creature_descriptions = {
        '1': "Okay, good choice. You can burn people and fly.",
        '2': "Hmm... I don't think your choice is worth it. But anyway, you can fly and help people recover from illnesses.",
        '3': "You choose wisely, young apprentice. You will learn a lot of things. You have a wand and potions."
    }

    if choice in creature_descriptions:
        print(creature_descriptions[choice])
    else:
        print('WRONG: Possible choices', creature_choices)
        return None

    return choice

# Define the function to choose a weapon
def choose_weapon():
    """
    The choose_weapon function allows the user to select a weapon for protection in a dangerous world.
    """
    weapon_choices = ["1", "2", "3", "4"]
    max_attempts = 3
    choice = get_valid_choice('''
    Now you can choose what weapon you will use to protect yourself in this dangerous world.
    1. A shield and a helmet,
    2. A dagger,
    3. A bow,
    4. Nothing.
    Which weapon do you choose? Type 1 for the shield and the helmet, 2 for the dagger, 3 for the bow, and 4 for nothing.
    Type one of the choices: 1, 2, 3, 4
    ''', weapon_choices, max_attempts)

    weapon_outcomes = {
        '1': {"message": "You lost 50HP! I told you it wasn't worth it to take this.", "hp_change": -50},
        '2': {"message": "You did a good choice.", "hp_change": 0},
        '3': {"message": "You lost 30HP! You didn't know how to shoot with a bow, isn't it?", "hp_change": -30},
        '4': {"message": "You didn't choose a weapon? You fool... I bet you are a fairy. You almost DIED.", "hp_change": -90}
    }

    if choice in weapon_outcomes:
        action = weapon_outcomes[choice]
        print(action["message"])
        return action["hp_change"]
    
    return 0

# Define the function to attack or defend
def attack_or_defend():
    """
    The attack_or_defend function presents the user with the choice to attack or defend when under attack in the game, providing relevant outcomes and HP changes.
    """
    choices = ["1", "2"]
    max_attempts = 3
    choice = get_valid_choice('''
    You are attacked! Hurry up! What do you want to do?
    1. Attack with the weapon you chose before.
    2. Defend yourself and not attack.
    Which solution do you choose? Type 1 to attack back or 2 to defend yourself.
    ''', choices, max_attempts)

    if choice == '1':
        print("You lost 80 HP! Ouch, you need some practice!")
        return -80
    elif choice == '2':
        print("You lost 100 HP! You should attack back...")
        return -100
    else:
        print('WRONG: Possible choices', choices)

    return 0

# Main execution block
if __name__ == "__main__":
    # Initialize player information
    print("Hello Player One, what's your name?")
    playerName = input()
    print("Welcome,", playerName)
    playerHP = 100
    print(f"You start with {playerHP} HP. Make good use of it.")

    # First choice: Choose a creature
    creature_choice = choose_creature()

    # Second choice: Choose a weapon
    weapon_hp_change = choose_weapon()
    playerHP += weapon_hp_change
    print(f"You have {playerHP} HP now")

    # Third choice: Attack or defend yourself
    attack_defend_hp_change = attack_or_defend()
    playerHP += attack_defend_hp_change

    if playerHP <= 0:
        print("Your HP has dropped to zero. Game over!")
    else:
        print("You're still alive! Now you prove that you can survive in this world. Welcome and enjoy.")

    print("Thanks for playing!")
