# Algorithms Midterm Study Notes

## 1. Naïve Algorithm Pattern

A **naïve algorithm** is a simple, straightforward approach to solving a problem.

* It is not based on a formal or highly structured algorithmic pattern.
* It is usually an **ad hoc** approach.
* Naïve algorithms can still solve many real-world problems efficiently.
* If a simple algorithm is **correct** and **efficient enough**, it should usually be preferred over a more complicated solution.

**Main idea:**

> Start with the simplest reasonable solution before introducing unnecessary complexity.

---

# 2. Sequential Search / Linear Search

### Definition

**Sequential search** finds an element in a list that has a particular desired property.

It checks elements **one at a time, in order**, until:

1. The desired element is found, OR
2. The entire list has been searched.

Sequential search is also called **linear search**.

### Example

```python
U = [3, 9, 2, 4, 7]

for x in U:
    if x == 4:
        return x
```

The algorithm checks:

```text
3 → not 4
9 → not 4
2 → not 4
4 → FOUND
```

### Time Complexity

If checking one element takes:

$$
O(1)
$$

and there are potentially \(n\) elements to check:

$$
T(n) = O(n)
$$

### Important Detail

```python
if x == 4:
```

is the main comparison being performed repeatedly.

The:

```python
return x
```

is an additional constant operation.

So when performing a detailed operation count, the `return` can contribute a **+1**.

---

# 3. Sequential Search vs. Sequential Optimization

**IMPORTANT MIDTERM CONCEPT**

### Sequential Search

**Goal:** Find an element satisfying a property.

```python
for x in S:
    if x == target:
        return x
```

The algorithm can **stop early** once the desired element is found.

Example:

```text
[3, 9, 2, 4, 7]
          ↑
        Found!
```

There is no reason to check `7` after finding `4`.

---

### Sequential Optimization

**Goal:** Find the **best** element.

Examples:

* Minimum
* Maximum
* Cheapest
* Largest
* Highest priority

```python
def sequential_optimization(S):
    best = S[0]

    for element in S:
        if element IS BETTER THAN best:
            best = element

    return best
```

Unlike sequential search, sequential optimization normally must examine **every element**.

Why?

Suppose:

```text
[3, 9, 2, 4, 7]
```

If we are looking for the minimum, finding `3` does not mean we can stop.

We could later find:

```text
2
```

Therefore:

```python
return best
```

comes **after the loop**.

### Key Difference

| Sequential Search               | Sequential Optimization    |
| ------------------------------- | -------------------------- |
| Search until something is found | Search all elements        |
| Can stop early                  | Normally cannot stop early |
| Looks for a property/target     | Looks for the best element |
| Example: find `4`               | Example: find minimum      |
| Worst case: \(O(n)\)            | \(O(n)\)                   |

---

# 4. The Sorting Problem

### Input

A list \(U\) containing \(n\) comparable elements.

Example:

```python
U = [3, 9, 2, 4, 7]
```

### Output

A list \(S\) containing the elements of \(U\) in **non-decreasing order**.

```python
S = [2, 3, 4, 7, 9]
```

### Why Sorting Matters

Sorting is one of the fundamental problems in computer science.

Sorting algorithms can also be used as building blocks for solving other problems.

The theoretical **lower bound for comparison-based sorting** is an important result in algorithm analysis.

---

# 5. Selection Sort

Selection sort repeatedly finds the **smallest element** in the unsorted portion of the list.

It then moves that element into the sorted portion.

Example:

```text
[3, 9, 2, 4, 7]

Find minimum → 2

[2 | 9, 3, 4, 7]

Find minimum → 3

[2, 3 | 9, 4, 7]

Find minimum → 4

[2, 3, 4 | 9, 7]

Find minimum → 7

[2, 3, 4, 7 | 9]
```

The array can therefore be viewed as:

```text
| SORTED | UNSORTED |
```

The sorted section grows while the unsorted section shrinks.

---

# 6. Pure Selection Sort

**Pure selection sort** creates a separate output list.

General algorithm:

```python
def pure_selection_sort(L):
    S = []

    while L is not empty:

        x = FIND THE SMALLEST ELEMENT IN L

        REMOVE x FROM L

        APPEND x TO S

    return S
```

### Three Important Steps

You should know these three operations:

1. **Finding step**

   * Find the smallest remaining element.

2. **Removal step**

   * Remove the smallest element from the unsorted list.

3. **Appending step**

   * Add the element to the sorted list.

Example:

```text
L = [3, 9, 2, 4, 7]
S = []

Find 2
L = [3, 9, 4, 7]
S = [2]

Find 3
L = [9, 4, 7]
S = [2, 3]

Find 4
L = [9, 7]
S = [2, 3, 4]

...
```

---

# 7. Selection Sort Pseudocode

A selection-style implementation may look like:

```python
def selection_sort(U):
    S = []

    while U is not empty:

        # Find the least unsorted element
        least_index = 0

        for i in range(1, len(U)):
            if U[i] < U[least_index]:
                least_index = i

        # Remove least element from U
        swap(U[least_index], U[-1])

        least = U.pop()

        # Add least to S
        S.append(least)

    return S
```

