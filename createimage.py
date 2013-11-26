import os
import time
import rrdtool
import sys
sys.path.append('/opt/rrdtool-1.4.8/lib/python2.7/site-packages/')

rrd = '/data/monitor.rrd'
def createimage_mem():
    timetemp = (int(time.time())-3600)
    rrdtool.graph('/data/image_mem.png',
                  '--imgformat', 'PNG',
                  '--start', '%(timetemp)s' % {'timetemp':timetemp},
                  'DEF:Mem=%(rrd)s:mem:AVERAGE' % {'rrd':rrd},

                  'LINE1:Mem#FF0000:Mem')
                
def createimage_net():
    timetemp = (int(time.time())-3600)
    rrdtool.graph('/data/image_net.png',
                  '--imgformat', 'PNG',
                  '--start', '%(timetemp)s' % {'timetemp':timetemp},
                  'DEF:Netout=%(rrd)s:netout:AVERAGE' % {'rrd':rrd},
                  'DEF:Netin=%(rrd)s:netin:AVERAGE' % {'rrd':rrd},
                  'LINE1:Netout#FF0000:Netout',
                  'LINE2:Netin#0000ff:Netin'                            
                        )

    
def createimage_disk():
    timetemp = (int(time.time())-3600)
    rrdtool.graph('/data/image_disk.png',
                   '--imgformat', 'PNG',
                   '--start', '%(timetemp)s' % {'timetemp':timetemp},
                   'DEF:Disk=%(rrd)s:disk:AVERAGE' % {'rrd':rrd},
    
                   'AREA:Disk#990033:disk')

def createimage_io():
    
    timetemp = (int(time.time())-3600)
    rrdtool.graph('/data/image_io.png',
                  '--imgformat', 'PNG',
                  '--start', '%(timetemp)s' % {'timetemp':timetemp},
                  'DEF:Iow=%(rrd)s:iow:AVERAGE' % {'rrd':rrd},
                  'DEF:Ior=%(rrd)s:ior:AVERAGE' % {'rrd':rrd},
                  'LINE1:Iow#FF0000:write',
                  'LINE2:Ior#0000ff:read'                            
                        )
    
    


while True:
    createimage_mem()
    createimage_net()
    createimage_disk()
    createimage_io()
    time.sleep(600)    


