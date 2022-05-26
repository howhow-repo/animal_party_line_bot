"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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


def main_page(request):
    return HttpResponseRedirect("/admin")


urlpatterns = [
    path('', main_page),
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


line_bot_api = LineBotApi(settings.ASAKUSA_LINE_CHANNEL_ACCESS_TOKEN)
TIME_ZONE = "Asia/Taipei"
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
