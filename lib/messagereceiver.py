import jieba

from core.settings import BASE_DIR

jieba.load_userdict('/home/ubuntu/animal_party_line_bot/jieba_dict.txt')


class MessageReceiver:

    @classmethod
    def echo(cls, text: str) -> str:
        return text

    @classmethod
    def split_sentence(cls, sentence):
        seg_list = jieba.lcut_for_search(sentence)
        print(seg_list)
        return seg_list
