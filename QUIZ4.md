CPSC 335 — Divide and Conquer Study Guide
Tara • Fall 2026 • Modules 11 and 12

Based on Dr. Chia Hsuan Tsai’s Canvas-linked lecture decks, reviewed November 2, 2026:
- Part 1 — 19 slides
- Part 2 — 21 slides
Slide references below identify the course material. Worked explanations, corrected executable-style pseudocode, practice questions, and implementation comparisons are added study aids, not claims about what will appear on an exam. This guide follows your instructor’s case numbering.
1. What divide and conquer actually does
Part 1, slides 2–6

Break a large problem into smaller versions of the same problem, solve them recursively, and use their answers to solve the original problem.
1. Divide: Identify smaller subproblems.
2. Conquer: Solve those subproblems recursively.
3. Combine: Construct the original answer from their results.
4. Base case: Solve a sufficiently small input directly, so recursion stops.
solve(instance):
    if instance is a base case:
        return direct answer
    L, R = divide(instance)
    left_answer = solve(L)
    right_answer = solve(R)
    return combine(left_answer, right_answer)
The base case is checked first even though the strategy is called divide–conquer–combine.

Do not confuse recursion depth with total runtime. Repeatedly halving an input produces about log₂ n levels. However, an algorithm may visit many subproblems on each level. Binary search follows one branch; merge sort processes both.
Reduction	Sizes along one branch	Approximate depth
Decrease by one	n, n−1, n−2, …, 1	n
Decrease by half	n, n/2, n/4, …, 1	log₂ n
Decrease by factor d > 1	n, n/d, n/d², …, 1	log_d n


The slides discuss potential speed and cache advantages, as well as recursion’s memory and stack costs. These are possibilities, not guarantees: recursive summation below is slower than a simple loop when it copies sublists. Also, recursively solving Tower of Hanoi still takes exponential time; divide and conquer does not automatically make a problem polynomial-time.
2. Minimum selection
Part 1, slides 7–8

Input: A nonempty collection of comparable values. Output: Its smallest value.
- Base case: One element; return it.
- Divide: Split into two roughly equal parts.
- Conquer: Find each part’s minimum.
- Combine: Return the smaller of those two answers.
Example: [8, 3, 6, 2] becomes [8, 3] and [6, 2]. Their minima are 3 and 2, so the final answer is 2. The combine step compares two answers, not every original element again.

Using index ranges avoids copying:
def minimum_range(V, s, e):  # V[s:e], nonempty; e is excluded
    if e - s == 1:
        return V[s]
    m = (s + e) // 2
    a = minimum_range(V, s, m)
    b = minimum_range(V, m, e)
    return min(a, b)
With constant-time indexing and comparisons, the recurrence is T(n) = 2T(n/2) + Θ(1), giving Θ(n) time and Θ(log n) stack depth. There are n−1 comparisons. If the implementation copies both sublists at every split, copying changes the overhead to Θ(n) per call and the total to Θ(n log n).

The empty input has no minimum unless the specification supplies a special convention. Do not silently return 0: that would be wrong for an all-positive list.
3. Summation: the implementation changes the analysis
Part 1, slides 9–13 and 19

Input: A list of numbers. Output: Their total.

The straightforward loop takes Θ(n) time and Θ(1) auxiliary space. The divide-and-conquer solution uses these base cases:
- Empty list → 0.
- One-element list → that element.
For larger inputs, recursively sum both halves and add the two returned totals.
def sum_dbh(V):
    n = len(V)
    if n == 0:
        return 0
    if n == 1:
        return V[0]
    half = n // 2
    L = V[:half]  # Copies elements for a Python list
    R = V[half:]  # Copies elements for a Python list
    return sum_dbh(L) + sum_dbh(R)
The lecture charges for copying L and R: |L| + |R| = n. Adding the returned totals is constant time. Thus its recurrence is:

T(n) = 2T(n/2) + n + 5 → O(n log n).

Under the standard unit-cost model, the tight bound is Θ(n log n). If ranges are passed without copying, the recurrence instead becomes 2T(n/2) + Θ(1), yielding Θ(n). Both algorithms still need to account for every input element.

