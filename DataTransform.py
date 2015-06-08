__author__ = 'Steven'
import pymysql

def connDB(): #连接数据库函数
    conn=pymysql.connect(host='localhost', user='root', passwd='123456', db='businquire', charset='utf8')
    cur=conn.cursor()
    return (conn,cur)

def exeUpdate(conn, cur, sql): #更新语句，可执行update,insert语句
    sta=cur.execute(sql)
    conn.commit()
    return(sta)

#更新语句，可执行update,insert语句
def exeInsert(conn, cur, data):
    sta=cur.execute("insert into rawdata (Username,idPhone, timeStamp, accelerometer_x, accelerometer_y, accelerometer_z,gravity_x, gravity_y, gravity_z, gyroscope_x, gyroscope_y, gyroscope_z, magnetic_x, magnetic_y, magnetic_z, stationID, stationSignalTime, wifiID, wifiIntensity, GPS_x, GPS_y, GPS_z)  values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", data)
    conn.commit()
    return(sta)

#插入用户名密码，同时判断是否已经存在该用户名
def UserDataRegisInsert(conn, cur, data): #更新语句，可执行update,insert语句
    sql = cur.execute("select * from user_info where Username = %s",data[0])
    if(sql == 1):
        return None
    data.append(10)
    sta=cur.execute("insert into user_info (Username, Password, Point)  values(%s, %s, %s)", data)
    conn.commit()
    return(sta)

#查询语句
def exeQuery(cur, sql):
    cur.execute(sql)
    return (cur.fetchall())

#关闭所有连接
def connClose(conn, cur):
    cur.close()
    conn.close()

#存储所有信息
def saveAllData(allData):
    conn, cur = connDB()
    sta = exeInsert(conn, cur, allData)
    connClose(conn, cur)
    if(sta == 1):
        print("success")
        return 1
    else:
        print("it occurs problems when insert ", allData, "into database")
        return 0

#插入用户信息API
def saveUserData(UserData):
    conn, cur = connDB()
    sta = UserDataRegisInsert(conn, cur, UserData)
    connClose(conn, cur)
    if(sta == 1):
        print("success")
        return 1
    elif(sta == None):
        print("已经存在")
        return None
    else:
        print("it occurs problems when insert ", UserData, "into database")
        return 0

#用户登录功能API
def UserLogin(UserData):
    conn,cur =connDB()
    sql = cur.execute("select Point from user_info where Username = %s and Password = %s",UserData)
    connClose(conn,cur)
    if(sql == 1):
        point = cur.fetchone()
        return "登录成功,Point="+str(int(point[0]))
    else:
        return None

#读取最新数据
def readLatestData():
    conn,cur =connDB()
    sql = "select * from rawdata order by idRawData desc limit 1"
    r = exeQuery(cur,sql)
    connClose(conn,cur)
    return r[0]


if __name__=='__main__':
    data = ('xiaomi', '20150415',1.23434245,1.45245,1.245, 1.2452,1.245252,1.2452, 1.0,1.0,1.0, 1.0,1.0,1.0, 1.0,1.0, 1.0,1.0, 2.0,2.0,2.0)
    sta = saveAllData(data)
    #data = readLatestData()
    #print(data)

