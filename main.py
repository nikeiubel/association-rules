import json, sys, string, urllib, urllib2, re, collections
from sys import stdout

def main(filename, min_sup, min_conf):
    
        else:
            usage()

def usage():
    sys.stderr.write("""
    Usage: 
        python main.py INTEGRATED-DATASET.csv min_sup min_conf
        \n""")

if __name__ == "__main__": 
    if len(sys.argv) == 4:
        main(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        usage()
        sys.exit(1)
