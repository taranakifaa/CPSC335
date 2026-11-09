# CPSC 335 — Divide & Conquer Quiz Review

**Modules 11–12 | Based on the supplied course study guide**  
**Important:** Master Theorem case numbers below follow your instructor's numbering (some textbooks swap Cases 1 and 3).

## 1. Divide and Conquer

1. **Base case:** Stop recursion on a small input.
2. **Divide:** Split into smaller subproblems.
3. **Conquer:** Recursively solve them.
4. **Combine:** Construct the final answer.

```python
def solve(instance):
    if is_base_case(instance):
        return direct_answer(instance)
    left, right = divide(instance)
    return combine(solve(left), solve(right))
```

**Depth is not runtime:** Halving gives about `log₂(n)` recursion levels, but both branches may be explored. Subtracting 1 each step gives `n` levels.

## 2. Fast algorithm comparison

| Algorithm | Calls per step | Outside work | Recurrence | Time |
|---|---:|---:|---|---|
| Minimum (index ranges) | 2 | Θ(1) | `2T(n/2)+1` | **Θ(n)** |
| Summation (loop) | 0 | One pass | — | **Θ(n)** |
| Summation (copied halves) | 2 | Θ(n) copying | `2T(n/2)+n` | **Θ(n log n)** |
| Summation (index ranges) | 2 | Θ(1) | `2T(n/2)+1` | **Θ(n)** |
| Merge operation alone | 0 | Θ(n) | — | **Θ(n)** |
| Merge sort | 2 | Θ(n) merge | `2T(n/2)+n` | **Θ(n log n)** |
| Binary search (sorted array) | 1 | Θ(1) | `T(n/2)+1` | **Θ(log n)** worst case |

### Binary search vs. merge sort

| Feature | Binary search | Merge sort |
|---|---|---|
| Purpose | Find a target | Sort all elements |
| Input must be sorted? | **Yes** | No |
| Recursive calls | **One** half | **Both** halves |
| Combine step | None | Merge two sorted lists |
| Worst-case time | Θ(log n) | Θ(n log n) |
| Base case | Found target or empty range | 0 or 1 element |

## 3. Master Theorem (quiz priority)

For **`T(n) = rT(n/d) + Θ(n^k)`**:

- `r` = number of recursive calls **actually made**
- `d` = shrink factor (`n/2` means `d=2`)
- `k` = exponent of dominant outside work (`1` → 0, `√n` → 1/2, `n` → 1, `n²` → 2)

| Instructor case | Compare `r` and `d^k` | Result | Dominant work |
|---|---|---|---|
| **1** | `r < d^k` | **Θ(n^k)** | Root |
| **2** | `r = d^k` | **Θ(n^k log n)** | All levels |
| **3** | `r > d^k` | **Θ(n^(log_d r))** | Leaves |

**Five steps:** Find `r,d,k` → compute `d^k` → compare → choose case → simplify.

| Recurrence | `r,d,k` | Compare | Case | Answer |
|---|---|---|---|---|
| `T(n/2)+n²` | 1,2,2 | 1 < 4 | 1 | Θ(n²) |
| `2T(n/4)+√n` | 2,4,1/2 | 2 = 2 | 2 | Θ(√n log n) |
| `3T(n/2)+n` | 3,2,1 | 3 > 2 | 3 | Θ(n^(log₂3)) |
| `2T(n/2)+n` | 2,2,1 | 2 = 2 | 2 | Θ(n log n) |
| `4T(n/2)+n` | 4,2,1 | 4 > 2 | 3 | Θ(n²) |
| `2T(n/2)+1` | 2,2,0 | 2 > 1 | 3 | Θ(n) |
| `T(n/2)+1` | 1,2,0 | 1 = 1 | 2 | Θ(log n) |

**When NOT to apply this simple polynomial table:** `nT(n/2)+n` (nonconstant call multiplier), `T(√n)` (not fixed shrink factor), `2T(n/2)+2^n` (exponential outside work), or negative outside work. `n log n` is not exactly Θ(n^k), so use an extended theorem or recursion tree rather than dropping the log.

## 4. Minimum selection

Split the list, find the minimum of each half, then compare those **two answers**.

Example: `[8,3,6,2]` → minimums `3` and `2` → **2**.

```python
def minimum_range(v, s, e):  # [s,e), nonempty
    if e - s == 1:
        return v[s]
    m = (s + e) // 2
    return min(minimum_range(v, s, m), minimum_range(v, m, e))
```

- Range-based: `T(n)=2T(n/2)+Θ(1)` → **Θ(n)**, stack Θ(log n).
- Copied halves: copying changes work to Θ(n) per call → **Θ(n log n)**.
- An empty list has **no minimum** unless the problem defines one. Returning 0 is not generally correct.

## 5. Recursive summation vs. a loop

A loop scans each element once: **Θ(n)** time, **Θ(1)** extra space.

```python
def sum_dbh(v):
    if len(v) == 0:
        return 0
    if len(v) == 1:
        return v[0]
    m = len(v) // 2
    return sum_dbh(v[:m]) + sum_dbh(v[m:])
```

Python slices `v[:m]` and `v[m:]` **copy elements**. Thus the lecture's version is `2T(n/2)+Θ(n)` → **Θ(n log n)**. If passing index ranges instead, outside work becomes Θ(1) → **Θ(n)**.

**Quiz shortcut:** Before writing a recurrence, ask: *Does the code copy arrays, scan/merge arrays, or only adjust indices?*

## 6. Merge sort and stability

**Steps:** Split into halves → sort both recursively → **merge in order**.

Example: `[7,2,8,4,5,6,1,3]`

