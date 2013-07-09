from models import Host, Ipaddr
from django.contrib import admin

class HostAdmin(admin.ModelAdmin):
    list_display = ['vendor',
            'product',
            'osver',
            'cpu_model',
            'cpu_num',
            'sn',
            'memory',
            'hostname'
            ]

class IpaddrAdmin(admin.ModelAdmin):
    list_display = ['ipaddr', 'host']

admin.site.register(Host, HostAdmin)
admin.site.register(Ipaddr, IpaddrAdmin)

