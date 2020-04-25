#!/usr/bin/python
#-*- coding: utf-8 -*-
import tweepy

#認証を行う
consumer_key = '5oM4yP4oWyzLVKOWZzpC46z7f'
consumer_secret = 'EwRKQqlBnUwiGZ38u6UMONHli0sNcRnAdKRbogzgXSPvutRhhh'
access_token = '1199166647455477760-BVDYxHwTOyfVoTZP5sq5AzEcbBrrQk'
access_secret = 'QJmuywTtvv28ZAFfv2wHikc42bjd6I7iYQUUWOZEeSsAf'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#Hello, world!と投稿する
api.update_status('Hello, world!')