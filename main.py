class Animal:

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind


class Enclosure:

    def __init__(self, name, animals):
        self.name = name
        self.animals = animals


class Zoo:

    def __init__(self, name, enclosures):
        self.name = name
        self.enclosures = enclosures
