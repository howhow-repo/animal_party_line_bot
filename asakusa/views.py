from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from lib import Asakusa


line_bot_api = LineBotApi(settings.ASAKUSA_LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.ASAKUSA_LINE_CHANNEL_SECRET)


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
        resp_text = Asakusa.pickone('short')
        print(resp_text)
        return HttpResponse(resp_text)
