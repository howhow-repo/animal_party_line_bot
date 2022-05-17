import json, os
import random

import jieba
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

line_bot_api = LineBotApi(settings.ASAKUSA_LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.ASAKUSA_LINE_CHANNEL_SECRET)


def split_sentence(sentence):
    seg_list = jieba.lcut_for_search(sentence)
    return seg_list


class Asakusa:
    keywords = ['問神', '運勢']
    with open(f'{os.path.dirname(__file__)}/asakusa.json', 'r') as f:
        datas = json.load(f)

    @classmethod
    def react(cls, message):
        if cls.check_if_ask(message):
            return cls.pickone()
        else:
            return None

    @classmethod
    def check_if_ask(cls, message):
        splited_list = split_sentence(message)
        for k in cls.keywords:
            if k in splited_list:
                return True
        return False

    @classmethod
    def pickone(cls):
        raw_pick = cls.datas[random.randint(0, 99)]
        return cls.format_to_line(raw_pick)

    @classmethod
    def format_to_line(cls, one_sign: dict):
        text = f"💮{one_sign['type']}\n" \
               f"📜{one_sign['poem']}\n" \
               f"📝{one_sign['explain']}\n" \
               f"----\n"
        print()
        for k, v in one_sign['result'].items():
            text += f"{k}: {v}\n"
        return text


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)  # 傳入的事件
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent) and event.message.type == 'text':  # 如果有訊息事件
                resp_text = Asakusa.react(event.message.text)
                print(resp_text)
                if resp_text is not None:
                    line_bot_api.reply_message(  # 回復傳入的訊息文字
                        event.reply_token,
                        TextSendMessage(text=resp_text)
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def test_stage(request):
    if request.method == 'GET':
        resp_text = Asakusa.pickone()
        return HttpResponse(resp_text)
