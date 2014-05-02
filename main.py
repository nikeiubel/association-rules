import csv, sys, collections
from sys import stdout
from itertools import combinations, permutations
    
freq_itemsets = []                              #Keeps track of frequent itemsets
supportScores = collections.defaultdict(float)  #Keeps track of support scores for itemsets
rules = collections.defaultdict(float)          #Keeps track of rules and their confidence scores
freq_itemsets_dic = collections.defaultdict(float)  #Keeps track of support scores for only frequent itemsets

def main(filename, min_sup, min_conf):
    if min_sup < 0.0 or min_sup > 1.0 or min_conf < 0.0 or min_conf > 1.0:
        usage()
    else:
        with open(filename, 'rU') as f:
            rows = list(csv.reader(f))
            itemset = get_itemset(rows)                 
            a_priori(rows, itemset, min_sup)
            generate_rules(freq_itemsets, min_conf)
            for itemset in freq_itemsets:                               #Populates freq_itemsets_dic with scores
                freq_itemsets_dic[itemset] = supportScores[itemset]
            output = open('output.txt', 'w')
            output.write('==Frequent itemsets (min_sup=' + str(int(min_sup*100)) + '%)\n')
            for key, value in sorted(freq_itemsets_dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):     #Sorts freq_itemsets_dic by value
                if value > 0:
                    output.write('[' + str(key) + '], ' + str(value*100) + '%\n')
            output.write('\n==High-confidence association rules (min_conf=' + str(int(min_conf*100)) + '%)\n')  #Sorts rules by value
            for key, value in sorted(rules.iteritems(), key=lambda (k,v): (v,k), reverse=True):
                lefthand = key[:-1]
                righthand = key[-1]
                itemset = list(tuple(lefthand))
                itemset.append(righthand)
                sorted_items = sorted(itemset)
                sorted_tuple = tuple(sorted_items)
                support = supportScores[sorted_tuple]
                output.write('[' + str(lefthand) + '] => [' + str(righthand) + '] (Conf: ' + str(value*100) + '%, Supp: ' + str(support*100) + '%)\n')

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
    get_large_1_itemset(rows,itemset,min_sup)  # supportScores maps tuples of 1-itemsets into their support score
    k = 2
    lkminus1 = []               # initially k = 2 so this list will store L-1, i.e. the list of all large 1-itemsets
    for key in supportScores:   # reads supportScores, which currently holds large 1-itemsets plus scores, to get a list of all large 1-itemsets
        lkminus1.append(key)
    lk = []                     # needs to declare it outside of loop so its value can be returned at the end
    while lkminus1:
        lk = []
        Ck = a_priori_gen(lkminus1)
        for itemlist in Ck:
            item_support = get_item_support(itemlist,rows)
            if item_support >= min_sup:
                sorted_itemlist = sorted(itemlist)
                supportScores[tuple(sorted_itemlist)] = item_support
                lk.append(tuple(itemlist))
        lkminus1 = lk
        k += 1
    return lk

def get_large_1_itemset(rows, itemset, min_sup):  # returns a map of large 1-itemset into their support scores
    for item in itemset:
        itemlist = []
        itemlist.append(item)
        item_support = get_item_support(itemlist,rows)
        if item_support >= min_sup:
            sorted_itemlist = sorted(itemlist)
            supportScores[tuple(sorted_itemlist)] = item_support

def a_priori_gen(lkminus1):     #Generates candidate itemsets 
    Ck = []
    itemsets = set(lkminus1)
    for p, q in combinations(lkminus1, 2):  #Creates combinations of itemsets in L(k-1)
        k = len(p)
        if p[:k-1] == q[:k-1]:  #If all items in the two itemsets are equal except for the last item
            c = p[:k-1] + tuple([p[k-1], q[k-1]])   #Creates new candidate itemset
            Ck.append(c)
    for c in Ck:                                    #For all new candidate itemsets
        for subset in combinations(c,k):            #Checks to see if a subset of that itemset is not in itemsets
            if subset not in itemsets:
                Ck.remove(c)
                break
    for c in Ck:
        freq_itemsets.append(c)
    return Ck

def get_item_support(item,rows):
    count = 0
    no_rows = len(rows)-1
    for row in rows:
        if all(i in row for i in item):
            count += 1
    return float(count)/float(no_rows)

def calc_confidence(lefthand,righthand):
    itemset = list(lefthand + righthand)
    sorted_items = sorted(itemset)
    sorted_tuple = tuple(sorted_items)
    if supportScores[lefthand] > 0:
        return supportScores[sorted_tuple]/supportScores[lefthand]
    else:
        return 0

def generate_rules(large_itemset, min_conf):
    for itemset in freq_itemsets:
        for item in combinations(itemset,1):
            righthand = item
            t = list(itemset)
            t.remove(item[0])
            lefthand = tuple(t)
            confidence = calc_confidence(lefthand,righthand)
            if confidence >= min_conf:
                rules[lefthand + righthand] = confidence

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
