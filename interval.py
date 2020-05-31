import random


class Interval:

    int_types = [
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th"
    ]

    def __init__(self, int_type, quality):
        self.type = int_type
        self.quality = quality

    @classmethod
    def random(cls):
        int_type = random.choice(cls.int_types)
        if int_type in ["4th", "5th"]:
            quality = "Perfect"
        else:
            quality = random.choice(["Major", "minor"])
        return cls(int_type, quality)

    def __str__(self):
        return self.quality + " " + self.type
