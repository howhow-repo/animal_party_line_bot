import jieba

from echolinebot.settings import BASE_DIR

jieba.load_userdict((BASE_DIR / 'jieba_dict.txt').name)


class MessageReceiver:

    @classmethod
    def echo(cls, text: str) -> str:
        return text

    @classmethod
    def split_sentence(cls, sentence):
        seg_list = jieba.lcut_for_search(sentence)
        print(seg_list)
        return seg_list
