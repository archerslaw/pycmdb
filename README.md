#### Python for Configuration Management Database:
Step by step guide to building a configuration management database(CMDB) using python and django, CMDB is a repository of information related to all the components of an information system. Then we can use the post_hardwave_and_softwave_infos_to_cmdb.py script to get the hardwave & softwave info from host and post the info data to CMDB automatically.

#### How to get the Django Sources:
https://www.djangoproject.com/download/

\# tar xzvf Django-1.5.1.tar.gz

\# cd Django-1.5.1

\# python setup.py install

#### How to start it:
\# cd pycmdb

\# python manager runserver $host\_ip:$port

#### How to post the data to CMDB:
\# python post_hardwave_and_softwave_infos_to_cmdb.py     
Get the hardwave and softwave infos from host:            
\{\'product\'\: \'ThinkPad X220\', \'vendor\': \'LENOVO\', \'cpu\_num\': 4, \'ipaddrs\': \'10.66.65.102\', \'hostname\': \'dhcp-65-102.nay.redhat.com\', \'cpu\_model\': \'GenuineIntel\', \'osver\': \'Fedora 16 Verne x86\_64\', \'sn\': \'R9NBEZA\', \'memory\': 4\}
----------------------------------------------------------
Post the hardwave and softwave infos to CMDB successfully!

