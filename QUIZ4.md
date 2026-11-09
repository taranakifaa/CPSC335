quiz tdoay
CPSC 335 — Divide & Conquer Quiz Study Guide
Modules 11–12 • Based on your uploaded lecture study guide • Quiz review

I reorganized your notes into a cleaner Markdown study guide with simple comparisons, worked examples, Master Theorem shortcuts, and common quiz traps.

1. Divide and Conquer (D&C)
Divide and Conquer is an algorithm strategy where you break a large problem into smaller problems, solve them, and combine the answers.

Step

Meaning

Example: Merge Sort

Divide

Split into smaller problems

Split array in half

Conquer

Solve smaller problems recursively

Sort each half

Combine

Put the answers together

Merge sorted halves

Base case

Condition that stops recursion

Array has 0 or 1 element

Remember: Divide → Conquer → Combine, with the base case checked first.

Recursion depth vs. runtime
Reduction

Depth

Subtract 1 each time

O
(
n
)
O(n)

Divide by 2 each time

O
(
log
⁡
n
)
O(logn)

Divide by 4 each time

O
(
log
⁡
4
n
)
O(log 
4
​
 n)

Quiz trap: Just because you divide by 2 does NOT mean the algorithm runs in 
O
(
log
⁡
n
)
O(logn). You must also count how many recursive calls execute.

2. Compare the main algorithms
Algorithm

Recursive calls

Work outside recursion

Total time

Minimum selection (ranges)

2

O
(
1
)
O(1)

O
(
n
)
O(n)

Summation (loop)

0

One pass

O
(
n
)
O(n)

Summation (copied halves)

2

O
(
n
)
O(n)

O
(
n
log
⁡
n
)
O(nlogn)

Summation (ranges)

2

O
(
1
)
O(1)

O
(
n
)
O(n)

Merge operation

0

O
(
n
)
O(n)

O
(
n
)
O(n)

Merge Sort

2

O
(
n
)
O(n)

O
(
n
log
⁡
n
)
O(nlogn)

Binary Search

1

O
(
1
)
O(1)

O
(
log
⁡
n
)
O(logn)

Binary Search vs. Merge Sort
Binary Search


Discards one half

Only 1 recursive call

Requires sorted input

T
(
n
)
=
T
(
n
/
2
)
+
1
T(n)=T(n/2)+1

O
(
log
⁡
n
)
O(logn)

Merge Sort


Processes both halves

2 recursive calls

Works on unsorted input

T
(
n
)
=
2
T
(
n
/
2
)
+
n
T(n)=2T(n/2)+n

O
(
n
log
⁡
n
)
O(nlogn)

3. Master Theorem — most important section
The general recurrence is:

T
(
n
)
=
r
T
(
n
/
d
)
+
c
(
n
)
T(n)=rT(n/d)+c(n)
​
 
Symbol

Meaning

Example

r
r

Number of recursive calls

2 calls → 
r
=
2
r=2

d
d

Factor input shrinks by

n
/
2
n/2 → 
d
=
2
d=2

c
(
n
)
c(n)

Work outside recursion

Copying or merging

k
k

Exponent of 
n
n in 
c
(
n
)
c(n)

n
2
n 
2
  → 
k
=
2
k=2

The 3 cases — using your professor's numbering
Case 1: 
r
<
d
k
r<d 
k
 

O
(
n
k
)
O(n 
k
 )

Work near the root dominates.
Case 2: 
r
=
d
k
r=d 
k
 

O
(
n
k
log
⁡
n
)
O(n 
k
 logn)

Work is balanced across levels.
Case 3: 
r
>
d
k
r>d 
k
 

O
(
n
log
⁡
d
r
)
O(n 
log 
d
​
 r
 )

Work near the leaves dominates.
These bounds are also tight 
Θ
Θ bounds for the polynomial recurrence form covered in your notes.

How to solve any standard Master Theorem question
Find 
r
r, 
d
d, and 
k
k.

Calculate 
d
k
d 
k
 .

Compare 
r
r against 
d
k
d 
k
 .

Choose Case 1, 2, or 3.

Write the final complexity.

Worked comparisons
Recurrence

Comparison

Case

Answer

T
(
n
/
2
)
+
n
2
T(n/2)+n 
2
 

1
<
4
1<4

1

Θ
(
n
2
)
Θ(n 
2
 )

2
T
(
n
/
2
)
+
n
2T(n/2)+n

2
=
2
2=2

2

Θ
(
n
log
⁡
n
)
Θ(nlogn)

4
T
(
n
/
2
)
+
n
4T(n/2)+n

4
>
2
4>2

3

Θ
(
n
2
)
Θ(n 
2
 )

2
T
(
n
/
2
)
+
1
2T(n/2)+1

2
>
1
2>1

3

Θ
(
n
)
Θ(n)

T
(
n
/
2
)
+
1
T(n/2)+1

1
=
1
1=1

2

Θ
(
log
⁡
n
)
Θ(logn)

2
T
(
n
/
4
)
+
n
2T(n/4)+ 
n
​
 

2
=
2
2=2

2

Θ
(
n
log
⁡
n
)
Θ( 
n
​
 logn)

Quick tip: 
O
(
1
)
O(1) means 
k
=
0
k=0, 
O
(
n
)
O(n) means 
k
=
1
k=1, and 
O
(
n
)
O( 
n
​
 ) means 
k
=
1
/
2
k=1/2.
