__author__ = 'Tree'
import socketserver, ssl, time

class MyHTTPSHandler_socket(socketserver.BaseRequestHandler):
    def handle(self):
        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        #context.load_cert_chain(certfile="cakey.pem")
        SSLSocket = context.wrap_socket(self.request, server_side=True)
        self.data = SSLSocket.recv(1024)
        print(self.data)
        buf = 'test HTTPS Server Handler%f'%time.time()
        buf = buf.encode()
        SSLSocket.send(buf)

if __name__ == "__main__":
    port = 443
    httpd = socketserver.TCPServer(('localhost', port), MyHTTPSHandler_socket)
    print('https serving at port',port)
    httpd.serve_forever()