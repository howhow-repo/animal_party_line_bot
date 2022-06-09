from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage
from decouple import config


MY_GROUP_ID = config('MY_GROUP_ID')
line_bot_api = LineBotApi(settings.ASAKUSA_LINE_CHANNEL_ACCESS_TOKEN)
TIME_ZONE = "Asia/Taipei"


urlpatterns = [
    path('', lambda request: HttpResponseRedirect("/admin")),
    path('admin/', admin.site.urls, name='admin'),
    path('echo/', include('echo.urls')),
    path('teddy/', include('teddybot.urls')),
    path('littleseal/', include('littlesealbot.urls')),
    path('asakusa/', include('asakusa.urls')),
]


def noon_alarm():
    line_bot_api.push_message(
        to=MY_GROUP_ID,
        messages=TextSendMessage(text='各位～ 別工作了～ 該吃午餐了～')
    )


scheduler = BackgroundScheduler()
scheduler.add_job(
        noon_alarm,
        trigger=CronTrigger(
            day_of_week='mon-fri', hour='11', minute='59', second='50',
            timezone=TIME_ZONE,
        ),
        id="noon_alarm",
        max_instances=1,
    )
try:
    scheduler.start()
except KeyboardInterrupt:
    scheduler.shutdown()
