import sys
sys.path.append('/opt/rrdtool-1.4.8/lib/python2.7/site-packages/')
import rrdtool

def rrdcreate():
    data_sources=[ 'DS:mem:GAUGE:600:0:U',
                   'DS:cpu:GAUGE:600:0:U',
                   'DS:disk:GAUGE:600:0:U',
                   'DS:netout:COUNTER:600:0:U',
                   'DS:netin:COUNTER:600:0:U',
                   'DS:ior:COUNTER:600:0:U',
                   'DS:iow:COUNTER:600:0:U']

    rrdtool.create( '/data/monitor.rrd',
                    '--start', '1357005600',
                    '--step', '60',
                    data_sources,
                    'RRA:AVERAGE:0.5:1:14400',
                    'RRA:AVERAGE:0.5:6:4800',
                    'RRA:AVERAGE:0.5:24:1200',
                    'RRA:AVERAGE:0.5:288:600',
                    'RRA:MAX:0.5:1:14400',
                    'RRA:MAX:0.5:6:4800',
                    'RRA:MAX:0.5:24:1200',
                    'RRA:MAX:0.5:288:600' )

def rrdupdata(get_time=0,mem=0,cpu=0,disk=0,netout=0,netin=0,ior=0,iow=0):
    rrdtool.update('/data/monitor.rrd',
                    '%(get_time)s:%(mem)s:%(cpu)s:%(disk)s:%(netout)s:%(netin)s:%(ior)s:%(iow)s' % {'get_time':get_time,'mem':mem,'cpu':cpu,'disk':disk,'netout':netout,'netin':netin,'ior':ior,'iow':iow})


