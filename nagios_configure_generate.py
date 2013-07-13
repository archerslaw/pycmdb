#!/usr/bin/python

import urllib, urllib2
import json
import os

CURR_DIR=os.path.abspath(os.path.dirname(__file__))
HOST_CONF_DIR=os.path.join(CURR_DIR,'hostsconfig')

HOST_TMP = """define host {
    use               chscity-server
    host_name         %(hostname)s
    alias             %(hostname)s
    address           %(ipaddr)s
    contact_groups    chscity_contacts
    }
"""

def getHosts():
    url = "http://192.168.3.121:8000/api/gethosts.json"
    return json.loads(urllib2.urlopen(url).read())

def initDir():
    if not os.path.exists(HOST_CONF_DIR):
        os.mkdir(HOST_CONF_DIR)
    return True
 
def writeFile(f,s):
    with open(f,'w') as fd:
        fd.write(s)
    return True

def genNagiosHost(hostdata):
    initDir()
    conf = os.path.join(HOST_CONF_DIR,'hosts.cfg')
    hostconf = ""
    for hg in hostdata:
        for h in hg['members']:
            #print hg['hostgroup'],h['hostname']
            #hostconf += HOST_TMP % h
            if h['ipaddr']:
                hostconf += HOST_TMP % {'hostname':h['hostname'], 'ipaddr': h['ipaddr']}
    return writeFile(conf,hostconf)

def main():
    result = getHosts()
    if result['status'] == 1:
        genNagiosHost(result['data'])
        print 'Generate the nagios of host successfully!'
    else:
        print 'Error: %s, Please check it again.' % result['message']
    return True

if __name__ == "__main__":
    main()

