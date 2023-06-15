from animals.bird.eagle import Eagle
from animals.bird.penguin import Penguin
from animals.mammal.flying_mammals.bat import Bat
from animals.mammal.lion import Lion

filling_line = '<----------------------------------->'
if __name__ == "__main__":
    lion = Lion('Lion', 'Savannah', 10, 'Yellow')
    lion.roar()
    lion.sleep()
    lion.eat()
    print(filling_line)
    bat = Bat('Bat', 'Cave', 2, 10.2, True)
    bat.living_life()
    print(filling_line)
    penguin = Penguin('Penguin', 'Arctic', 'type_3', 'excellent')
    penguin.living_life()
    print(filling_line)
    eagle = Eagle('Eagle', 'Mountain_sky', 'type_3', 18.5)
    eagle.living_life()