Exam habit: Before writing a recurrence, ask whether the code copies data, scans data, or merely adjusts indices.
4. Read and solve a recurrence
Part 1, slides 14–19

The slides use T(n) = rT(n/d) + c(n).
Symbol	Meaning	What to look for in code
r	Number of recursive subproblems actually solved	Recursive calls that execute
d	Factor by which each subproblem shrinks	n/2 means d = 2; n/4 means d = 4
c(n)	Work outside the recursive calls	Splitting, copying, comparisons, merging
k	Polynomial exponent of the outside work	Constant → 0; √n → 1/2; n → 1; n² → 2


Do not set r = 2 merely because you see an if/else containing two possible recursive calls. Binary search executes only one of them.
Master Theorem: your instructor’s numbering
For the simple polynomial form c(n) = Θ(n^k), compare r with d^k:
Course case	Comparison	Tight bound for this polynomial form	Where work dominates
Case 1	r < d^k	Θ(n^k)	Near the root
Case 2	r = d^k	Θ(n^k log n)	Comparable totals across levels
Case 3	r > d^k	Θ(n^(log_d r))	Near the leaves


Your slides state O bounds. Θ here states a tight bound when the outside work is Θ(n^k) and base cases take constant positive time. Some references reverse Cases 1 and 3, so use the inequality rather than memorizing a case number alone.

Five-step method:
1. Identify r and d.
2. Simplify the nonrecursive work to its dominant growth term.
3. Determine k.
4. Compute d^k and compare it with r.
5. Substitute into the matching result and simplify.
Lecture examples, worked
Recurrence	r, d, k	Comparison	Result
T(n) = T(n/2) + ½n² + n	1, 2, 2	1 < 4: Case 1	Θ(n²)
T(n) = 2T(n/4) + √n + 52	2, 4, 1/2	2 = √4: Case 2	Θ(√n log n)
T(n) = 3T(n/2) + ¾n + n	3, 2, 1	3 > 2: Case 3	Θ(n^(log₂3))
T(n) = 2T(n/2) + n + 5	2, 2, 1	2 = 2: Case 2	Θ(n log n)


For example, √n is n^(1/2), so k = 1/2, not 1. The constant 52 does not change the dominant term.
Why the three cases make sense
At level i there are r^i subproblems, each of size n/d^i. For polynomial overhead, total work on that level is proportional to:

r^i(n/d^i)^k = n^k(r/d^k)^i.

The ratio r/d^k determines whether the level totals decrease, stay equal, or increase. This is a geometric-series interpretation of the theorem.

For merge sort, r/d^k = 2/2 = 1. Each level costs Θ(n), and there are Θ(log n) levels: Θ(n log n).
When the simple table does not apply
The lecture flags nonconstant parameters and invalid overhead terms. Examples include:
- 2^n T(n/2) + n²: the recursive-call multiplier depends on n.
- T(√n): the recursive size is not n divided by a fixed constant.
- 27T(n/9) − n² log n: negative outside work does not model the required nonnegative processing cost.
- 2T(n/2) + 2^n: exponential outside work is outside the course’s polynomial framework.
Clarification: Being polynomially bounded is not the same as being exactly Θ(n^k). Terms such as n log n need appropriate handling; do not drop the log and claim a tight bound from this table. For example, 2T(n/2) + Θ(n log n) is Θ(n(log n)²), obtainable by a recursion tree or an extended theorem. Failure of this table does not mean the recurrence has no solution.
5. Merge sort
Part 2, slides 2–13

Input: Comparable elements. Output: The same elements in nondecreasing order.
- Divide: Split near the middle.
- Conquer: Recursively sort both halves.
- Combine: Merge the sorted halves.
- Base case: Length 0 or 1 is already sorted.
def merge_sort(V):
    if len(V) <= 1:
        return V
    m = len(V) // 2
    L = merge_sort(V[:m])
    R = merge_sort(V[m:])
    return merge(L, R)

def merge(L, R):
    S = []
    i = j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            S.append(L[i])
            i += 1
        else:
            S.append(R[j])
            j += 1
    while i < len(L):
        S.append(L[i])
        i += 1
    while j < len(R):
        S.append(R[j])
        j += 1
    return S
