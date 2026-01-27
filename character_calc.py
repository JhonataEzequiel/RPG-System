MAX_LEVEL = 20
MAX_ATTRIBUTE = 10
SPECIAL_LEVELS = {5, 10, 15, 20}
ATTRIBUTE_COUNT = 7

class Character:
    def __init__(self, level=1, attribute_points=7, attributes=None):
        self.level = level
        self.attribute_points = attribute_points
        self.attributes = attributes if attributes is not None else [0] * ATTRIBUTE_COUNT

    @property
    def max_skill_level(self):
        return 2 if self.level == 1 else 3 + self.level // 2

    def add_attribute_point(self, quantity = 0):
        self.attribute_points += quantity

    def level_up(self):
        if self.level == MAX_LEVEL:
            print("Already at max level")
        else:
            self.level += 1
            self.add_attribute_point(2 if self.level in SPECIAL_LEVELS else 1)
            
    
    def allocate_attribute_points(self):
        while self.attribute_points > 0:
            chosen_attribute = self.choose_attribute() - 1

            if not -2 <= chosen_attribute < len(self.attributes):
                print("Invalid choice")
                continue
            elif chosen_attribute == -1:
                break

            if self.attributes[chosen_attribute] < MAX_ATTRIBUTE:
                if self.attributes[chosen_attribute] < self.max_skill_level:
                    self.attributes[chosen_attribute] += 1
                    self.attribute_points -= 1
                else:
                    print("already at max possible level, choose another one!")
            else:
                print(f"already at level {MAX_ATTRIBUTE}, choose another one!")

            
    def choose_attribute(self):
        return int(input("Choose an attribute to level up:\n\
1 - Constitution\n2 - Strength\n3 - Dexterity\n4 - Wisdom\n5 - Faith\n6 - Intelligence\n7 - Charisma\n0 - Exit\n"))
    
    def print_character(self):
        print(
            f"Level: {self.level} | "
            f"Available Points: {self.attribute_points}\n"
            f"Constitution: {self.attributes[0]}\n"
            f"Strength: {self.attributes[1]}\n"
            f"Dexterity: {self.attributes[2]}\n"
            f"Wisdom: {self.attributes[3]}\n"
            f"Faith: {self.attributes[4]}\n"
            f"Intelligence: {self.attributes[5]}\n"
            f"Charisma: {self.attributes[6]}\n"
        )


if __name__ == "__main__":
    player_choice = int(input("Create a new character or import one?\n1 - Create\n2 - Import\n3 - Exit\n"))
    player = None
    if player_choice == 1:
        player = Character()
    elif player_choice == 2:
        pass
    elif player_choice == 3:
        exit

    if player is not None:
        while 1:
            try:
                menu_choice = int(
                    input("What do you want to do?\n1 - See Character Stats\n2 - Level up\n3 - Allocate attributes\n4 - Quit\n")
                    )
            except ValueError:
                print("Invalid input")
                continue
            if menu_choice == 1:
                player.print_character()
            elif menu_choice == 2:
                player.level_up()
            elif menu_choice == 3:
                player.allocate_attribute_points()
            else:
                break
