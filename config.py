#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5822396703:AAG7sX8J2gaYpF9J_ZHGphpqZ4VXSdpF-P8")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "4018758"))
    API_HASH = os.environ.get("API_HASH", "622bba3cf046315531f71f9d97fa6c2a")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5385471287").split())
    
