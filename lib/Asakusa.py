import json
import os
import random

import jieba


def split_sentence(sentence):
    if sentence == '/help':
        return ['/help']
    seg_list = jieba.lcut_for_search(sentence)
    return seg_list


def add_some_phrase(raw_pick):
    if raw_pick['type'] == "大吉":
        return "真正的大吉！恭喜你！✧*｡٩(ˊᗜˋ*)و✧*｡"
    elif raw_pick['type'] == "中吉":
        return "還不錯吧。(ゝ∀･)"
    elif raw_pick['type'] == "吉":
        return "很棒呢！(๑•̀ω•́)"
    elif raw_pick['type'] == "小吉":
        return "很普通的小吉，世界和平☮️(ﾉ>ω<)ﾉ"
    elif raw_pick['type'] == "末吉":
        return "不錯呢！(,,・ω・,,)"
    elif raw_pick['type'] == "末小吉":
        return "勉勉強強啦！(*´∀`)"
    else:
        return random.choice([
            '有點糟糕。(つд⊂)',
            '運氣不是很好呢，怎麼辦？Σ(ﾟдﾟ)',
            '還不算太糟！(ﾟωﾟ)',
            '這真的有點糟糕！(☉д⊙)',
        ])


class Asakusa:
    """只要發言中含有 問神 兩字，將會自動抽出結果，回覆完整詩籤；
    只要發言中含有 運勢 兩字，將會自動抽出大吉至凶的結果。"""

    long_ver_keyword = '問神'
    short_ver_keyword = '運勢'
    quick_pick = ['大吉', '吉', '中吉', '小吉', '末吉', '末小吉', '末凶', '小凶', '半凶', '凶', '大凶']
    with open(f'{os.path.dirname(__file__)}/asakusa.json', 'r') as f:
        omikuji = json.load(f)

    @classmethod
    def react(cls, message):
        msg_ver = cls.check_service(message)
        if msg_ver == 'help':
            return cls.__doc__
        if msg_ver:
            return cls.pickone(msg_ver)
        else:
            return None

    @classmethod
    def check_service(cls, message):
        if cls.check_if_help(message):
            return cls.check_if_help(message)
        elif cls.check_if_ask(message):
            return cls.check_if_ask(message)
        elif cls.check_if_dice(message):
            return cls.check_if_dice(message)

    @classmethod
    def check_if_dice(cls, message):
        pass
        # TODO

    @classmethod
    def check_if_help(cls, message):
        if message == '/help':
            return 'help'
        return False

    @classmethod
    def check_if_ask(cls, message):
        splited_list = split_sentence(message)
        for word in splited_list:
            if word == cls.long_ver_keyword:
                return 'long'
            elif word == cls.short_ver_keyword:
                return 'short'
        return False

    @classmethod
    def pickone(cls, msg_ver='long'):
        if msg_ver == 'long':
            raw_pick = random.choice(cls.omikuji)
            return cls.format_long_to_line(raw_pick)
        if msg_ver == 'short':
            raw_pick = {'type': random.choice(cls.quick_pick)}
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
        text = f"💮<<{one_sign['type']}>>" + '\n' + add_some_phrase(one_sign)
        return text