The remaining minimum must be at the current front of one of the two sorted lists. Each comparison chooses one element in constant time. Once one list is exhausted, append the remainder of the other.

Concatenation is not merging: [2, 7] + [1, 5] gives [2, 7, 1, 5]. A correct merge gives [1, 2, 5, 7].
Worked example from slide 10
Input: [7, 2, 8, 4, 5, 6, 1, 3].
Stage	Sublists
First split	[7,2,8,4] and [5,6,1,3]
Second split	[7,2], [8,4], [5,6], [1,3]
Base cases	Eight one-element lists
Merge pairs	[2,7], [4,8], [5,6], [1,3]
Merge groups of four	[2,4,7,8] and [1,3,5,6]
Final merge	[1,2,3,4,5,6,7,8]


In the final merge, compare 2 with 1 and take 1; compare 2 with 3 and take 2; compare 4 with 3 and take 3; continue until one side is empty.
Complexity
Merging lists with n total elements takes Θ(n), because every element is placed into the output exactly once. The loops are sequential, and their combined number of output insertions is n.

Copying halves costs Θ(n); merging costs Θ(n). Together they remain Θ(n), not Θ(n²). The lecture obtains approximately:

T(n) = 2T(n/2) + 2n + 2 → Θ(n log n).

Odd lengths produce floor(n/2) and ceiling(n/2), which do not change the bound. Standard array merge sort uses Θ(n) peak auxiliary storage, plus Θ(log n) recursive stack depth. The shown version is not in-place because it creates new lists.
6. Stability
Part 2, slide 14

A stable sort preserves the original relative order of elements whose sorting keys are equal.

Example: input records (80, Ana), (70, Bo), (80, Cy) sorted by score become (70, Bo), (80, Ana), (80, Cy). Ana stays before Cy.

In merge, choose the left element on a tie. That is why the code uses L[i] <= R[j]. If an equal element on the right is chosen first, it can move ahead of an equal element originally to its left.

Stability is useful when sorting records on multiple attributes: a stable second sort preserves the earlier ordering within tied groups. It does not mean that values never move or that the algorithm runs at a constant speed.
7. Binary search
Part 2, slides 15–19

Requirement: The input is already sorted in nondecreasing order. Compare the target with the middle element and discard the half that cannot contain it.

The detailed lecture code uses a half-open range [s, e): s is included, e is excluded. Initially, s = 0 and e = len(V).
def binary_search(V, q):
    return search_range(V, q, 0, len(V))

def search_range(V, q, s, e):
    if s == e:
        return None
    m = (s + e) // 2
    if q < V[m]:
        return search_range(V, q, s, m)
    if q == V[m]:
        return m
    return search_range(V, q, m + 1, e)
Use integer division for the midpoint in executable Python. The lecture’s general description also mentions inclusive endpoints; do not mix that description with the half-open code above.
Trace using the slide 16 array
V = [1, 2, 3, 9, 11, 13, 17, 25, 57, 90], target q = 25. Indices are zero-based.
Step	s	e (excluded)	m	V[m]	Decision
1	0	10	5	13	25 > 13 → search [6,10)
2	6	10	8	57	25 < 57 → search [6,8)
3	6	8	7	25	Return index 7


Only one recursive call executes per step. There is no merge step, and the range-based implementation does not copy arrays:

T(n) = T(n/2) + Θ(1).

Thus r = 1, d = 2, k = 0; d^k = 1. Course Case 2 gives Θ(log n) worst-case time. Best case is Θ(1) when the first middle element matches. Recursive stack space is O(log n); an iterative version can use O(1) auxiliary space.

If duplicates exist, this code returns a matching index, not necessarily the first occurrence. Finding the first occurrence requires modified logic.
8. When splitting is not enough
Part 2, slides 20–21

The course’s simple balanced approach needs a useful way to divide the instance and a correct way to combine independently computed answers.

The slides use traveling salesman and circuit satisfiability to illustrate global dependencies. For traveling salesman, two independently optimal local tours do not automatically combine into a globally optimal tour. For a circuit, shared variables and connections can couple the pieces.

