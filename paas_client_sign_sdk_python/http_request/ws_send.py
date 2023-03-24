import time
import websocket

from util.get_ws_sign import get_sign
from constant import *


def send_ws():

    url_params = URL_PARAMS.copy()

    # 获取当前时间（东8区）
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

    # 获取带签名URL
    url = get_sign(ACCESS_KEY_ID, ACCESS_KEY_SECRET, timestamp, WS_URL, url_params)

    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                header=None,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()


def on_message(ws, message):
    ws.send("Hello Server:" + str(time.time() * 1000))


def on_error(ws, error):
    print(error)


def on_close(ws):
    print(ws)


def on_open(ws):
    ws.send("Hello Server")
