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
\# cd pycmdb

\# python post_hardwave_and_softwave_infos_to_cmdb.py     

