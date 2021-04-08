# Eluvio Core Software Engineering - Challenge

The program "script.py" is written in Python3 and it follows the following criteria: 
- Given a large number of binary files, the program finds the longest strand of bytes
  that is identical between two or more files. I will be using the test set in this 
  directory.
  
### The program displays the following outputs:
- The length of the strand
- The file names where the largest strand appears
- The offset where the strand appears in each file

### Given the 10 test files that were posted by Eluvio, these were the results:
Max array size = 27648   
Found in files:  ['sample.1', 'sample.2', 'sample.3', 'sample.4', 'sample.5', 'sample.6', 'sample.7', 'sample.8', 'sample.9', 'sample.10']   
Offset: 3072 (first file in which is found) 

The program does the following:
Loops through all files, extracts the information and puts it into an array. 

Given 10 files, this would make 100 comparisons, but the program is properly adjusted 
to take care of duplicate work by skipping comparisons already made. For example, 
After comparing sample.1 and sample.2, it will skip sample.2 and sample.1 comparison,
leaving 45 total comparisons.

## The script can run with no need to install additional libraries. Here is the performance:
n = time to parse all info from files to an array  
m = number of files  
v = length of all files   

n + (m*log(m) * v(logv))  

v is neglected since it is constant (Only ran 1 time), so final performance is:  
### (m*log(m) * v(logv))
