from http.server import HTTPServer,BaseHTTPRequestHandler
from DataTransform import readLatestData
import DataTransform
import io,shutil,socketserver
import time,string
from URLDataProcess import *
import ssl
#定义数据处理函数来处理每个数据包的关键信息，将关键信息存入列表中
def PutPacketData2List(PacketTime,littleList):
    if(len(info_List) == 0 or info_PacketTime[0] == PacketTime):
        info_List.append(littleList)
        info_PacketTime.append(PacketTime)
        print(info_List)
    elif(PacketTime != info_PacketTime[0]):#如果当前包的时间和list中的时间不一致，则进行聚类操作，并清空
        #聚类Process
        info_List.clear()
        info_PacketTime.clear()

class MyThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    pass


class MyHttpHandler(BaseHTTPRequestHandler):
    '''
    def handle(self):
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.load_cert_chain(certfile="myreq.pem")
        SSLSocket = context.wrap_socket(self.request, server_side=True)
        self.data = SSLSocket.recv(1024)
        print(self.data)
        buf = 'test HTTPS Server Handler%f'%time.time()
        buf = buf.encode()
        SSLSocket.send(buf)
        '''
    def do_GET(self):
        #地址转换为字典Dict
        p = path2dict(self.path)
        #地址转换为列表List
        t = path2list(self.path)
        #对请求的数据进行处理，返回处理结果，如果返回None代表处理失败（查询失败，注册失败，登录失败等）
        result = dataProcess(p)

        #根据数据包类型返回相应提示字符串
        if(p!=None and ('PacketType' in p)):
            if(p['PacketType'] =='1'):
                r_str = "查询结果:  "+"<br>"
            elif(p['PacketType']=='3'):
                r_str = "提交成功！"+"<br>"
            elif(p['PacketType']=='4'):
                r_str = "注册结果："+"<br>"
            elif(p['PacketType']=='5'):
                r_str = "登录结果："+"<br>"
        #如果请求成功，则将结果加入r_str中
        if(result!=None):
            r_str += str(result)

        #如果注册失败，添加到r_str中
        if(p!=None and ('PacketType' in p)):
            if(p['PacketType']=='4' and result ==None):
                r_str += '注册失败'
        #如果登录失败，添加到r_str中
        if(p!=None and ('PacketType' in p)):
            if(p['PacketType']=='5' and result ==None):
                r_str += '登录失败'
        #如果是查询数据则返回查询结果到r_str中
        if(t != None):
            if(p!=None and ('PacketType' in p)):
                if(p['PacketType']=='1'):
                    for each in t:
                        r_str = r_str + "<br>" + each[0] + "=" + each[1]
        #如果有相应的数据，则取出该数据，存入列表
        if(t != None):
            if(p!=None and ('PacketType' in p)):
                if(p['PacketType']=='3' and result !=None):
                    if(('IMEI' in p) and ('GPS_X' in p) and ('GPS_Y' in p) and ('GPS_Z' in p) and('PacketTime' in p)):
                        PacketTime = p['PacketTime']
                        IMEI = p['IMEI']
                        GPS_X = p['GPS_X']
                        GPS_Y = p['GPS_Y']
                        GPS_Z = p['GPS_Z']
                        littleList = [IMEI,float(GPS_X),float(GPS_Y),float(GPS_Z)]
                        PutPacketData2List(PacketTime,littleList)
        #返回相应的信息到客户端
        enc="UTF-8"
        encoded = ''.join(r_str).encode(enc)
        #print(encoded)
        f = io.BytesIO() #??????????????????????
        f.write(encoded)
        f.seek(0)  
        self.send_response(200)  
        self.send_header("Content-type", "text/html; charset=%s" % enc)  
        self.send_header("Content-Length", str(len(encoded)))  
        self.end_headers()  
        shutil.copyfileobj(f,self.wfile)#copy data from f to self.wfile




if __name__ == '__main__':
    #存储获取的用户数据
    info_List = []
    info_PacketTime = []
    #创建多线程的HTTP服务器
    httpd= MyThreadingHTTPServer(('127.0.0.1',8000),MyHttpHandler)
    print("Server started on 127.0.0.1,port 8000.....")
    httpd.serve_forever()
'''
    port = 443
    httpd= MyThreadingHTTPServer(('127.0.0.1',port),MyHttpHandler)
    #httpd = socketserver.TCPServer(('localhost‘, port), MyHTTPSHandler_socket)
    print('https serving at port', port)
    httpd.serve_forever()
    '''