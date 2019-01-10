#!/usr/bin/python
#-*- coding: utf-8 -*-

import requests
resp = requests.get('https://www.baidu.com')
text = resp.content.decode('utf-8')
print(text)
print('hello')
