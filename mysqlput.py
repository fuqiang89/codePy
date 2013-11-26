#!/usr/bin/python
#encoding=utf-8 
__author__ = 'fuqiang'

import MySQLdb


class mysqlc:
    def __init__(self):
        self.conn = MySQLdb.connect(host="192.168.5.130", user="fuqiang", passwd="adminos", charset="UTF8", db="osdata")
        self.curm = self.conn.cursor()
        if not self.curm:
            raise(NameError,"db access failed")
    
        
        
def test():
    c = mysqlc()
    try:
        sql = c.curm.execute('select * from Data')
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#    print sql
    return sql


def updata(get_time=0,snmp_mem=0,snmp_cpu=0,snmp_disk=0,snmp_networkin=0,snmp_networkout=0,disk_io_w=0,disk_io_r=0):
    c = mysqlc()
    id = c.conn.insert_id()
    sql = """insert into Data(id,get_time,snmp_mem,snmp_cpu,snmp_disk,snmp_networkin,snmp_networkout,disk_io_w,disk_io_r) values('%(id)s','%(get_time)s','%(snmp_mem)s','%(snmp_cpu)s','%(snmp_disk)s','%(snmp_networkin)s','%(snmp_networkout)s','%(disk_io_w)s','%(disk_io_r)s')""" % {'id':id,'get_time':get_time,'snmp_mem':snmp_mem,'snmp_cpu':snmp_cpu,'snmp_disk':snmp_disk,'snmp_networkin':snmp_networkin,'snmp_networkout':snmp_networkout,'disk_io_r':disk_io_r,'disk_io_w':disk_io_w}
    #print sql
    try:
            sql = c.curm.execute(sql)
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#    c.curm.commit()
    c.curm.close()
    c.conn.close()


#updata(snmp_cpu=123,snmp_disk=40,disk_io_r=90)





