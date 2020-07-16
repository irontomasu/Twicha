#!/usr/bin/python
#-*- coding: utf-8 -*-
import tweepy


consumer_key = '5oM4yP4oWyzLVKOWZzpC46z7f'
consumer_secret = 'EwRKQqlBnUwiGZ38u6UMONHli0sNcRnAdKRbogzgXSPvutRhhh'
access_token = '1199166647455477760-4sgRmgoQXbSDWFnnQZuPYDB0cIvTlH'
access_secret = 'nma2MYHPsYu02BDYEgSFDyH7FMwjR1WuR3DQKA2ItYIn8'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)


api.update_status('peropero')
