'''def exc1(host,port,db,charset):
    conn=connect(host,port,db,charset)
    conn.execute(sql)
    return xxx
def exc2(host,port,db,charset,proc_name):
    conn=connect(host,port,db,charset)
    conn.call_proc(sql)
    return xxx
# 每次调用都需要重复传入一堆参数
# exc1('127.0.0.1',3306,'db1','utf8','select * from tb1;')
# exc2(‘127.0.0.1’,3306,'db1','utf8','存储过程的名字')'''


class Exc:
    def __init__(self, host, port, db, charset):
        self.host = host
        self.port = port
        self.db = db
        self.charset = charset

    def exc1(self):
        conn = connect(self.host, self.port, self.db, self.charset)
        conn.execute(sql)
        return xxx

    def exc2(self, operation):
        conn = connect(self.host, self.port, self.db, self.charset, operation)
        conn.call_proc(sql)
        return xxx


exc_sub1 = Exc()
exc_sub1.exc1()
exc_sub1.exc2('select * from tb1;')