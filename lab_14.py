class Basic():
    health = 100
    attack = 40
    defence = 40
    def __init__(self, name):
        self.name = name
    def print(self):
        print("Имя персонажа ", self.name)
        print("******************")
        print("Здоровье: ", self.health)
        print("Атака: ", self.attack)
        print("Защита: ", self.defence)
        print("******************")
        
class Mag(Basic):
    def __init__(self, name):
        print("Выбран класс: Маг")
        Basic.__init__(self, name)
        self.attack = self.attack + (self.attack * 0.2)
        
        
class Warrior(Basic):
    def __init__(self, name):
        print("Выбран класс: Воин")
        Basic.__init__(self, name)
        self.health = self.health + (self.health * 0.5)
        

class Healer(Basic):
    def __init__(self, name):
        print("Выбран класс: Целитель")
        Basic.__init__(self, name)
        self.defence = self.defence + (self.defence * 0.1)

class Boost_Basic(Basic):
    crit_attack = 20
    dodge = 15
    def __init__(self, name, element):
        Basic.__init__(self, name)
        self.element = element
    def boost_print(self):
        print("Крит. атака: ", self.crit_attack)
        print("Уклонение: ", self.dodge)
        print("Cтихия: ", self.element)

class Boost_mag(Boost_Basic, Mag):
    def __init__(self, name, element):
        Mag.__init__(self, name)
        Boost_Basic.__init__(self, name, element)

class Boost_warrior(Boost_Basic, Mag):
    def __init__(self, name, element):
        Warrior.__init__(self, name)
        Boost_Basic.__init__(self, name, element)

class Boost_healer(Boost_Basic, Mag):
    def __init__(self, name, element):
        Healer.__init__(self, name)
        Boost_Basic.__init__(self, name, element)

correct = bool(False)        
class_choise = input("Выберите класс: mag - маг, war - воин, cel - целитель: ")
while correct == False:
    if class_choise == 'mag':
        person = Mag(input("Введите имя: "))
        correct = True
        person.print()
    elif class_choise == 'war':
        person = Warrior(input("Введите имя: "))
        correct = True
        person.print()
    elif class_choise == 'cel':
        person = Healer(input("Введите имя: "))
        correct = True
        person.print()
    else:
        class_choise = input("Ошибка ввода, повторите: ")

boost_choise = input("Желаете улучшить персонажа? (Y/N) ")
correct = False
while correct == False:
    if class_choise == 'mag' and boost_choise == 'Y':
        boost_person = Boost_mag(person.name, input("Введите стихию: "))
        boost_person.print()
        correct = True
        boost_person.boost_print()
    elif class_choise == 'war' and boost_choise == 'Y':
        boost_person = Boost_warrior(person.name, input("Введите стихию: "))
        boost_person.print()
        correct = True
        boost_person.boost_print()
    elif class_choise == 'cel' and boost_choise == 'Y':
        boost_person = Boost_healer(person.name, input("Введите стихию: "))
        boost_person.print()
        correct = True
        boost_person.boost_print()
    elif boost_choise == 'N':
        break
    else:
        boost_choise = input("Ошибка ввода, повторите: ")
