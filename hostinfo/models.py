from django.db import models

# Create your models here.

class Host(models.Model):
    """store host infomation"""
    hostname = models.CharField(max_length = 40)
    osver = models.CharField(max_length = 40)
    vendor = models.CharField(max_length = 40)
    product = models.CharField(max_length = 40)
    cpu_model = models.CharField(max_length = 40)
    cpu_num = models.IntegerField(max_length = 4)
    memory = models.IntegerField(max_length = 8)
    sn = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.hostname 
    """
    def __init__(self):
        super(Host, self).__init__()"""

class Ipaddr(models.Model):
    ipaddr = models.IPAddressField()
    host = models.ForeignKey('Host')
    """
    def __init__(self):
        super(Ipaddr, self).__init__()"""

class HostGroup(models.Model):
    name = models.CharField(max_length = 30)
    members = models.ManyToManyField(Host)

