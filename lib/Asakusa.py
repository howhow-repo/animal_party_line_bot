import json
import os
import random

import jieba


def split_sentence(sentence):
    if sentence == '/help':
        return ['/help']
    seg_list = jieba.lcut_for_search(sentence)
    return seg_list


class Asakusa:
    """只要發言中含有 問神 兩字，將會自動抽出結果，回覆完整詩籤；
    只要發言中含有 運勢 兩字，將會自動抽出大吉至凶的結果。"""

    long_ver_keyword = '問神'
    short_ver_keyword = '運勢'
    with open(f'{os.path.dirname(__file__)}/asakusa.json', 'r') as f:
        datas = json.load(f)

    @classmethod
    def react(cls, message):
        msg_ver = cls.check_if_ask(message)
        if msg_ver == 'help':
            return cls.__doc__
        if msg_ver:
            return cls.pickone(msg_ver)
        else:
            return None

    @classmethod
    def check_if_ask(cls, message):
        splited_list = split_sentence(message)
        for word in splited_list:
            if word == cls.long_ver_keyword:
                return 'long'
            elif word == cls.short_ver_keyword:
                return 'short'
            if word == '/help':
                return 'help'
        return False

    @classmethod
    def pickone(cls, msg_ver='long'):
        raw_pick = random.choice(cls.datas)
        if msg_ver == 'long':
            return cls.format_long_to_line(raw_pick)
        if msg_ver == 'short':
            return cls.format_short_to_line(raw_pick)
        return False

    @classmethod
    def format_long_to_line(cls, one_sign: dict):
        text = f"💮<<{one_sign['type']}>>\n" \
               f"📜{one_sign['poem']}\n" \
               f"----\n" \
               f"📝{one_sign['explain']}\n" \
               f"----\n"
        print()
        for k, v in one_sign['result'].items():
            text += f"{k}: {v}\n"
        return text

    @classmethod
    def format_short_to_line(cls, one_sign: dict):
        text = f"💮<<{one_sign['type']}>>"
        return text