Interpret this as a limit of the simple independent-halves pattern, not a claim that no specialized recursive approach can ever help these problems.
9. One-page review table
Algorithm / implementation	Calls per recursive step	Outside work	Time
Minimum, index ranges	2 on half-size inputs	Θ(1)	Θ(n)
Summation loop	None	One pass	Θ(n)
Summation, copied halves in lecture	2 on half-size inputs	Θ(n)	Θ(n log n)
Summation, index ranges	2 on half-size inputs	Θ(1)	Θ(n)
Merge alone	None	Place n elements	Θ(n)
Merge sort	2 on half-size inputs	Θ(n)	Θ(n log n)
Binary search, index ranges	1 on a half-size input	Θ(1)	Θ(log n) worst case


Mistakes to catch before submitting an answer
- Counting possible branches instead of recursive calls actually executed.
- Assuming every halving algorithm is O(log n).
- Forgetting the cost of copied sublists.
- Treating merging as concatenation.
- Forgetting to append leftover elements during merge.
- Choosing the right element on a tie while claiming stability.
- Using binary search on an unsorted list.
- Mixing inclusive and exclusive endpoints.
- Choosing k from a lower-order term or arbitrarily loose bound.
- Applying the simple Master Theorem table outside its assumptions.
10. Practice — solve before checking the answers
1. Explain divide, conquer, combine, and the base case for minimum selection.
2. Why does logarithmic recursion depth not guarantee logarithmic runtime?
3. Solve T(n) = 4T(n/2) + n. State r, d, k, and the course case.
4. Solve T(n) = 2T(n/4) + √n.
5. Solve T(n) = T(n/2) + n².
6. Solve T(n) = 2T(n/2) + 1.
7. Explain why the lecture’s recursive summation is O(n log n), while a loop is O(n).
8. Trace merging [2, 5, 9] with [1, 5, 7]. Label the two 5s by their source list.
9. What property can be lost by changing <= to < in the merge comparison?
10. Trace binary search for 9 in [1,2,3,9,11,13,17,25,57,90], using [s,e).
11. Why does binary search have r = 1 even though it divides the range into two sides?
12. Does the course’s simple theorem apply to T(n) = nT(n/2) + n? Explain.
13. What is wrong with using an empty list as a minimum-selection base case that returns 0?
14. Can two optimal tours on disjoint halves always be combined into an optimal traveling-salesman tour?
11. Answer key
1. Split into halves, recursively find both minima, compare them, and return the sole element for a one-element input.
2. Depth measures one path. Total runtime also includes the number of nodes and work at each node.
3. r=4, d=2, k=1; 4>2 → Course Case 3 → Θ(n²).
4. r=2, d=4, k=1/2; 2=4^(1/2) → Case 2 → Θ(√n log n).
5. r=1, d=2, k=2; 1<4 → Case 1 → Θ(n²).
6. r=2, d=2, k=0; 2>1 → Case 3 → Θ(n).
7. The lecture copies n total elements across its sublists at each split, giving Θ(n) work per level over Θ(log n) levels. The loop visits each element once.
8. [1, 2, 5_L, 5_R, 7, 9]; left 5 wins the tie. Once the right list runs out, append 9.
9. Stability: an equal right-side element can move ahead of an equal left-side element.
10. (s,e,m) = (0,10,5): 13 is too large; (0,5,2): 3 is too small; (3,5,4): 11 is too large; (3,4,3): 9 matches. Return 3.
11. It recursively searches only the side that can contain the target; the other side is discarded.
12. No. r=n is not constant.
13. An empty list has no minimum under the given specification, and 0 could incorrectly beat all actual positive values.
14. No. Cross-boundary edges and the global tour constraint mean independently optimal local answers need not yield a global optimum.
12. Suggested study order
1. Explain the DCC pattern aloud using minimum selection.
2. Compare copied summation with range-based summation.
3. Solve the four Master Theorem lecture examples without looking.
4. Trace merge sort on eight numbers and perform the final merge by hand.
5. Explain stability using two equal-key records.
6. Trace binary search, explicitly recording s, e, and m.
7. Finish the practice set, then review only the mistakes.
The central question to keep asking is: How many subproblems do I actually solve, how big are they, and what work happens outside those recursive calls?
