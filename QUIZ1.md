## Quiz is on (9/9)
## Presentation (9/18)

## QUIZ REVIEW

* create html file for google doc

## Asymptotic Notations

### Mathematical notations of an efficiency class of an algorithm
• f(n) ∈ O(g(n)) implies that C x g(n) is an upper bound of f(n)

• f(n) ∈ Ω(g(n)) implies that C x g(n) is a lower bound of f(n)

• f(n) ∈ Θ(g(n)) implies that C1

x g(n) is an upper bound of f(n)

and C2

x g(n) is a lower bound of f(n)

• C, C1, and C2 are positive constants, and there exist a positive
n > n0

for which these relationships hold

*don't remember the notations but remember the figures 

* Note for Theta represents the tight bound

* Note you want to know how fast you want your program to run  (f(n) represents that factor)
[paste here] 


## Categorizing Functions 

- Big Oh can be used to  categorize functions

- Some simplifying assumptions are made when analysis the running time of an algorithm


Categorizing Functions

• An algorithm A is more efficient than another algorithm
B if the r.t of A has a lower order of growth.
• Examples: log(n), n, n^2, n^2log(n), n^3, 2^n, n^n 

– O(n) is the set of all functions that are equivalent to f(n) = n for the purposes
of measuring algorithmic complexity;
– O(n^2) is the set of all functions that are equivalent to f(n) = n2

for the purposes of measuring algorithmic complexity;

For example, the statements:
– 2n + 3 is O(n) and 5n is O(n); places 2n + 3 and 5n in the same category
– Both functions are less than or equal to g(n) = n, up to a constant factor, for large
values of n

---

True or False

1. True
2. True
3. True
4. True ( n^2 * n^2 )
5. True
6. no (n^6 is greater than n^5) False is my guess
7. Yes because it is within BOUND

---

## Step Counts:

• A single 'step' in our analysis might represent a
simple operation (like adding two numbers) or a
more complex one (like calculating a square root).

For example, the entire statement:
• return a+b+b*c+(a+b-c)/(a+b)+4
– can be regarded as a single step if its execution time is
independent of the problem size.

• We may also count a statement such as x = y; as a
single step

* The quiz will most likely consist of

* Time Step:

* while loop
* i = n + --> +1
* condition: --> so when I is less than + 4 --> log_2(n) 

i = i/2 --> n/2^k = 1 
* 
* k is number of runs(passes) 
   