---

# 8. Selection Sort Time Complexity

The worst-case time complexity is:

$$
O(n^2)
$$

Why?

The first search examines approximately:

$$
n
$$

elements.

The next examines approximately:

$$
n-1
$$

then:

$$
n-2
$$

and so on.

Therefore:

$$
n+(n-1)+(n-2)+\cdots+1
$$

This is equivalent to:

$$
\sum_{k=1}^{n} k
$$

Using the summation formula:

$$
\sum_{k=1}^{n} k
=
\frac{n(n+1)}{2}
$$

Therefore:

$$
T(n) \approx \frac{n^2+n}{2}
$$

When determining Big-O, constants and lower-order terms are ignored:

$$
\boxed{O(n^2)}
$$

---

# 9. Operation Counting

Your professor noted that **loop overhead is ignored** and you should count the important/key operations.

Example inner-loop calculation:

$$
S = 1 + (n-1)(2) + 2 + 1
$$

Simplify:

$$
S = 1 + 2n - 2 + 2 + 1
$$

$$
\boxed{S = 2n+2}
$$

Know how to simplify operation counts and then determine their asymptotic complexity.

For example:

$$
2n+2
$$

has complexity:

$$
\boxed{O(n)}
$$

---

# 10. Summations to Know

### Basic Sum

$$
\sum_{k=1}^{n} k
=
1+2+3+\cdots+n
$$

Formula:

$$
\boxed{\frac{n(n+1)}{2}}
$$

Therefore:

$$
\sum_{k=1}^{n} k = \Theta(n^2)
$$

You may also encounter expressions such as:

$$
\sum_{k=1}^{n}(k-1)
$$

which gives:

$$
0+1+2+\cdots+(n-1)
$$

and therefore:

$$
\boxed{\frac{n(n-1)}{2}}
$$

which is also:

$$
\boxed{\Theta(n^2)}
$$

---

# 11. Proof by Induction

**MIDTERM: KNOW THIS**

You should know how to prove a mathematical statement using induction.

### Step 1 — Base Case

Show that the statement is true for the starting value, usually:

$$
n=1
$$

### Step 2 — Inductive Hypothesis

Assume the statement is true for:

$$
n=k
$$

### Step 3 — Inductive Step

Use the assumption for \(k\) to prove the statement for:

$$
n=k+1
$$

### Structure

```text
1. Prove P(1)
2. Assume P(k) is true
3. Prove P(k+1)
4. Therefore P(n) is true
```

---

# 12. Big-O Proofs: Finding C and n₀

**MIDTERM: KNOW HOW TO FIND \(C\) AND \(n_0\)**

Definition:

$$
f(n)=O(g(n))
$$

if there exist positive constants:

$$
C>0
$$

and

$$
n_0
$$

such that:

$$
f(n)\le Cg(n)
$$

for every:

$$
n\ge n_0
$$

### Example

Suppose:

$$
f(n)=3n+2
$$

Show:

$$
3n+2=O(n)
$$

For \(n\ge1\):

$$
2\le2n
$$

Therefore:

$$
3n+2\le3n+2n
$$

$$
3n+2\le5n
$$

So one valid choice is:

$$
\boxed{C=5}
$$

and:

$$
\boxed{n_0=1}
$$

Therefore:

$$
\boxed{3n+2=O(n)}
$$

Remember: **\(C\) and \(n_0\) do not have to be unique.**

---

# 13. Limits and Asymptotic Notation

You should know how to use limits to compare growth rates.

A common comparison is:

$$
\lim_{n\to\infty}\frac{f(n)}{g(n)}
$$

### Case 1

If:

$$
\lim_{n\to\infty}\frac{f(n)}{g(n)}=0
$$

then \(f(n)\) grows slower than \(g(n)\).

---

### Case 2

If:

$$
0<L<\infty
$$

then the functions grow at the same asymptotic rate:

$$
f(n)=\Theta(g(n))
$$

---

### Case 3

If:

$$
\lim_{n\to\infty}\frac{f(n)}{g(n)}=\infty
$$

then \(f(n)\) grows faster than \(g(n)\).

**Professor specifically mentioned knowing Case 3.**

---

# 14. Amortized Analysis

### Definition

**Amortized analysis** is a technique used to analyze the average cost of operations over a **sequence of operations**.

It does **not** simply mean average-case analysis.

Some individual operations may be expensive, but if those expensive operations happen rarely, the average cost per operation can still be small.

### Classroom Example

Know the classroom example discussed in lecture.

Specifically identify:

* **Cost**
* **Period**

Think:

```text
How expensive is the event?
```

and:

```text
How frequently does the event occur?
```

---

# 15. Data Structures

## Dictionary

A **dictionary** stores:

$$
\boxed{\text{Key} \rightarrow \text{Data/Value}}
$$

Example:

```python
student = {
    "name": "Tara",
    "id": 123
}
```

`"name"` is a **key**.

`"Tara"` is its **value/data**.

---

# 16. Array vs. Linked List

### Array

Elements are stored in contiguous memory.

```text
[A][B][C][D]
```

Advantages:

