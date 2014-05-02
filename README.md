a. Your name and your partner's name;

Nikolas Iubel, nfi2103

Elaine Mao, ekm2133

b. A list of all the files that you are submitting;

main.py
INTEGRATED-DATASET.csv
Makefile
README.md
example-run.txt

c. A detailed description explaining: 

(a) which NYC Open Data data set(s) you used to generate the INTEGRATED-DATASET file; 

Data set comes from '311 Service Requests from 2010 to Present' NYC Open Data data set, available at: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9


(b) what (high-level) procedure you used to map the original NYC Open Data data set(s) into your INTEGRATED-DATASET file;

We made use of the 'filter' tool made available at the NYC Open Data interface. The following filter was applied: 'Created Date' 'is between' '12/25/2013 12:00:00 AM' and '12/25/2013 11:59:59 PM'. In other words, this data set contains all 311 service requests made on Christmas day last year.

(c) what makes your choice of INTEGRATED-DATASET file interesting (in other words, justify your choice of NYC Open Data data set(s)). 

This dataset allows us to view all 311 service requests made in every borough of New York in a 24-hour time period. The 24-hour time period we have chosen coincides with a very demanding time of year for New York City. Holiday tourism and harsh winter weather both take a toll on the city's resources and infrastructure, making 311 calls very frequent during this period. Our dataset contains information on type of complaint, location of complaint, agency responsible, etc. The most interesting question this allows us to answer is: what types of problems are the most common in different areas of New York? Do certain boroughs have (or report) more problems than others? 

We picked this data set in the hope that association rules would shed light on patterns of service requests in New York City, such as what boroughs see a given type of request more often. For instance, we found that heating complaints are more prevalent in the Bronx, which is incidentally a low-income borough.

d. A clear description of how to run your program (note that your project must compile/run under Linux in your CS account);

1) Makefile:

Run program with Makefile in the following manner:

    make FILENAME=[csv_file] MIN_SUP=[min_sup] MIN_CONF=[min_conf]

 Example:
 make FILENAME=INTEGRATED-DATASET.csv MIN_SUP=0.1 MIN_CONF=0.8

2) Terminal:

Run the program on the command line as follows: 

$ python main.py INTEGRATED-DATASET.csv min_sup min_conf

Example:
python main.py INTEGRATED-DATASET.csv 0.1 0.8

e. A clear description of the internal design of your project; in particular, if you decided to implement variation(s) of the original a-priori algorithm (see above), you must explain precisely what variation(s) you have implemented and why.

The code is a straightforward implementation of the a_priori algorithm as outlined in Figure 1 of section 2.1 of Agarwal's paper on association rules. We first read in the csv file and loop through the rows to generate an itemset (set of all items seen in the rows). We then call the a-priori algorithm, which is implemented as a separate function which, in turn, calls a-priori-gen to join instances of Lk with themselves and eventually returns a list of frequent itemsets.

To generate the rules, we simply take the frequent itemsets (generated by the a-priori algorithm) and for each itemset, calculate all possible rules of the specified format (i.e. one item on the right-hand side, at least one item on the left-hand side). If the rule has confidence greater than min-conf, the rule is added to the rules dictionary. 

f. The command line specification of an interesting sample run (i.e., a min_sup, min_conf combination that produces interesting results). Briefly explain why the results are interesting.

$ python main.py INTEGRATED-DATASET.csv 0.1 0.8

This combination produces interesting results because the low min_sup prevents too many items from being filtered out of the analysis, while the high min_conf picks out only the rules which are very strongly supported. This sample run produces some interesting insights about heating complaints in New York. They occur most frequently in The Bronx, followed by Brooklyn and then Manhattan. Heating complaints were also the most common complaints overall, and they occurred in residential buildings 100% of the time. This is interesting because it means that no non-residential buildings (e.g. commercial buildings) complained of heating-related problems on Christmas Day. 


