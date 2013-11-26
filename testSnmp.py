#! /usr/bin/env python
import os
import time



def snmp_mem():
    snmpwalk_memTotal = "snmpwalk -v 2c -c public 127.0.0.1 UCD-SNMP-MIB::memTotalReal.0"
    res_memTotal = os.popen(snmpwalk_memTotal).read()
    memTotal = int((res_memTotal.split(': ')[-1]))
#    print memTotal

    snmpwalk_memAvail = "snmpwalk -v 2c -c public 127.0.0.1 UCD-SNMP-MIB::memAvailReal.0"
    res_memAvail = os.popen(snmpwalk_memAvail).read()
    memAvail = int((res_memAvail.split(': ')[-1]))
#    print memAvail

    snmpwalk_memBuffer = "snmpwalk -v 2c -c public 127.0.0.1 UCD-SNMP-MIB::memBuffer.0"
    res_memBuffer = os.popen(snmpwalk_memBuffer).read()
    memBuffer = int((res_memBuffer.split(': ')[-1]))
#    print memBuffer

    snmpwalk_memCached = "snmpwalk -v 2c -c public 127.0.0.1 UCD-SNMP-MIB::memCached.0"
    res_memCached = os.popen(snmpwalk_memCached).read()
    memCached = int((res_memCached.split(': ')[-1]))
#    print memCached

    Mem = int((float(memTotal-memAvail-memBuffer-memCached)/float(memTotal))*100)
#    print Mem
    return Mem

def snmp_cpu():
    snmpwalk_cpu = "snmpwalk -v 2c -c public 127.0.0.1   -On .1.3.6.1.2.1.25.3.3.1.2"
    res_cpu = os.popen(snmpwalk_cpu).read()
    cpu = int((res_cpu.split(': ')[-1]))
    return cpu

def snmp_disk():
    snmpwalk_disk ="snmpwalk -v 2c -c public 127.0.0.1    UCD-SNMP-MIB::dskAvail.1"
    res_disk = os.popen(snmpwalk_disk).read()
    disk_b = float((res_disk.split(': ')[-1]))
    disk = round(disk_b/1048576,2)
        
    return disk

def snmp_networkout():
    snmpwalk_networkout ="snmpwalk -v 2c -c public 127.0.0.1    IF-MIB::ifOutOctets.2"
    res_netout = os.popen(snmpwalk_networkout).read()
    netout = int(res_netout.split(': ')[-1])
    return netout

def snmp_networkin():
    snmpwalk_networkin ="snmpwalk -v 2c -c public 127.0.0.1    IF-MIB::ifInOctets.2"
    res_netin = os.popen(snmpwalk_networkin).read()
    netin = int(res_netin.split(': ')[-1])
    return netin

def get_time():
    dtime = time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
    return dtime

def disk_io_w(id):
    snmpwalk_io_w = "snmpwalk -v 2c -c public 127.0.0.1 UCD-SNMP-MIB::ucdavis.57.101.%s" % id
    res_io_w = os.popen(snmpwalk_io_w).read()
    io_w = int(res_io_w.split('"')[1])
    return io_w

def disk_io_r(id):
    snmpwalk_io_r = "snmpwalk -v 2c -c public 127.0.0.1 UCD-SNMP-MIB::ucdavis.58.101.%s" % id
    res_io_r = os.popen(snmpwalk_io_r).read()
    io_r = int(res_io_r.split('"')[1])
    return io_r


  
if __name__ == '__main__':
  t = snmp_mem()
  print t
  c = snmp_cpu()
  print c
  d = snmp_disk()
  print d    
  n = snmp_networkout()
  print n
  i = snmp_networkin()
  print i
  dt = get_time()
  print dt
  iow = disk_io_w(18)
  print iow
  ior = disk_io_r(18)
  print ior