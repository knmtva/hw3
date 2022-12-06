class SuperHero():
    # атрибуты уровня класса
    people = "people"

    # конструктор класса с атрибутами
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name_hero(self):
        print(f'name: {self.name}')

    def print_health(self):
        print(f'health: {self.health_points * 2}')

    def __str__(self):
        return f'name: {self.nickname}\n' \
               f'superpower: {self.superpower}\n' \
               f'health: {self.health_points}'

    def __len__(self):
        print("len_catchphrase: ",len(self.catchphrase))


Hero = SuperHero(name="Sabina", nickname="02", superpower="stupidity", health_points=50, catchphrase="I wanna sleep")
Hero.print_name_hero()
Hero.print_health()
Hero.__len__()
print(Hero)