* Fast indexing
* Access by index is typically \(O(1)\)

Example:

```python
A[3]
```

### Linked List

Elements are stored as nodes connected using pointers/references.

```text
[A] → [B] → [C] → [D] → NULL
```

Advantages:

* Can efficiently insert/remove nodes when the relevant node/location is already known.
* Does not require contiguous storage.

Random access is not constant time.

To reach the fourth element:

```text
A → B → C → D
```

So accessing an arbitrary position is generally:

$$
O(n)
$$

---

# 17. Stack

A stack follows:

$$
\boxed{\text{LIFO}}
$$

**Last In, First Out**

Think of a stack of plates.

```text
Push A
Push B
Push C

TOP
 ↓
[C]
[B]
[A]
```

Removing gives:

```text
C → B → A
```

Common operations:

```text
push
pop
peek/top
```

---

# 18. Queue

A queue follows:

$$
\boxed{\text{FIFO}}
$$

**First In, First Out**

Think of people waiting in line.

```text
A → B → C
```

A entered first, so A leaves first.

Common operations:

```text
enqueue
dequeue
front
```

---

# 19. Priority Queue

A **priority queue** removes elements according to their **priority**, rather than simply their insertion order.

Conceptually:

```text
(value, priority)
```

Example:

```text
A → priority 3
B → priority 1
C → priority 2
```

The next element removed depends on how the priority ordering is defined.

Priority queues are commonly implemented using a:

$$
\boxed{\text{Heap}}
$$

---

# 20. Binary Heap

A binary heap is a **complete binary tree** satisfying the heap property.

### Min-Heap

Each parent is less than or equal to its children.

```text
        2
       / \
      4   7
     / \
    9   10
```

### Max-Heap

Each parent is greater than or equal to its children.

### Important Complexity

Insertion into a binary heap:

$$
\boxed{O(\log n)}
$$

Why?

A newly inserted element may have to move upward through the height of the tree.

The height of a complete binary tree is:

$$
O(\log n)
$$

Therefore heap insertion is:

$$
\boxed{O(\log n)}
$$

---

# 21. Graphs

**EXPECT MANY GRAPH QUESTIONS**

A graph is commonly represented as:

$$
G=(V,E)
$$

where:

* \(V\) = vertices
* \(E\) = edges

Example:

```text
A ----- B
|       |
|       |
C ----- D
```

Vertices:

$$
V=\{A,B,C,D\}
$$

---

# 22. Degree of a Vertex

The **degree** of a vertex is the number of edges connected to it in an undirected graph.

Example:

```text
    B
    |
A---C---D
```

For vertex \(C\):

$$
\deg(C)=3
$$

because three edges connect to \(C\).

For directed graphs, distinguish:

* **in-degree** = number of incoming edges
* **out-degree** = number of outgoing edges

---

# 23. Complete Graph

A **complete graph** is a graph where **every pair of distinct vertices is connected by an edge**.

Notation:

$$
K_n
$$

Example \(K_4\):

```text
A ----- B
|\     /|
| \   / |
|  \ /  |
|  / \  |
| /   \ |
|/     \|
C ----- D
```

Every vertex connects to every other vertex.

Number of edges in an undirected complete graph:

$$
\boxed{\frac{n(n-1)}{2}}
$$

---

# 24. Adjacency Matrix

An adjacency matrix represents connections between vertices.

Suppose:

```text
A ----- B
|
|
C
```

Edges:

$$
(A,B)
$$

and:

$$
(A,C)
$$

The adjacency matrix is:

|       |  A |  B |  C |
| ----- | -: | -: | -: |
| **A** |  0 |  1 |  1 |
| **B** |  1 |  0 |  0 |
| **C** |  1 |  0 |  0 |

A:

$$
1
$$

means an edge exists.

A:

$$
0
$$

means no edge exists.

For an **undirected graph**, the adjacency matrix is symmetric.

---

# MIDTERM PRIORITY CHECKLIST

Make sure you can do the following without relying only on memorization:

* Explain **naïve algorithms**
* Explain **sequential search**
* Know why sequential search is \(O(n)\)
* Explain **sequential search vs. sequential optimization**
* Explain why sequential optimization checks all elements
* Explain the **sorting problem**
* Perform **selection sort by hand**
* Know the three pure selection sort steps:

  * Find
  * Remove
  * Append
* Derive why selection sort is \(O(n^2)\)
* Work with summations such as:

$$
\sum_{k=1}^{n}k
$$

* Perform a **proof by induction**
* Find \(C\) and \(n_0\) in a Big-O proof
* Solve limits involving asymptotic notation
* Know the three limit cases, especially **Case 3**
* Explain **amortized analysis**
* Identify the **cost and period** in an amortized-analysis problem
* Define a **dictionary**
* Compare **arrays and linked lists**
* Know **Stack = LIFO**
* Know **Queue = FIFO**
* Explain a **priority queue**
* Understand basic **binary heaps**
* Know binary-heap insertion is \(O(\log n)\)
* Identify graph **vertices and edges**
* Find the **degree** of a vertex
* Recognize a **complete graph**
* Construct an **adjacency matrix**
