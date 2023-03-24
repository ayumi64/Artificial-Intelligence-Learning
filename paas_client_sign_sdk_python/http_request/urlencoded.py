# -*- coding: utf-8 -*-
"""
author: yu.hailong
email: yuhailong@100tal.com
datetime: 2020/4/23 2:34 下午
description：
urlencoded methods
"""

import time
import copy
from util.send_sign_http import send_request
from constant import URL_PARAMS, ACCESS_KEY_ID, ACCESS_KEY_SECRET, HTTP_URL, BODY_PARAMS
from util.http import application_x_www_form_urlencoded


class UrlencodedMethods(object):
    def __init__(self):
        self.header = application_x_www_form_urlencoded

    def response(self, method, payload=None, body_params=None):
        # 北京时间
        if payload is None:
            payload = copy.deepcopy(URL_PARAMS)

        if body_params is None:
            body_params = copy.deepcopy(BODY_PARAMS)

        # 获取当前时间（东8区）
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

        result = send_request(ACCESS_KEY_ID, ACCESS_KEY_SECRET, timestamp, HTTP_URL, payload, body_params, method,
                              application_x_www_form_urlencoded)
        return result

    @classmethod
    def post(cls):
        method = "POST"
        return cls().response(method)

    @classmethod
    def get(cls):
        method = "GET"
        return cls().response(method, {})

    @classmethod
    def delete(cls):
        method = "DELETE"
        return cls().response(method)

    @classmethod
    def patch(cls):
        method = "PATCH"
        return cls().response(method)

    @classmethod
    def put(cls):
        method = "PUT"
        return cls().response(method)
