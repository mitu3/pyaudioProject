import wave
from pyaudio import PyAudio,paInt16
import urllib.request
import json
import pycurl
import requests



framerate = 8000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 1

def save_wave_file(filename,data):
    '''save the data to the wan file'''
    wf = wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()

def my_record():
    pa = PyAudio()
    stream = pa.open(format = paInt16, channels = 1,
                     rate = framerate, input = True,
                     frames_per_buffer = NUM_SAMPLES)
    my_buf = []
    count = 0
    while count < TIME * 10:
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print('..')
    save_wave_file('01.wav',my_buf)
    stream.stop_stream()
    stream.close()



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


def use_cloud(token):
    fp = wave.open(u'01.wav','rb')
    nf = fp.getnframes()
    f_len = nf * 2
    audio_data = fp.readframes(nf)

    cuid = 'adbc'
    srv_url = 'http://vop.baidu.com/server_api?lan=zh&cuid={}&token={}'.format(cuid, token)
    # http_header = [
    #     'Content-Type : audio/wav; rate = 8000',
    #     'Cotent-Length : {}'.format(f_len)
    # ]
    http_header = {
        'Content-Type' : 'audio/wav; rate = 8000',
        'Cotent-Length' : '{}'.format(f_len)

    }
    # c = pycurl.Curl()
    # c.setopt(pycurl.URL, str(srv_url))
    # c.setopt(c.HTTPHEADER, http_header)
    # c.setopt(c.POST, 1)
    # c.setopt(c.CONNECTTIMEOUT, 80)
    # c.setopt(c.TIMEOUT, 80)
    # c.setopt(c.WRITEFUNCTION, dump_res)
    # c.setopt(c.POSTFIELDS, audio_data)
    # c.setopt(c.POSTFIELDSIZE, f_len)
    # c.perform()
    results = requests.get(srv_url,headers=http_header, data=audio_data)
    my_temp = results.json()
    print(my_temp)







my_record()
token = get_token()
print(token)
use_cloud(token)


print('over!')


