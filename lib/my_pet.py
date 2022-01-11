from random import randint

from .messagereceiver import MessageReceiver


class MyPet(MessageReceiver):
    favorite_food = []
    nick_names = []
    party = ['暖暖趴', '小動物趴']

    food_response = []
    name_response = []
    party_response = []

    @classmethod
    def react(cls, message: str):
        splited_list = cls.split_sentence(message)
        for w in splited_list:
            if w in cls.favorite_food:
                return cls.food_reaction()
            elif w in cls.nick_names:
                return cls.name_reaction()
            elif w in cls.party:
                return cls.party_reaction()

        return None

    @classmethod
    def food_reaction(cls):
        l = len(cls.food_response) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.food_response[i]

    @classmethod
    def name_reaction(cls):
        l = len(cls.name_response) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.name_response[i]

    @classmethod
    def party_reaction(cls):
        print('party')
        l = len(cls.party_response) - 1
        if l < 0:
            return None
        i = randint(0, l)
        return cls.party_response[i]
