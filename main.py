#!/usr/bin/python
#encoding=utf-8 
__author__ = 'fuqiang'
import os
import MySQLdb
import mysqlput
import snmp
import rrd
import time

rrd.rrdcreate()
while True:
    snmpwalk_memTotal = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.4.5.0')
    snmpwalk_memAvail = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.4.6.0')
    snmpwalk_memBuffer = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.4.14.0')
    snmpwalk_memCached = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.4.15.0')
    
    snmp_mem = int((float(snmpwalk_memTotal-snmpwalk_memAvail-snmpwalk_memBuffer-snmpwalk_memCached)/float(snmpwalk_memTotal))*100)
    
    snmp_cpu = snmp.snmpwalk(oid='1.3.6.1.2.1.25.3.3.1.2')
    
    snmp_disk = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.9.1.7')
    
    snmp_networkout = snmp.snmpwalk(oid='1.3.6.1.2.1.2.2.1.16.2')
    
    snmp_networkin = snmp.snmpwalk(oid='1.3.6.1.2.1.2.2.1.10.2')
    
    get_time = snmp.get_time()
    
    disk_io_r = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.58.101.18')
    
    disk_io_w = snmp.snmpwalk(oid='1.3.6.1.4.1.2021.57.101.18')
    
    #print snmp_mem
    
    #print snmpwalk_memAvail
    #print snmpwalk_memBuffer
    #print snmpwalk_memCached
    #print snmpwalk_memTotal
    #print snmp_cpu
    
    #print snmp_disk
    
    #print  snmp_networkin
    
    #print  snmp_networkout
    
    #print disk_io_r
    
    #print disk_io_w
    
    #print  get_time
    
    #mysqlput.updata(snmp_mem=snmp_mem,snmp_cpu=snmp_cpu,snmp_disk=snmp_disk,snmp_networkin=snmp_networkin,snmp_networkout=snmp_networkout,get_time=get_time,disk_io_r=disk_io_r,disk_io_w=disk_io_w)
    
#    rrd.rrdcreate()
    
    rrd.rrdupdata(get_time=get_time,mem=snmp_mem,cpu=snmp_cpu,disk=snmp_disk,netout=snmp_networkout,netin=snmp_networkin,ior=disk_io_r,iow=disk_io_w)
    print get_time
    time.sleep(10)
    




