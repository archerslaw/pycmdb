#!/usr/bin/python
import urllib,urllib2
req = urllib2.urlopen('http://127.0.0.1:8000/api/collect')
req.read()
print 'Nothing to post.'
data = {'vendor':'LENOVO','product':'ThinkPad X220','osver':'Fedora 16 x86_64','memory':16,'cpu_model':'Intel','cpu_num':4,'sn':'R9NBEZA','ipaddrs':'192.168.3.123','hostname':'Sibiao Luo'}
postdata = urllib.urlencode(data)
req = urllib2.urlopen('http://127.0.0.1:8000/api/collect',postdata)
req.read()
print 'Post data successfully.'
