# -*- coding: utf-8 -*-
"""
author: yu.hailong
email: yuhailong@100tal.com
datetime: 2020/4/23 2:56 下午
description：
"""

# # Content-Type:application/json
# from http_request.urlencoded import UrlencodedMethods

# # Content-Type: Form_Data
# from http_request.form_data import FormDataMethods

# Content-Type:application/json
from http_request.application_json import ApplicationJsonMethods

# from http_request.binary import BinaryMethods


def main():
    class_name = ApplicationJsonMethods

    # print(class_name.get())
    print(class_name.post())
    # print(class_name.patch())
    # print(class_name.delete())
    # print(class_name.put())


# http测试入口
if __name__ == '__main__':
    main()
