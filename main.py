import csv, sys
#import json, sys, string, urllib, urllib2, re, collections
from sys import stdout

def main(filename, min_sup, min_conf):
    if min_sup < 0.0 or min_sup > 1.0 or min_conf < 0.0 or min_conf > 1.0:
        usage()
    else:
        with open(filename, 'rU') as f:
            rows = list(csv.reader(f))
            itemset = get_itemset(rows)
            freq_itemsets = a_priori(rows, itemset, min_sup)
            #print itemset

def get_itemset(rows):
    itemlist = []
    i = 0
    j = 0
    for row in rows:
        if i != 0:  # prevents top row (i.e. names of columns) from being added to itemset
            for attr in row:
                if j != 0 and attr:   # prevents TIDs and empty cells from being added to itemset
                    itemlist.append(attr)
                j += 1
        i += 1
        j = 0
    return set(itemlist)

def a_priori(rows, itemset, min_sup):
    supportScores = get_large_1_itemset(rows,itemset,min_sup)  # supportScores maps 1-itemsets into their support score
    k = 2
    lkminus1 = []              # initially k = 2 so this list will store L-1, i.e. the list of all large 1-itemsets
    for key in supportScores:  # reads supportScores, which currently holds large 1-itemsets plus scores, to get a list of all large 1-itemsets
        lkminus1.append(key)
    print lkminus1
    lk = []
    while lkminus1:
        lk = []
        Ck = a_priori_gen(lkminus1)
        for itemlist in Ck:
            item_support = get_item_support(itemlist,rows)
            if item_support >= min_sup:
                supportScores[itemlist] = item_support
                lk.append(itemlist)
        lkminus1 = lk
        k += 1
    return lk

def get_large_1_itemset(rows, itemset, min_sup):  # returns a map of large 1-itemset into their support scores
    l1 = {}
    for item in itemset:
        itemlist = []
        itemlist.append(item)
        item_support = get_item_support(itemlist,rows)
        if item_support >= min_sup:
            l1[itemlist] = item_support
    return l1

def a_priori_gen(lkminus1):
    

def get_item_support(item,rows):
    count = 0
    no_rows = len(rows)
    for row in rows:
        if all(i in row for i in item):
            count += 1
    return float(count)/float(no_rows)

def usage():
    sys.stderr.write("""
    Usage: 
        python main.py INTEGRATED-DATASET.csv min_sup min_conf \n
    Values of min_sup and min_conf must be at least 0.0 and at most 1.0
        \n""")

if __name__ == "__main__": 
    if len(sys.argv) == 4:
        main(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
    else:
        usage()
        sys.exit(1)
