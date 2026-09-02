## Efficiency Analysis
- 08/31/2026

### Analysis of Algorithms 
- I. Random Access Machine (RAM)

Each **basic** instruction takes a constant amount of time

• arithmetic: add, subtract, multiply, divide, remainder, floor, ceiling, shift
left/shift right
• data movement: load, store, copy

**Question** : What is the fastest algorithm to use? 

L = [ ... ] ; # n =60
sort_c[L] #note the time of this executing: 3 s
## ----
sort[L] #note the time of this executing: 0.0003 s 

- The answer is that this is undecidable 

- Note that loops and subroutine calls are not basic operations. They depend upon the size of the data and the contents of a subroutine
- - "Sort" is not a single step operation
 
  ***Review***
  Sort:
L[6,5,0,1,7] # we will assign the first element; min_val = 6 ; we have to check through all the elements
#Note that we iterate through all the elements to see which is smaller
----
## Example 1 (non-efficient): 
def min_v1(S):
min_val = S[0] # 1
for x in S: # for loop runs n times
if x < min_val: # n comparisons
min_val = x # <=n
else:
-min_val = min_val # <=n wasted-
return min_val # 1
  ----
##Example 2(efficient): 
def min_v2(S):
min_val = S[0] # 1
for x in S: # for loop runs n times
if x < min_val: # n comparisons
min_val = x # ≤ n
return min_val # 1

### Functions for Measuring Resources
An algorithm is efficient when it consumes few resources

• Time: measured in units of seconds, CPU instructions, or generic
steps;
• Space: measured in units of bits, bytes, gigabytes, or generic
words;
• input/output bandwidth (I/O): measured in units of bytes or
blocks;
• Cache: measured in units of integers; or
• Energy: measured in units of kilowatt-hours.

----
Measuring the quality of an algorithm

• Quality of an algorithm is measured in terms of the resources
it consumes when it is executed on a computer

• Of interest in this class are the execution time and the memory
need

– Shorter the execution time, better the quality of the algorithm – ***time
complexity***
– Smaller the amount of memory needed for execution, better the
quality of the algorithm – space complexity

*less memory shorter time 
----

  The second trial of the algorithm will be “slightly” faster.
• No wasted assignment.
Time complexity function for the number of statements taken by min_v1 will be

## Optimization 

def min_v1(S):
min_val = S[0] # 1
for x in S: # for loop runs n times
if x < min_val: # n comparisons
min_val = x # <=n
else:
min_val = min_val # <=n wasted
return min_val # 1


*T1(n) - step count*
T1(n)=n(comparisons)+n(useful or wasted assignments)+2=2n+2
def min_v2(S):
min_val = S[0] # 1
for x in S: # for loop runs n times
if x < min_val: # n comparisons
min_val = x # ≤ n
return min_val # 1

Worst case: T2(n)=2n+2
Best case: T2(n)=n+2 (note: S[0] is already the minimum element in S)

----

## Counting Operations: 
• Step count (or running time):
• The sum of steps (or running times) for each executable
statement

----
## General Rules for Computing the S.C.

• Simple operations take (1) unit of time:
– addition, multiplication, assignment, comparison, read/write a value
• Consecutive statements add up.
• If/Else: for the fragment

If (condition)
S1
else
S2

• The s.c. is equal to the number of steps to evaluate the condition
plus the maximum of the s.c. of S1 and S2. i.e. max ( S.C. of if, else)

• For loops: The s.c. of a for-loop is at most the s.c. of the statements
inside the for-loop times the number of iterations.
)
• Nested loops are analyzed inside out.

* S.C. = (cost of condition) + max(S.C. of if-branch, S.C. of else-branch

## Obtaining Big Oh efficiency from Step Counts
- Example: See Ipad:

----
## Efficiency Analysis of an Algorithm

• Analysis is the key to understanding algorithm
– How to predict an algorithm’s performance
– How well an algorithm scales up
– How to compare different algorithms for a problem

Two evidence-based approaches:
1. Experimental analysis: using the scientific method of hypothesis,
experiment, and empirical data analysis; and

2. Mathematical analysis: using the mathematical method of
modeling, lemma, and proof

----

## Experimental Analysis

• Steps:
– Implement algorithm in a given programming language
– Measure runtime with several inputs
– Infer running time from the inputs
• Pros:
– No math, straightforward method
• Cons:
– Not always reliable, heavily dependent on
• the sample inputs
• programming language and environment
- 
----
Mathematical Analysis

• Uses math to estimate the running time of an
algorithm
– Dependent of the activities/steps counts/input size

• Pros:
– formal, rigorous
– no need to implement algorithms
– machine-independent

• Cons:
– math knowledge
----

## Analysis by Case Complexities 

Best case complexity: minimum number of steps.
• Eg, sorting a sequence of sorted or almost-sorted numbers using insertion-sort

• Worst-case complexity : maximum number of steps.
• Eg, sorting a sequence of fully unsorted numbers using insertion-sort

• Average case complexity : the input is chosen at random, the average
number of steps.

• The worst-case running time of an algorithm is an upper bound on the running time
for any input.

----
Easier Method:

Upper and Lower Bounds

• It is easier to talk about upper and lower bounds of the
function.
• Asymptotic notation (O, Ω, Θ) to practically deal with
complexity functions.
