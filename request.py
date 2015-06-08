# -*- coding: utf-8 -*-
from requests.packages.urllib3.poolmanager import PoolManager
import urllib
import time
import requests
import ssl

def urlRequest(s):
    r = urllib.request.urlopen(s)
    return r.read()

#Convert the Result to List
def ProcessResult(str):
    des = str.split('<br>')
    if(des[1]==''):
        return None
    des2 = des[1].replace('(','')
    des2 = des2.replace(')','')
    des2 = des2.replace('\'','')
    listDes2  = des2.split(',')
    return listDes2
'''
class MyAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize,block=False):
        self.poolmanager = PoolManager(num_pools=connections,
            maxsize=maxsize,block=block,
            ssl_version=ssl.PROTOCOL_SSLv3)
'''


if __name__ == '__main__':
    #提交数据URL
    url = "http://127.0.0.1:8000/?PacketType=3&Username=testUser&IMEI=xiaomi&PacketTime=2015-05-28:14:10:28&X1=1.11&Y1=1.22&Z1=1.33&X2=2.11&Y2=2.22&Z2=2.33&X3=3.11&Y3=3.22&Z3=3.33&X4=4.11&Y4=4.22&Z4=4.33&StationID=testStation&SignalTime=2014-05-28:14:13:70&WiFiID=treeWifi&WiFiIntensity=32.4&GPS_X=1&GPS_Y=2&GPS_Z=3"
    #注册用户URL
    #url = "http://127.0.0.1:8000/?PacketType=4&IMEI=xiaomi&PacketTime=2015-05-28:14:10:28&Username=testUsername1&Password=12345"
    #登录账户URL
    #url = "http://127.0.0.1:8000/?PacketType=5&IMEI=xiaomi&PacketTime=2015-05-28:14:10:28&Username=testUsername1&Password=12345"
    r = urlRequest(url)
    dec="UTF-8"
    str = r.decode(dec)
    print(str)
    #Convert the Result to List
    try:
        listA = ProcessResult(str)
    except Exception as e:
        print(e)
    if(listA != None):
        print(listA)
    time.sleep(1)



'''
 #while 1==1:
 url = 'https://127.0.0.1:443/dd'
 s = requests.Session()
 s.mount('https://', MyAdapter())#所有的https连接都用ssl.PROTOCOL_SSLV3去连接
 #a = requests.adapters.HTTPAdapter(max_retries=3)
 #s.mount('http://', a)
 r = s.get(url)
 print(r)
'''


'''
if __name__ == '__main__':
 username = 'username'
 password = 'password'
 email = 'email@example.com'
 url = 'https://api.example.com/'
 headers = {'Accept': 'application/json', 'content-type': 'application/json'}
 params = {'emailaddress': email}
 auth = (username, password)

 s = requests.Session()
 s.mount(url, MyAdapter())
 #r = s.get(url+'customer.svc/search', params=params, auth=auth, headers=headers)

 x = s.get('https://github.com/timeline.json')
 print(x.json)
 print(x.text)
 #print(x.encoding)
 '''

