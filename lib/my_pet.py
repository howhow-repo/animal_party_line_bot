from random import randint

from .messagereceiver import MessageReceiver
from .key_and_answer import KeyAndAnswers


def random_pick_in_list(ls: list):
    if len(ls) <= 0:
        return
    l = len(ls) - 1
    i = randint(0, l)
    return ls[i]


class MyPet(MessageReceiver):
    food_map = KeyAndAnswers([], [])
    name_map = KeyAndAnswers([], [])
    party_map = KeyAndAnswers(['暖暖趴', '小動物趴'], [])
    po_map = KeyAndAnswers(['波', '波波', '啵', '啵啵'], [])
    bro_map = KeyAndAnswers(['哥比', '葛格'], [])
    morning_map = KeyAndAnswers(['早安'], [])
    good_night_map = KeyAndAnswers(['晚安'], [])

    @classmethod
    def reacts(cls, message: str):
        splited_list = cls.split_sentence(message)
        ka_list = [cls.__dict__[ka] for ka in cls.__dict__ if type(cls.__dict__[ka]) == KeyAndAnswers]
        for word in splited_list:
            for ka in ka_list:
                if word in ka.keywords:
                    return random_pick_in_list(ka.answers)
        return None
