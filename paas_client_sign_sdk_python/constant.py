import os
import json


def get_base_dir():
    return os.path.dirname(os.path.abspath(__file__))


# 填写自己AK
# 获取AK教程：https://openai.100tal.com/documents/article/page?fromWhichSys=admin&id=27
ACCESS_KEY_ID = "5328703320949760"
ACCESS_KEY_SECRET = "378d3f0d70ea47a39cea73dcac7c06e7"

# 所属环境
HTTP_ENV_URL = "http://openai.100tal.com"
# 能力地址
HTTP_API_URL = "/aiimage/handrecognition"
# 请求URL，请替换自己的真实地址
HTTP_URL = HTTP_ENV_URL + HTTP_API_URL

# 所属环境
WS_ENV_URL = "ws://openai.100tal.com"
# 能力地址
WS_API_URL = "/ai---/----"
# 请求URL，请替换自己的真实地址
WS_URL = WS_ENV_URL + WS_API_URL

# 据接口要求，填写真实URL参数。key1、key2仅做举例
URL_PARAMS = {
    "ACCESS_KEY_ID": "___",
    "ACCESS_KEY_SECRET": "__"
}

# 根据接口要求，填写真实URL参数。key1、key2仅做举例
BODY_PARAMS = {
    "image_url": "https://pro-image.xiaoheiban.cn/bin/3cfd6dfe-0691-4c20-8cea-e6f689eb908e.jpg",
    # "image_base64": "base64",
    "ifche": 0,
    'answer':[]
}

# 二进制文件。 文件内容
FILE_PATH = get_base_dir() + "/files/binary_content.txt"