from __future__ import annotations

import json
import os
import random
import re

import jieba


def split_sentence(sentence):
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
    """
    1. 只要發言中含有 問神 兩字，將會自動抽出結果，回覆完整詩籤。
    2. 只要發言中含有 運勢 兩字，將會自動抽出大吉至凶的結果。
    3. 使用格式 choice[選項一,選項二,選項三,...] 將隨機抽出一個選項。
    4. 使用格式 <number 1>d<number 2> (ex: 2d100; 3d6), 將擲出<number 2>面骰子<number 1>次
    """

    long_ver_keyword = '問神'
    short_ver_keyword = '運勢'
    quick_pick = ['大吉', '吉', '中吉', '小吉', '末吉', '末小吉', '末凶', '小凶', '半凶', '凶', '大凶']
    with open(f'{os.path.dirname(__file__)}/asakusa.json', 'r') as f:
        omikuji = json.load(f)

    @classmethod
    def react(cls, message):
        service_type, pre_formed_data = cls.check_service(message)
        if service_type == 'help':
            return cls.__doc__
        elif service_type == 'ask':
            return cls.pickone(pre_formed_data)
        elif service_type == 'choice':
            return cls.do_choose(pre_formed_data)
        elif service_type == 'dice':
            return cls.do_dice(pre_formed_data)
        else:
            return None

    @classmethod
    def check_service(cls, message) -> tuple[str, str] | tuple[None, None]:
        if cls.check_if_help(message):
            return "help", ""
        elif cls.check_if_ask(message):
            return "ask", cls.check_if_ask(message)
        elif cls.check_if_choice(message):
            return "choice", cls.check_if_choice(message)
        elif cls.check_if_dice(message):
            return "dice", cls.check_if_dice(message)
        return None, None

    @classmethod
    def check_if_help(cls, message):
        if message == '/help':
            return 'help'
        return False

    @classmethod
    def check_if_choice(cls, message):
        Regex = re.compile(r'choice\[(.*)]')
        match = Regex.match(message)
        if match:
            return match[1]
        return False

    @classmethod
    def do_choose(cls, choose_str: str):
        return random.choice(choose_str.split(r','))

    @classmethod
    def check_if_dice(cls, message):
        Regex = re.compile(r'(\d+)d(\d+)')
        match = Regex.match(message)
        if match and int(match[1]) <= 10:
            return match[0]
        return False

    @classmethod
    def do_dice(cls, dice_str: str):
        times, dice_size = dice_str.split('d')
        results = []
        for t in range(int(times)):
            results.append(random.randint(1, int(dice_size)))
        return cls.format_dice_result(results)

    @classmethod
    def format_dice_result(cls, result_list):
        return f'擲骰: {result_list}={sum(result_list)}'

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
