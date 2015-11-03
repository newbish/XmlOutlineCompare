__author__ = 'Keith'

import sys, getopt
from pyxmldiff import xmldiff

def main(argv):
    source = ''
    target = ''
    try:
        opts, args = getopt.getopt(argv, "hs:t:", ["source=", "target="])
    except getopt.GetoptError:
        display_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            display_help()
            sys.exit()
        elif opt in ('-t', '--target'):
            target = arg
        elif opt in ('-s', '--source'):
            source = arg
    if (len(source) == 0 or len(target) == 0):
        display_help()
        sys.exit(2)
    compare(source, target)


def compare(sf, tf):
    with open(sf, 'r') as s:
        with open(tf, 'r') as t:
            source = xmldiff.fromstring(s.read())
            target = xmldiff.fromstring(t.read())
            xmldiff.xmlDiff(source, target)


def display_help():
    print '''EPM Outline Compare
Usage: python compare.py -s <source xml file> -t <target xml file>
 -s, --source   Source XML file (source.xml)
 -t, --target   Target XML file (target.xml)

Flags:
 -h             Help
'''

if __name__ == '__main__':
    main(sys.argv[1:])