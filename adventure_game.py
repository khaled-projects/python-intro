import random
import time


def print_sleep(message, wait_time):
    """Print message and sleep for given time."""
    print(message)
    time.sleep(wait_time)


def get_random_weapon():
    """Return a randomly chosen weapon."""
    weapons = [
        {"name": "dagger", "level": 1},
        {"name": "sword", "level": 3},
        {"name": "bow", "level": 2},
        {"name": "axe", "level": 4},
        {"name": "magic staff", "level": 5}
    ]
    return random.choice(weapons)


def get_random_enemy():
    """Return a randomly chosen enemy."""
    enemies = [
        {"name": "dragon", "level": 10},
        {"name": "troll", "level": 8},
        {"name": "wicked fairy", "level": 6},
        {"name": "pirate", "level": 7},
        {"name": "gorgon", "level": 9}
    ]
    return random.choice(enemies)


def combat(player_weapons, enemy_weapons, enemies, score):
    """Handle combat logic and determine outcome."""
    print_sleep(
        f"The {enemies[0]['name']} attacks you with a"
        f"{enemy_weapons[0]['name']}!",
        2
    )
    print_sleep(
        f"The {enemies[1]['name']} attacks you with a"
        f"{enemy_weapons[1]['name']}!",
        2
    )
    print_sleep(
        f"You face the {enemies[0]['name']} "
        f"and {enemies[1]['name']} with your "
        f"{player_weapons[0]['name']} and {player_weapons[1]['name']}.", 2
    )

    total_player_level = sum(weapon['level'] for weapon in player_weapons)
    total_enemy_level = sum(weapon['level'] for weapon in enemy_weapons)

    combat_choice_prompt = (
        "Enter '1' to attack one enemy with each arm, "
        "'2' to focus on one enemy with both arms: "
    )
    choice = input(combat_choice_prompt)
    while choice not in ['1', '2']:
        print("Invalid choice!")
        choice = input(combat_choice_prompt)

    if choice == '1':
        if total_player_level >= total_enemy_level:
            score += total_enemy_level
            print_sleep(
              f"You have defeated both enemies! Your score is now {score}.", 2
            )
            return 'victorious', score
        else:
            print_sleep("You have been defeated by the enemies!", 2)
            return 'defeated', score
    elif choice == '2':
        if total_player_level >= total_enemy_level / 2:
            score += total_enemy_level
            print_sleep(
                f"You focus your attacks and defeat the enemies! "
                f"Your score is now {score}.", 2
            )
            return 'victorious', score
        else:
            print_sleep("You have been defeated by the enemies!", 2)
            return 'defeated', score


def play_again(score):
    """Ask the player if they want to play again."""
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)\n")
        if choice == 'n':
            print_sleep(
                f"Thanks for playing! Your final score was {score}. "
                "See you next time.", 2
            )
            return 'game_over', score
        elif choice == 'y':
            print_sleep(
                "Excellent! Restarting the game ...",
                2
            )
            return 'running', score


def explore(player_weapons, enemies, cave_visited, score):
    """Explore either the cave or the house."""
    while True:
        print_sleep(
            "Enter 1 to knock on the door of the house.", 2
        )
        print_sleep(
            "Enter 2 to peer into the cave.", 2
        )
        print_sleep(
            "What would you like to do?", 2
        )

        choice = ''
        while choice not in ['1', '2']:
            choice = input("(Please enter 1 or 2.)\n")
        if choice == '1':
            result, score = explore_house(player_weapons, enemies, score)
            if result == 'victorious':
                return 'next_stage', score
            else:
                return result, score
        elif choice == '2':
            player_weapons, cave_visited = explore_cave(
                player_weapons, cave_visited
            )


def explore_cave(player_weapons, cave_visited):
    """Simulate exploring the cave and potentially finding new weapons."""
    print_sleep(
        "You peer cautiously into the cave.", 2
    )
    if cave_visited:
        print_sleep(
            "You've been here before, and there is nothing new to find.", 2
        )
        return player_weapons, cave_visited
    else:
        print_sleep(
            "It turns out to be only a very small cave.", 2
        )
        print_sleep(
            "Your eye catches a glint of metal behind a rock.", 2
        )
        print_sleep(
            "You have found the magical Sword of Ogoroth!", 2
        )
        player_weapons[1] = {"name": "magical Sword of Ogoroth", "level": 5}
        cave_visited = True
        return player_weapons, cave_visited


def explore_house(player_weapons, enemies, score):
    """Simulate exploring the house and combat with enemies."""
    print_sleep(
        "You approach the door of the house.", 2
    )
    print_sleep(
        f"As you are about to knock, the door opens and out steps a "
        f"{enemies[0]['name']} and a {enemies[1]['name']}!", 3
    )

    print_sleep(
        f"Eep! This is the {enemies[0]['name']}'s house!", 2
    )
    result, score = combat(
        player_weapons,
        [get_random_weapon(), get_random_weapon()],
        enemies,
        score
    )
    if result == 'defeated':
        result, score = play_again(score)
        return result, score
    else:
        return 'next_stage', score


def next_stage(stage, score):
    """Move to the next stage."""
    if stage <= 3:
        print_sleep(
            f"Congratulations! You have reached stage {stage}.", 2
        )
        enemies = [
            get_random_enemy(),
            get_random_enemy()
        ]
        player_weapons = [
            get_random_weapon(),
            get_random_weapon()
        ]
        cave_visited = False
        intro(stage, enemies, player_weapons)
        return explore(player_weapons, enemies, cave_visited, score)
    else:
        print_sleep(
           f"You have completed all stages! Your final score is {score}."
           f"You are the ultimate champion!", 2
        )
        return play_again(score)


def intro(stage, enemies, player_weapons):
    """Print game introduction."""
    print_sleep(
       f"Stage {stage}: You find yourself standing in an open field, "
       f"filled with grass and yellow wildflowers.", 3
    )
    print_sleep(
       f"Rumor has it that a {enemies[0]['name']} and a"
       f"{enemies[1]['name']} are somewhere around here, "
       f"and have been terrifying the nearby village.", 3
    )

    print_sleep(
        "In front of you is a house.", 2
    )
    print_sleep(
        "To your right is a dark cave.", 2
    )
    print_sleep(
        f"In your hands you hold your trusty (but not very effective)"
        f"{player_weapons[0]['name']} and {player_weapons[1]['name']}.", 2
    )


def start_game():
    """Start the game and manage game flow."""
    if __name__ == "__main__":
        game_state = 'running'  # Initialize game_state
        stage = 1
        score = 0

        while game_state == 'running':
            enemies = [
                get_random_enemy(),
                get_random_enemy()
            ]
            player_weapons = [
                get_random_weapon(),
                get_random_weapon()
            ]
            cave_visited = False

            intro(stage, enemies, player_weapons)
            game_state, score = explore(
                player_weapons, enemies, cave_visited, score
            )

            if game_state == 'next_stage':
                stage += 1
                game_state = next_stage(stage, score)

            elif game_state == 'game_over':
                break


# Start the game
start_game()
