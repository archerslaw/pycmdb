#!/usr/bin/python
#coding=utf-8

from subprocess import Popen, PIPE
import re
import urllib
import urllib2
import platform

def getIfconfig():
    p = Popen('ifconfig', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout
             
def parserIfconfig(stdout):
    groups = [i for i in stdout.split('\n\n') if i and not i.startswith('lo')]
    ifname = re.compile(r'^(wlan0)')       #(r'^(eth\d:?\d?)')
    macaddr = re.compile(r'.*HWaddr\s+([0-9a-fA-F:]{17})')
    ipaddr = re.compile(r'.*inet addr:+([\d.]{7,15})')
    result = []
    for group in groups:
        config_list = {}
        for line in group.split('\n'):
            m_ifname = ifname.match(line)
            m_macaddr = macaddr.match(line)
            m_ipaddr = ipaddr.match(line)
            if m_ifname:
                config_list['ifname'] = m_ifname.group(1)
            if m_macaddr:
                config_list['macaddr'] = m_macaddr.groups()[0]
            if m_macaddr:
                config_list['macaddr'] = m_macaddr.groups()[0]
            if m_ipaddr:
                config_list['ipaddr'] = m_ipaddr.groups()[0]
        result.append(config_list)
    return result

def getDMI():
    p = Popen('dmidecode', stdout=PIPE, shell=True)
    stdout, stderr = p.communicate()
    return stdout
        
def parserDMI(dmidata):
    pd = {}
    line_in = False
    for line in dmidata.split('\n'):
        if line.startswith('System Information'):
             line_in = True
             continue
        if line.startswith('\t') and line_in:
                 k,v = [i.strip() for i in line.split(':')]
                 pd[k] = v
        else:
            line_in = False
    return pd

def getMemTotal():
    cmd = "grep MemTotal /proc/meminfo"
    p = Popen(cmd, stdout = PIPE, shell = True)
    data = p.communicate()[0]
    mem_total = data.split()[1]
    return mem_total

def getCpu():
    cmd = "cat /proc/cpuinfo"
    p = Popen(cmd, stdout = PIPE, stderr = PIPE, shell = True)
    stdout, stderr = p.communicate()
    return stdout
     
def parserCpu(stdout):
    groups = [i for i in stdout.split('\n\n')]
    group = groups[-2]
    cpu_list = [ i for i in group.split('\n')]
    cpu_info = {}
    for x in cpu_list:
        k, v = [i.strip() for i in x.split(':')]
        cpu_info[k] = v
    return cpu_info

def postData(data):
    postdata = urllib.urlencode(data)
    req = urllib2.urlopen('http://192.168.0.111:8000/api/collect',postdata)
    req.read()
    return True

def main():
    data_info = {}
    """
    data_info = {'ipaddrs':'192.168.3.123','memory':16,'cpu_model':'Intel','cpu_num':4,'sn':'R9NBEZA','vendor':'LENOVO','product':'ThinkPad X220','osver':'Fedora 16 x86_64','hostname':'Sibiao Luo'}
    """
    ipinfo = parserIfconfig(getIfconfig())
    for x in ipinfo:
        if 'ifname' in x:
            data_info['ipaddrs'] = x['ipaddr']
    
    memtotal = int(round(int(getMemTotal())/1024.0/1024.0, 0))
    data_info['memory'] = memtotal
    
    cpuinfo = parserCpu(getCpu())
    data_info['cpu_num'] = int(cpuinfo['processor']) + 1
    data_info['cpu_model'] = cpuinfo['vendor_id']

    data_info['sn'] = parserDMI(getDMI())['Serial Number']
    data_info['vendor'] = parserDMI(getDMI())['Manufacturer']
    data_info['product'] = parserDMI(getDMI())['Version']
    
    os_version = [i for i in platform.linux_distribution()]
    os_version.append(platform.machine())
    os_ver = ''
    for x in os_version:
        os_ver += x
        os_ver = os_ver + ' '
    os_ver = os_ver.rstrip()
    data_info['osver'] = os_ver
    data_info['hostname'] = platform.uname()[1]

    return data_info

if __name__ == "__main__":
    result = main()
    print 'Get the hardwave and softwave infos from host:'
    print result
    print '----------------------------------------------------------'
    postData(result)
    print 'Post the hardwave and softwave infos to CMDB successfully!'