1. Split: `[7,2,8,4]` / `[5,6,1,3]`
2. Split to single elements.
3. Merge pairs: `[2,7]`, `[4,8]`, `[5,6]`, `[1,3]`
4. Merge groups: `[2,4,7,8]`, `[1,3,5,6]`
5. Final: **`[1,2,3,4,5,6,7,8]`**

```python
def merge_sort(v):
    if len(v) <= 1:
        return v
    m = len(v) // 2
    return merge(merge_sort(v[:m]), merge_sort(v[m:]))

def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # left wins ties: stable
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])
    out.extend(right[j:])
    return out
```

- Merge alone takes **Θ(n)**.
- Merge sort: `2T(n/2)+Θ(n)` → **Θ(n log n)**.
- Standard array merge sort uses **Θ(n)** extra array storage and **Θ(log n)** stack depth.
- **Stable sort** keeps equal-key records in their original relative order. Choose the **left** item on a tie (`<=`).
- **Concatenating is NOT merging:** `[2,7]+[1,5]` is not sorted; proper merge is `[1,2,5,7]`.

## 7. Binary search

**Only works on sorted input.** Compare the target to the middle, then discard one half. It has **one recursive call**, not two.

```python
def binary_search(v, q, s=0, e=None):
    if e is None:
        e = len(v)
    if s == e:
        return None
    m = (s + e) // 2
    if q < v[m]:
        return binary_search(v, q, s, m)
    if q == v[m]:
        return m
    return binary_search(v, q, m + 1, e)
```

**Half-open indices:** `[s,e)` includes `s`, excludes `e`.

Trace for target **25** in `[1,2,3,9,11,13,17,25,57,90]`:

| Step | s | e | m | v[m] | Action |
|---|---:|---:|---:|---:|---|
| 1 | 0 | 10 | 5 | 13 | Search `[6,10)` |
| 2 | 6 | 10 | 8 | 57 | Search `[6,8)` |
| 3 | 6 | 8 | 7 | 25 | Return **7** |

- `T(n)=T(n/2)+Θ(1)` → **Θ(log n)** worst case; **Θ(1)** best case.
- Recursive stack: O(log n); iterative implementation: O(1) auxiliary space.
- With duplicates, ordinary binary search need not return the first matching index.

## 8. Limits of simple divide and conquer

For **Traveling Salesman**, optimal tours for separate halves do not necessarily combine into a globally optimal tour. For **circuit satisfiability**, variables and connections can link the halves. Splitting alone does not solve global dependencies.

## 9. Common quiz traps

- **Two branches in an `if/else` ≠ two executed recursive calls.** Binary search uses one.
- **Halving ≠ automatically O(log n).** Merge sort explores both halves.
- **Copying slices matters.** Python slicing can increase recursive summation from Θ(n) to Θ(n log n).
- **Merging ≠ concatenating.** Merge requires ordered comparisons.
- **Do not forget leftovers** after one merge list runs out.
- **Stability:** choose left on equal keys (`<=`).
- **Binary search requires sorted data.**
- **Do not mix `[s,e)` and `[s,e]` endpoints.**
- **Use the dominant term** to determine `k`.
- **Do not apply the simple theorem outside its assumptions.**

## 10. Quick practice quiz

1. What are divide, conquer, combine, and base case?
2. Why doesn't logarithmic recursion depth imply logarithmic runtime?
3. Solve `4T(n/2)+n` and name the instructor case.
4. Solve `2T(n/4)+√n`.
5. Solve `T(n/2)+n²`.
6. Solve `2T(n/2)+1`.
7. Why is copied recursive summation slower asymptotically than a loop?
8. Merge `[2,5,9]` and `[1,5,7]` stably.
9. What can changing `<=` to `<` break during merge?
10. Binary-search for 9 in `[1,2,3,9,11,13,17,25,57,90]` using `[s,e)`.
11. Why is binary search `r=1`?
12. Does the simple Master Theorem cover `nT(n/2)+n`?
13. Why can't an empty minimum-selection input return 0 by default?
14. Can optimal traveling-salesman tours on halves always combine into a global optimum?

<details>
<summary>Answer key — check after trying</summary>

1. Split, recursively solve, combine; stop at a base case.
2. Runtime also counts number of subproblems and work at each level.
3. `r=4,d=2,k=1`; Case **3** → **Θ(n²)**.
4. `r=2,d=4,k=1/2`; Case **2** → **Θ(√n log n)**.
5. `r=1,d=2,k=2`; Case **1** → **Θ(n²)**.
6. `r=2,d=2,k=0`; Case **3** → **Θ(n)**.
7. Copies Θ(n) total elements per level over Θ(log n) levels; loop scans once.
8. `[1,2,5_left,5_right,7,9]`.
9. **Stability**, because a right-side tie may jump ahead.
10. `(s,e,m)`: `(0,10,5)` → `(0,5,2)` → `(3,5,4)` → `(3,4,3)` → index **3**.
11. Only one possible half is actually searched.
12. **No**, recursive-call multiplier `n` is not constant.
13. Empty input has no minimum; 0 may be smaller than every actual element.
14. **No**, cross-boundary connections affect global optimality.

</details>

## 11. Last-minute study priority

1. **Master Theorem:** identify `r,d,k`, compare `r` to `d^k`.
2. **Binary search vs. merge sort:** one branch vs. two; Θ(log n) vs. Θ(n log n).
3. **Copied vs. index-range summation:** Θ(n log n) vs. Θ(n).
4. **Merge trace and stability:** `<=` chooses left on ties.
5. **Base cases and half-open indices.**

**One question to ask on every recurrence:** *How many recursive calls actually run, how large are they, and what work happens outside them?*
