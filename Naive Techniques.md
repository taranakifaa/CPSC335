Naïve Pattern

• A naïve algorithm pattern is not based on any of the
formal and structured patterns
– It is usually an adhoc approach

• Some real-world software development problems can
be solved efficiently by naive algorithms
– Contains essential building block of practical software
development

• If a simple algorithm is both correct and efficient
enough, it should be chosen over more complicated
methods.

**Sequential Search**

Let's say we have: 
```python
U = [3,9,2,4,7]
for x in U 
if x == 4
return x 
```
time complexity is n. 

Sequential search = finding an element of a list with
a particular property

– It checks each element in sequence until the desired
element is found, or the list is exhausted.
– Also known as linear search

**Sequential Search**

• A straightforward approach is to use a loop to check
each element of S for the desired property.
– If a match is found, the element is returned, and the loop is
stopped

• It runs in O(n) time, provided that each element may be tested in
in O(1) time

<img width="915" height="625" alt="image" src="https://github.com/user-attachments/assets/3647a0f1-50e0-4068-815d-01edeef16d15" />


Say I want to check: 

```python
U = [3,9,2,4,7]
for x in U 
if x == 4 <-- this statement
return x 
```
* note that the return x is the "+ 1" 
<img width="360" height="153" alt="image" src="https://github.com/user-attachments/assets/bb1fce5d-c317-449c-a7de-b34e91a1ec5f" />

Midterm:

What is the difference between sequential optimization (search all) vs sequential search (search until found).

Sequential Optimization

• Method: make a guess about which element is best, and
initialize best with any element of S: Then we loop
through all the elements of S;
– if a better element x is found, x becomes best .
```python
def sequential_optimization(S):
best = S[0]
for element in S:
if <element IS BETTER THAN best>:
best = element
return best

```
Note that return best is at the end because we are aiming to find the best element, (This is after we check everything) 

***The Sorting Problem***
Selection Sort --> pure selection
|-> in place

*There is a naive solution (This is a potential non-supported solution) 

EX: Say we want to sort this: U = [3,9,2,4,7]

For pure selection sort, you will have one for loop

**The Sorting Problem**

sorting problem
input: a list U of n comparable elements
output: a list S containing the elements of U in non-decreasing order

• Sorting is a well-studied problem in computer science, for both
theoretical and practical reasons.

• A sorting algorithm can be used to solve many different problems that
do not resemble the original sorting problem.

• The lower bound for sorting is a landmark result that lays the
foundation for lower bounds of other problems.

Selection Sort

• Sorts an array by repeatedly finding the minimum
element ( in non-decreasing order) from unsorted part
– and append it to the beginning of the array

• It maintains two subarrays in a given array.
– 1) The subarray which is already sorted.
– 2) Remaining subarray which is unsorted.

• The smallest element is selected from the unsorted
array and swapped with the leftmost element,
– It then becomes a part of the sorted array

Algorithm pure_selection_sort:
```python
def pure_selection_sort(L):
S = [ ]
while L is not empty:
x = <FIND THE SMALLEST ELEMENT IN L> // finding step
<REMOVE x FROM L> // removal step
< APPEND x to S> // appending step
return S
```
Three steps: finding, removal, and appending steps, need to be
detailed

```python
def selection_sort(U):
S = []
while U is not empty:
# find the least unsorted element
least_index = 0
for i in range(1, len(U)):
if U[i] < U[least_index]
least_index = i
# remove least from U
swap(U[least_index], U[-1]) # move min to end
least = U.pop() #remove and capture that min
# add least to S
S.add_back(U[least_index])
return S
```
The worst case time complexity of selection_sort is O(n^2)
Note: Loop overhead per iteration is ignored; we only count key operations
STEPS for inner loop: 

S = 1 + (n- 1)(2) +2 +1 = 2n + 2

Inner loop: 

n
summation k = (n+1)n/2 
k = 1

n
summation k
k-1 


QUIZ: 

l.
PROVE BY INDUCTION

YOU NEED TO KNOW HOW TO GET C AND N_0 

HOW TO USE A LIMITS AND ASUMPTOTIC NOTATIONS 

HOW T SOLVE FOR LIMITS
CASE 3 


AMORTIZED ANALUSIS 

A TECHNIQUE USED TO ANALYZE TIME COMPLEXITY 

LOOK AT UNIVERSITY CLASSROOM EXAMPLE: 

WHAT IS THE COST AND WHAT IS THE PERIOD 

DATA STRUCTURES

WHAT IS DICTIONARY --> KEY AND DATA  

BASIC CONCEPTS ON LINKED LISTS THE DIFFERENCE BETWEEN ARRAY AND LINKED LIST
WHAT IS STACK LIFO 

WHAT IS QUEUE FIFO 

WHAT IS PRIORITY QUEUE DEFINE THE ARRAY USING THE P

BASIC CONCEPTS ON HEAPS 

WHAT IS THE TIME COMPLEXITY WHEN i WANT TO INSERT INTO A BINARY HEAP

YOU WILL SEE ALOT OF QUESTIONS ON GRAPHS 

WHAT IS THE DEGREE/ VERTICIES OF THIS GRAPH

WHAT IS THE COMPLETE GRAPH

WRITE DOWN THE ADJACENCY MATIX BASED ON THIS GRAPH


