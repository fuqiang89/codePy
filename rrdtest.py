import sys
sys.path.append('/opt/rrdtool-1.4.8/lib/python2.7/site-packages/')
import rrdtool

def rrdcreate():
    data_sources=[ 'DS:mem:GAUGE:30:0:U',
                   'DS:cpu:GAUGE:30:0:U',
                   'DS:disk:GAUGE:30:0:U',
                   'DS:netout:COUNTER:30:0:U',
                   'DS:netin:COUNTER:30:0:U',
                   'DS:ior:COUNTER:30:0:U',
                   'DS:iow:COUNTER:30:0:U']
    
    rrdtool.create( '/data/monitor.rrd',
                    '--start', '1357005600',
                    '--step', '20',
                    data_sources,
                    'RRA:AVERAGE:0.5:1:86400',
                    'RRA:AVERAGE:0.5:2:43200',
                    'RRA:AVERAGE:0.5:10:12000',
                    'RRA:AVERAGE:0.5:120:800' )

def rrdupdata(get_time=0,mem=0,cpu=0,disk=0,netout=0,netin=0,ior=0,iow=0):
    rrdtool.update('/data/monitor.rrd',
                    '%(get_time)s:%(mem)s:%(cpu)s:%(disk)s:%(netout)s:%(netin)s:%(ior)s:%(iow)s' % {'get_time':get_time,'mem':mem,'cpu':cpu,'disk':disk,'netout':netout,'netin':netin,'ior':ior,'iow':iow})
                    

#rrdcreate()
#rrdupdata()
    

