#!/usr/bin/python

import sys
from subprocess import Popen, PIPE
from optparse import OptionParser

OK = 0
WARNING = 1
CRICITICAL = 2
UNKNOWN = 3

def opt():
    parser = OptionParser(usage="usage: %prog -w WARNING -c CRITICAL")
    parser.add_option("-c", default="100", action="store", dest="critical", type="string")
    parser.add_option("-w", default="200", action="store", dest="warning", type="string")
    return parser.parse_args()

"""
def getMemFree():
    cmd = "grep MemFree /proc/meminfo"
    p = Popen(cmd, stdout = PIPE, shell = True)
    data = p.communicate()[0]
    MemFree = data.split()[1]
    free_mem = int(MemFree)/1024
    return free_mem
"""

def getFreeMemory():
    with open('/proc/meminfo', 'r') as fd:
        for line in fd.readlines():
            if line.startswith('MemFree'):
                k, v, u = line.split()
                return int(v)*1024

def convertUnit(s):
    unit = {'t':2**40, 'g':2**30, 'm':2**20, 'k':2**10, 'b':2**0}
    s = s.lower()
    lastchar = s[-1]
    num = int(s[:-1])
    if lastchar in unit:
        return int(num) * unit[lastchar]
    else:
        return int(s)

def getConvert(data):
    if 2**10 > data >= 0:
        return '%d B' % data
    elif 2**20 > data >= 2**10:
        return '%d KB' % (data/(2**10))
    elif 2**30 > data >= 2**20:
        return '%d MB' % (data/(2**20))
    elif 2**40 > data >= 20**30:
        return '%d GB' % (data/(2**30))
    elif data >= 2**40: 
        return '%d TB' % (data/(2**40))
    else:
        return False

def main():
    opts, args = opt()
    w = convertUnit(opts.warning)
    c = convertUnit(opts.critical)
    data = getFreeMemory()
    free_mem = getConvert(data)
    if w >= free_mem > c: 
        print "WARNING, FreeMem: %s" % free_mem
        sys.exit(WARNING)
        #return WARNING
    elif free_mem <= c:
        print "CRICITICAL, FreeMem: %s" % free_mem
        sys.exit(CRICITICAL)
        #return CRICITICAL
    elif free_mem > w:
        print "OK, FreeMem: %s" % free_mem
        sys.exit(OK)
        #return OK
    else:
        print "UNKNOWN, FreeMem: %s" % free_mem
        sys.exit(UNKNOWN)
        #return UNKNOWN

if __name__ == "__main__":
    #free_mem = getMemFree()
    #print 'MemFree: %dMB' % free_mem
    main()

