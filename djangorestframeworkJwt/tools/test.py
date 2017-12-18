#!/usr/bin/env python
# coding: utf8

"""
project: djangorestframeworkJwt
create date: 2017/12/18 
__author__ = xiashuangxi
"""

import requests


# 登录
auth_url = "http://localhost:8000/api-token-auth/"
data = {
    "username": "admin",
    "password": "password123"
}
r = requests.post(auth_url, data=data)
content = r.json()
token = content['token']
print token

# 刷新
refresh_url = "http://localhost:8000/api-token-refresh/"
data = {
    "token": token
}
r = requests.post(refresh_url, data=data)
content = r.json()
token = content['token']
print token

# 验证
verify_url = "http://localhost:8000/api-token-verify/"
data = {
    "token": token
}
r = requests.post(verify_url, data=data)
content = r.json()
token = content['token']
print token
