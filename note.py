import random


class Note:

    notes = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G"
    ]

    alterations = [
        "",
        "b",
        "#"
    ]

    def __init__(self, note_name, alteration):
        self.note_name = note_name
        self.alteration = alteration

    @classmethod
    def random(cls):
        note_name = random.choice(cls.notes)
        alteration = random.choice(cls.alterations)
        return cls(note_name, alteration)

    def __str__(self):
        return self.note_name + self.alteration
