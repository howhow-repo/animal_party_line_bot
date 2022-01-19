from lib.key_and_answer import KeyAndAnswers
from lib.my_pet import MyPet


class Teddy(MyPet):
    food_map = KeyAndAnswers(
        ['紅蘿蔔', 'carrot', '胡蘿蔔', '🥕'],
        [
            'PUI !?',
            'PUI! PUI! PUI!',
            '! (嗅嗅'
        ])

    name_map = KeyAndAnswers(
        ['泰迪', '小泰迪'],
        [
            'PUI!',
            'PUI! PUI!'
        ]
    )
    party_map = MyPet.party_map.update_answers(
        [
            '(Dancing~ 🎵🎵  Danceing~ 🎵🎵',
            '(轉轉~ 🎵🎵  跳跳~ 🎵🎵'
        ]
    )

    po_map = MyPet.po_map.update_answers(
        [
            '姐接姐接姐接姐接！',
            '(蹭蹭蹭蹭蹭'
        ])

    bro_map = MyPet.bro_map.update_answers(
        [
            '葛格葛格葛格葛格！',
            '(蹭蹭蹭蹭蹭'
        ]
    )

    morning_map = MyPet.morning_map.update_answers(
        ['姐接早安！ 葛格早安！', '小動物幫早安！', '早安 PUI! PUI!']
    )

    good_night_map = MyPet.good_night_map.update_answers(
        ['姐接晚安！ 葛格晚安！', '小動物幫晚安！', '晚安暖暖趴！', '(擠擠棉被']
    )
