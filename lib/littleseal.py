from lib.key_and_answer import KeyAndAnswers
from lib.my_pet import MyPet


class LittleSeal(MyPet):
    food_map = KeyAndAnswers(
        ['小魚乾', '小魚干', '魚', '小魚', '魚乾', 'fish', '🐟'],
        [
            '我要！',
            '(嚼嚼嚼',
            '(彈彈彈',
            '(盯....'
        ])

    name_map = KeyAndAnswers(
        ['小海豹', '豹豹', '小豹豹'],
        [
            '在這裏!',
            '伸出圓手',
            '(滾動',
        ])

    party_map = KeyAndAnswers(
        [
            '(彈彈彈~ 🎵🎵~ 歐歐歐歐~ 🎵',
            '(翻滾～ 翻滾～'
        ])

    po_map = MyPet.po_map.update_answers(
        [
            '姐接姐接姐接姐接！',
            '(蹭蹭蹭蹭蹭'
        ])

    bro_map = MyPet.bro_map.update_answers(
        [
            '葛格葛格葛格葛格！',
            '(蹭蹭蹭蹭蹭'
        ])

    morning_map = MyPet.morning_map.update_answers(
        ['姐接早安！ 葛格早安！', '小動物幫早安！', '早安的好豹豹印章！']
    )

    good_night_map = MyPet.good_night_map.update_answers(
        ['姐接晚安！ 葛格晚安！', '小動物幫晚安！', '晚安暖暖趴！', '(擠擠棉被']
    )
