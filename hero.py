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
        return f'nickname: {self.nickname}\n' \
               f'superpower: {self.superpower}\n' \
               f'health: {self.health_points}'

    def __len__(self):
        print("len_catchphrase: ",len(self.catchphrase))


Hero = SuperHero(name="Sabina", nickname="02", superpower="stupidity", health_points=50, catchphrase="I wanna sleep")
Hero.print_name_hero()
print(Hero)
Hero.print_health()
Hero.__len__()


class Batman(SuperHero):
    ears = "ears"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False ):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly=fly
        self.damage=damage
    def print_health(self):
        self.fly = True
        print(f'health: {self.health_points ** 2}')

    def print_fly(self):
        print(f'fly in the True_phrase')

bat = Batman(name="Emma", nickname="kani", superpower="my brain", health_points=60, catchphrase="I wanna eat", damage=5)
print(bat)
bat.print_health()
bat.print_fly()



class Goodman(SuperHero):
    nails = "nails"
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly=fly
        self.damage=damage

    def print_health(self):
        self.fly = True
        print(f'health: {self.health_points ** 2}')
    def print_fly(self):
        print(f'fly in the True_phrase')



good = Goodman(name="Emily", nickname="bugaga", superpower="teleport", health_points=70, catchphrase="Меня зовут Кира Йошикаге", damage=11)
print(good)
good.print_fly()
good.print_health()


class Villian(Goodman):
    people = "monster"
    def gen_x(self):
        pass

    def crit(self, damage):
        print(f'damage: {damage ** 2}')


vivi = Villian(name="L", nickname="Lll", superpower="cloaning", health_points=100, catchphrase="LOL", damage=21)
print(vivi)
vivi.gen_x()
vivi.crit(good.damage)











