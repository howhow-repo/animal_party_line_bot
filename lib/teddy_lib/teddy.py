from lib.my_pet import MyPet


class Teddy(MyPet):
    food_map = [
        ['紅蘿蔔', 'carrot', '胡蘿蔔', '🥕'],
        [
            'PUI !?',
            'PUI! PUI! PUI!',
            '! (嗅嗅'
        ]
    ]
    name_map = [
        ['泰迪', '小泰迪'],
        [
            'PUI!',
            'PUI! PUI!'
        ]
    ]
    party_map = [
        MyPet.party_map[0],
        [
            '(Dancing~ 🎵🎵  Danceing~ 🎵🎵',
            '(轉轉~ 🎵🎵  跳跳~ 🎵🎵'
        ]
    ]

    po_map = [
        MyPet.po_map[0],
        [
            '姐接姐接姐接姐接！',
            '(蹭蹭蹭蹭蹭'
        ]
    ]

    bro_map = [
        MyPet.bro_map[0],
        [
            '葛格葛格葛格葛格！',
            '(蹭蹭蹭蹭蹭'
        ]
    ]