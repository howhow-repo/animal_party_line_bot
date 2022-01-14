from random import randint

from .messagereceiver import MessageReceiver


class MyPet(MessageReceiver):
    food_map = [[], []]
    name_map = [[], []]
    party_map = [['暖暖趴', '小動物趴'], []]
    po_map = [['波', '波波', '啵', '啵啵'], []]
    bro_map = [['哥比', '葛格'], []]
    morning_map = [['早安'], []]
    good_night_map = [['晚安'], []]

    @classmethod
    def reacts(cls, message: str):
        splited_list = cls.split_sentence(message)
        for w in splited_list:
            if w in cls.food_map[0]:
                return cls.food_reaction()
            elif w in cls.name_map[0]:
                return cls.name_reaction()
            elif w in cls.party_map[0]:
                return cls.party_reaction()
            elif w in cls.po_map[0]:
                return cls.po_reaction()
            elif w in cls.bro_map[0]:
                return cls.bro_reaction()
            elif w in cls.morning_map[0]:
                return cls.mor_reaction()
            elif w in cls.good_night_map[0]:
                return cls.good_night_reaction()

        return None

    @classmethod
    def food_reaction(cls):
        l = len(cls.food_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.food_map[1][i]

    @classmethod
    def name_reaction(cls):
        l = len(cls.name_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.name_map[1][i]

    @classmethod
    def party_reaction(cls):
        l = len(cls.party_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.party_map[1][i]

    @classmethod
    def po_reaction(cls):
        l = len(cls.po_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.po_map[1][i]

    @classmethod
    def bro_reaction(cls):
        l = len(cls.bro_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.bro_map[1][i]

    @classmethod
    def mor_reaction(cls):
        l = len(cls.morning_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.morning_map[1][i]

    @classmethod
    def good_night_reaction(cls):
        l = len(cls.good_night_map[1]) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.good_night_map[1][i]