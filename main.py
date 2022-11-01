class Animal:
    sounds = {
        "lion": "roar",
        "dog": "woof",
        "fox": "what does the fox say?",
    }

    predators = ["lion", "dog", "fox"]

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    @property
    def is_predator(self):
        return self.kind in self.predators

    def make_sound(self):
        print(self.sounds.get(self.kind, "idk"))

    def __str__(self):
        return f"{self.kind} ({self.name})"


class Enclosure:

    def __init__(self, name, animals=None):
        self.name = name
        if animals is None:
            animals = []
        self.animals = animals

    def add_animal(self, animal):
        is_not_mixed = len({a.is_predator for a in self.animals + animal}) == 1
        if is_not_mixed:
            self.animals.append(animal)
        else:
            print("Ага, зараз лисиці курей з'їдять")

    def remove_animal(self, animal):
        print(f"З вольєру {self.name} видаляється тварина {animal}")
        self.animals.remove(animal)

    def __str__(self):
        return f"Вольєр {self.name} з такими тваринами: {', '.join([str(animal) for animal in self.animals])}"


class Zoo:

    def __init__(self, name, enclosures=None):
        self.name = name
        if enclosures is None:
            enclosures = []
        self.enclosures = enclosures

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def show(self):
        print(f"Я зоопарк '{self.name}'")
        print(f"У мене є такі вольєри:")
        for enclosure in self.enclosures:
            print(f"\t{str(enclosure)}")


def create_zoo():
    return Zoo(name="Kyiv zoo" or input("Введіть назву вашого зоопарку: "))


def create_enclosure(zoo):
    enclosure = Enclosure(name="Bears" or input("Введіть назву вашого вольєру: "))
    zoo.add_enclosure(enclosure=enclosure)
    return enclosure


def create_animal(enclosure, default=True):
    animal = Animal(
        name="Boris" if default is True else input("Введіть назву вашої тварини: "),
        kind="fox" if default is True else input("Введіть вид вашої тварини: ")
    )
    enclosure.add_animal(animal=animal)
    return animal


def choose_animal(zoo):
    while True:
        print("Оберіть вольєр \n-1 - вихід")
        for number, enclosure in enumerate(zoo.enclosures):
            print(f"{number} - {enclosure.name}")

        command = input("Введіть номер вольєру: ")

        while True:
            print("Оберіть тварину \n-1 - вихід")

            for number, animal in enumerate(zoo.enclosures[int(command)].animals):
                print(f"{number} - {enclosure.name}")

            sub_command = input("Введіть номер тварини: ")

            if sub_command == "-1":
                break

            chosen_animal = zoo.enclosures[int(command)].animals[int(sub_command)]
            print("\tТварина намагається щось сказати:", end=" ")
            chosen_animal.make_sound()

        if command == "-1":
            break


def start_zoo():
    zoo = create_zoo()

    enclosure = create_enclosure(zoo)

    animal = create_animal(enclosure)

    while True:
        print(
            """
            Menu
            1 - створити зоопарк
            2 - додати вольєр
            3 - додати тварину
            4 - показати зоопарк
            5 - обрати тваринку
            """
        )
        command = input("Введіть команду: ")
        if command == "1":
            zoo = create_zoo()
        if command == "2":
            enclosure = create_enclosure(zoo)
        if command == "3":
            animal = create_animal(enclosure)
        if command == "4":
            zoo.show()
        if command == "5":
            choose_animal(zoo)





start_zoo()
