
import urllib.request
import json


def get_token():
    apiKey = 'QWC0pIo6LdII0UGoiaAI0jLE'
    secretKey = 'b618a99d2851a7d0b655d5496085466e'
    aurh_url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(apiKey,secretKey)
    res = urllib.request.urlopen(aurh_url)
    json_data = res.read()
    print(json_data)
    print(type(json_data))
    return json.loads(str(json_data,encoding='utf-8'))['access_token']




r = get_token()
print(r)