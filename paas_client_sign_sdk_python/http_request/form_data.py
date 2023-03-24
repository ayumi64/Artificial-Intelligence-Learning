# -*- coding: utf-8 -*-
"""
author: yu.hailong
email: yuhailong@100tal.com
datetime: 2020/4/23 2:34 下午
description：
urlencoded methods
"""
import copy
import random, string, time
from util.send_sign_http import send_request
from constant import URL_PARAMS, ACCESS_KEY_ID, ACCESS_KEY_SECRET, HTTP_URL
from util.http import multipart_formdata, multipart_encoder
from requests_toolbelt.multipart import MultipartEncoder

FILE_PATH = "http_request/binary_content.txt"


class FormDataMethods(object):
    def __init__(self):
        self.header = multipart_formdata

    def response(self, method, payload=None, body_params={}):
        if payload is None:
            payload = copy.deepcopy(URL_PARAMS)

        # 获取当前时间（东8区）
        timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

        result = send_request(ACCESS_KEY_ID, ACCESS_KEY_SECRET, timestamp, HTTP_URL, payload, body_params,
                              method, self.header)
        return result

    @classmethod
    def post(cls):
        method = "POST"
        multipart_encoder_data = MultipartEncoder(
            fields={
                'save_name': 'test.txt',
                'save_data': ('test.txt', open(FILE_PATH, 'rb'), 'application/octet-stream')},
            boundary='------' + ''.join(random.sample(string.ascii_letters + string.digits, 32))
        )
        body_params = {
            multipart_encoder: multipart_encoder_data
        }
        return cls().response(method, body_params=body_params)

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
        multipart_encoder_data = MultipartEncoder(
            fields={
                'save_name': 'test.txt',
                'save_data': ('test.txt', open(FILE_PATH, 'rb'), 'application/octet-stream')},
            boundary='------' + ''.join(random.sample(string.ascii_letters + string.digits, 32))
        )
        body_params = {
            multipart_encoder: multipart_encoder_data
        }
        return cls().response(method, body_params=body_params)

    @classmethod
    def put(cls):
        method = "PUT"
        # 设置formdata参数
        multipart_encoder_data = MultipartEncoder(
            fields={
                'save_name': 'test.txt',
                'save_data': ('test.txt', open(FILE_PATH, 'rb'), 'application/octet-stream')},
            boundary='------' + ''.join(random.sample(string.ascii_letters + string.digits, 32))
        )
        body_params = {
            multipart_encoder: multipart_encoder_data
        }
        return cls().response(method, body_params=body_params)
