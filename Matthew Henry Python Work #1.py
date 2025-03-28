class Monster:     
    def __init__(self, name, monster_type):
        self.__name = name
        self.__monster_type = monster_type

    def set_name(self, name):
        self.__name = name

    def set_monster_type(self, monster_type):
        self.__monster_type = monster_type

    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__monster_type
    
    def scare(self):
        if self.__monster_type == "Frankenstein":
            print("Fire Bad!")
        elif self.__monster_type == "Werewolf":
            print("Awoooo!")
        elif self.__monster_type == "Dracula!":
            print("Bleh!")
        else:
            print("Boo!")

monster1 = Monster("Franky", "Frankenstein")
monster2 = Monster("Drayden", "Dracula")

print(monster1.get_name())
print(monster2.get_name())

monster1.scare()
monster2.scare()
