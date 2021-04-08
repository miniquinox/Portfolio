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
Max array size = 27648. 
Found in files:  ['sample.1', 'sample.2', 'sample.3', 'sample.4', 'sample.5', 'sample.6', 'sample.7', 'sample.8', 'sample.9', 'sample.10'], 
Offset: 3072.

Given 10 files, this would make 100 comparisons, but the program properly adjusted 
