from models import Host, Ipaddr, HostGroup
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

class HostGroupAdmin(admin.ModelAdmin):
    list_display = ['name',]
 
admin.site.register(Host, HostAdmin)
admin.site.register(Ipaddr, IpaddrAdmin)
admin.site.register(HostGroup, HostGroupAdmin)

