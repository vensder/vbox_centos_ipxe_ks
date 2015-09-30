#!/usr/bin/env python

import subprocess
from bottle import route, run, template, static_file


#Get the vboxnet0 ipaddr
intf = 'vboxnet0'
intf = 'virbr0'
intf_ip = subprocess.check_output(['ip', 'address', 'show', 'dev', intf]).split()
intf_ip = intf_ip[intf_ip.index('inet') + 1].split('/')[0]

#TODO Error checking
HOSTURL = "http://%s:4443" % (intf_ip)

BASEURL = "http://127.0.0.1:4443"

GUESTIP = '192.168.56.102'

@route('/images/<os>/<release>/x86_64/<filename>')
def index(os, release, filename):
    print 'images/%s/%s/x86_64' % (os, release), filename
    return static_file(filename, root='images/%s/%s/x86_64' % (os, release))


MAP = {
#       'xx:xx': (pxe, ks/cloud-config') 
#        'c7': ('centos7.pxe', 'centos7_minimal.ks'),
        'c7': ('centos7_minimal.pxe', 'centos7_minimal.ks'),
        }



@route('/<typ>/<mac>/')
def index(typ, mac):
    if typ not in ['ipxe', 'kickstart']:
        raise Exception

    if typ == 'ipxe':
        tplname = MAP[mac[-5:-3]][0]
        data = {'host_url': HOSTURL, 'base_url': BASEURL}

    elif typ == 'kickstart':
        tplname = MAP[mac[-5:-3]][1]
        data = {'host_url': HOSTURL, 'base_url': BASEURL}

    else:
        raise Exception


    print "Recieved %s and mac %s  Serving %s" % (typ, mac, tplname)

    tpl = file('templates/' + tplname).read()

    return template(tpl, **data)



run(host='0.0.0.0', port=4443)
