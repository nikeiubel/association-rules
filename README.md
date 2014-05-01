a. Your name and your partner's name;

Nikolas Iubel, nfi2103

Elaine Mao, ekm2133

b. A list of all the files that you are submitting;

// Elaine

c. A detailed description explaining: 

(a) which NYC Open Data data set(s) you used to generate the INTEGRATED-DATASET file; 

Data set comes from '311 Service Requests from 2010 to Present' NYC Open Data data set, available at: https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9


(b) what (high-level) procedure you used to map the original NYC Open Data data set(s) into your INTEGRATED-DATASET file;

We made use of the 'filter' tool made available at the NYC Open Data interface. The following filter was applied: 'Created Date' 'is between' '12/25/2013 12:00:00 AM' and '12/25/2013 11:59:59 PM'. In other words, this data set contains all 311 service requests made on Christmas day last year.

(c) what makes your choice of INTEGRATED-DATASET file interesting (in other words, justify your choice of NYC Open Data data set(s)). 

// Elaine 

d. A clear description of how to run your program (note that your project must compile/run under Linux in your CS account);

Run the program on the command line as follows: 

$ python main.py INTEGRATED-DATASET.csv min_sup min_conf

Example:
python main.py file.csv 0.3 0.4

e. A clear description of the internal design of your project; in particular, if you decided to implement variation(s) of the original a-priori algorithm (see above), you must explain precisely what variation(s) you have implemented and why.

f. The command line specification of an interesting sample run (i.e., a min_sup, min_conf combination that produces interesting results). Briefly explain why the results are interesting.

g. Any additional information that you consider significant.

