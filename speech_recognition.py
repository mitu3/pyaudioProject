import wave
from pyaudio import PyAudio,paInt16
import urllib.request
import json
import requests


def dump_res(buf):
    my_temp = json.loads(str(buf,encoding='utf-8'))
    my_list = my_temp['result']
    print(my_temp)
    print(type(my_list))
    print(my_list[0])


def get_token():
    apiKey = 'QWC0pIo6LdII0UGoiaAI0jLE'
    secretKey = 'b618a99d2851a7d0b655d5496085466e'
    aurh_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(apiKey,secretKey)
    res = urllib.request.urlopen(aurh_url)
    json_data = res.read()
    return json.loads(str(json_data, encoding='utf-8'))['access_token']


def use_cloud(file,token):
    fp = wave.open(file,'rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = 'adbc'
    srv_url = 'http://vop.baidu.com/server_api?lan=zh&cuid={}&token={}'.format(cuid, token)

    http_header = {
        'Content-Type' : 'audio/wav; rate = 8000',
        'Cotent-Length' : '{}'.format(f_len)

    }

    results = requests.get(srv_url,headers=http_header, data=audio_data)
    my_temp = results.json()
    frp = json.loads(results.text)

    print(frp['result'][0])




def speech_shi(files):
    result = use_cloud(files, get_token())
    print('over!')
    return result








