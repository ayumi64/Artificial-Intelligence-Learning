#sonic账号地址
APP_ID = '20545078'
API_KEY = 'qROAdLBMg7msxQgCB5FBwXIc'
SECRECT_KEY = '2KEtyNrmIstLt48hzMvnAXaNMQKg88a6'

# 利用aip进行识别
def identify_words(index=0):
    from aip import AipOcr
    client = AipOcr(APP_ID, API_KEY, SECRECT_KEY)
    with open(r'AI-Lab/OCR/page.png', 'rb') as f:
        img = f.read()
    message = client.basicGeneral(img)
    res = message['words_result']
    print(res)
    print('识别结果为: %s' % res[0]['words'])
    if len(res) == 0:
        return '1'
    else:
        return res[index]['words']

if __name__ == '__main__':
    identify_words()