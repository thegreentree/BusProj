from DataTransform import *

#将带等号的字符串返回为元组
def param2tuple(s):
    return tuple(s.split('='))
#将路径返回为字典
def path2dict(s):
    p = s.split('?')
    if len(p) == 2:
        return dict(list(map(param2tuple, p[1].split('&'))))

#将路径返回为列表
def path2list(s):
    p = s.split('?')
    if len(p) == 2:
        listA = list(map(param2tuple,p[1].split('&')))
        #print(listA)
        return listA

#对数据包进行处理
def dataProcess(p):
    if(p!=None):
        #包类型为查询请求数据包
        if(('PacketType' in p) and (p['PacketType']=='1')):
            #Get the User Request Information
            #初始化数据
            IMEI = -1
            BusLineNum = -1
            Direction = -1
            X = -1
            Y = -1
            Z = -1
            #判断如果相应字段有数据再进行处理
            if('IMEI' in p):
                IMEI = p['IMEI']
            if('BusLineNum' in p):
                BusLineNum = int(p['BusLineNum'])
            if('Direction' in p):
                Direction = int(p['Direction'])
            if('X' in p):
                X = float(p['X'])
            if('Y' in p):
                Y = float(p['Y'])
            if('Z' in p):
                Z = float(p['Z'])
            #Process the data to getting the BusResult
            #～～～～～～～～～
            #！～～～～～～～～～
            #return the result of the busline
            showString = [p['PacketType'],IMEI,BusLineNum,Direction,X,Y,Z]
            #print(showString)
            return readLatestData()
        #包类型为所有数据数据包
        elif(('PacketType' in p) and (p['PacketType']=='3')):
            #初始化数据
            Username = -1
            IMEI = -1
            PacketTime = -1
            X1 = -1
            Y1 = -1
            Z1 = -1
            X2 = -1
            Y2 = -1
            Z2 = -1
            X3 = -1
            Y3 = -1
            Z3 = -1
            X4 = -1
            Y4 = -1
            Z4 = -1
            StationID = -1
            SignalTime = -1
            WiFiID = -1
            WiFiIntensity = -1
            GPS_Z = -1
            GPS_Y = -1
            GPS_X = -1

            #判断如果相应字段有数据再进行处理
            if('Username' in p):
                Username = p['Username']
            if('IMEI' in p):
                IMEI = p['IMEI']
            PacketTime = p['PacketTime']
            if('X1' in p):
                X1 = float(p['X1'])
            if('Y1' in p):
                Y1 = float(p['Y1'])
            if('Z1' in p):
                Z1 = float(p['Z1'])
            if('X2' in p):
                X2 = float(p['X2'])
            if('Y2' in p):
                Y2 = float(p['Y2'])
            if('Z2' in p):
                Z2 = float(p['Z2'])
            if('X3' in p):
                X3 = float(p['X3'])
            if('Y3' in p):
                Y3 = float(p['Y3'])
            if('Z3' in p):
                Z3 = float(p['Z3'])
            if('X4' in p):
                X4 = float(p['X4'])
            if('Y4' in p):
                Y4 = float(p['Y4'])
            if('Z4' in p):
                Z4 = float(p['Z4'])
            if('StationID' in p):
                StationID = p['StationID']
            if('SignalTime' in p):
                SignalTime = p['SignalTime']
            if('WiFiID' in p):
                WiFiID = p['WiFiID']
            if('WiFiIntensity' in p):
                WiFiIntensity = float(p['WiFiIntensity'])
            if('GPS_X' in p):
                GPS_X = float(p['GPS_X'])
            if('GPS_Y' in p):
                GPS_Y = float(p['GPS_Y'])
            if('GPS_Z' in p):
                GPS_Z = float(p['GPS_Z'])
            DataPacket = [Username,IMEI,PacketTime,X1,Y1,Z1,X2,Y2,Z2,X3,Y3,Z3,X4,Y4,Z4,StationID,SignalTime,WiFiID,WiFiIntensity,GPS_X,GPS_Y,GPS_Z]
            saveAllData(DataPacket)#将数据插入数据库中
            print(DataPacket)
            return "Insert Success"
        #对注册请求进行处理
        elif(('PacketType' in p) and (p['PacketType']=='4')):
            IMEI = -1
            PacketTime = -1
            Username = ""
            Password = ""
            if('IMEI' in p):
                IMEI = p['IMEI']
            if('PacketTime' in p):
                PacketTime = p['PacketTime']
            if('Username' in p):
                Username = p['Username']
            if('Password' in p):
                Password = p['Password']
            if(Username != "" and Password !=""):
                try:
                    UserData = [Username,Password]
                    result = saveUserData(UserData)
                    if(result == None):
                        return None
                except Exception as e:
                    print(e)
                    return None#插入失败
                return "注册成功"#插入成功
            return None
            #return readLatestData()
        #对登录请求进行处理
        elif(('PacketType' in p) and (p['PacketType']=='5')):
            IMEI = -1
            PacketTime = -1
            Username = ""
            Password = ""
            if('IMEI' in p):
                IMEI = p['IMEI']
            if('PacketTime' in p):
                PacketTime = p['PacketTime']
            if('Username' in p):
                Username = p['Username']
            if('Password' in p):
                Password = p['Password']
            if(Username != "" and Password !=""):
                Userdata = [Username,Password]
                result = UserLogin(Userdata)
                return result
            return None
    return None

