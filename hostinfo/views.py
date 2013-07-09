# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Host, Ipaddr

def collect(request):
    req = request
    if req.POST:
        vendor = req.POST.get('vendor')
        product = req.POST.get('product')
        cpu_model = req.POST.get('cpu_model')
        cpu_num = req.POST.get('cpu_num')
        memory = req.POST.get('memory')
        sn = req.POST.get('sn')
        osver = req.POST.get('osver')
        hostname = req.POST.get('hostname')
        ipaddrs = req.POST.get('ipaddrs')
        host = Host()
        host.hostname = hostname
        host.product = product
        host.cpu_num = int(cpu_num)
        host.cpu_model = cpu_model
        host.memory = int(memory)
        host.sn = sn
        host.osver = osver
        host.vendor = vendor
        host.save()
        for ip in ipaddrs.split(';'):
            o_ip = Ipaddr()
            o_ip.ipaddr = ip
            o_ip.host = host
            o_ip.save()
        return HttpResponse("post data successfully!")
    else:
        return HttpResponse("no any post data!")

