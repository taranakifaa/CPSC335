# 📚 Quiz Review

**Quiz:** 9/9
**Presentation:** 9/18

---

# 1. Asymptotic Notations

### What are asymptotic notations?

Asymptotic notation is a way to describe **how fast an algorithm grows as the input size `n` gets bigger**.

Think:

> **"How does the running time of my program change when `n` gets really large?"**

We usually care about the **growth rate**, not the exact number of seconds.

### The 3 Important Notations

| Notation    | Name      | Meaning     | Easy Way to Remember         |
| ----------- | --------- | ----------- | ---------------------------- |
| **O(g(n))** | Big-O     | Upper bound | **At most this fast**        |
| **Ω(g(n))** | Big-Omega | Lower bound | **At least this fast**       |
| **Θ(g(n))** | Big-Theta | Tight bound | **Exactly this growth rate** |

---

## Big-O: `O(g(n))`

**Big-O gives an upper bound.**

If:

`f(n) ∈ O(g(n))`

then `f(n)` does **not grow faster than** `g(n)` (up to a constant factor) for large enough `n`.

### Think:

> **O = Upper limit**

Example:

`f(n) = 2n + 3`

We can say:

`f(n) ∈ O(n)`

because as `n` gets larger, the function grows at the same general rate as `n`.

---

## Big-Omega: `Ω(g(n))`

**Big-Omega gives a lower bound.**

If:

`f(n) ∈ Ω(g(n))`

then `f(n)` grows **at least as fast as** `g(n)` (up to a constant factor) for large enough `n`.

### Think:

> **Ω = Lower limit**

---

## Big-Theta: `Θ(g(n))`

**Big-Theta gives a tight bound.**

If:

`f(n) ∈ Θ(g(n))`

then `g(n)` describes the growth rate of `f(n)` from **both above and below**.

### Think:

> **Θ = Tight / exact growth category**

For example:

`f(n) = 2n + 3`

is:

`Θ(n)`

because it grows linearly.

### ⭐ Important

**Theta represents the tight bound.**

---

# 2. The Figures

You do **not necessarily need to memorize the exact mathematical notation**.

Focus on remembering what the figures mean:

### Big-O

**Upper bound**

`f(n)` stays **below** a constant multiple of `g(n)`.

### Big-Omega

**Lower bound**

`f(n)` stays **above** a constant multiple of `g(n)`.

### Big-Theta

**Tight bound**

`f(n)` is trapped **between an upper and lower bound**.

---

# 3. What Do `C`, `C₁`, and `C₂` Mean?

These are just **positive constants**.

You don't need to overthink them.

* `C` → used for Big-O
* `C₁` → upper-bound constant for Theta
* `C₂` → lower-bound constant for Theta
* `n₀` → some point after which the relationship is true

The important idea is:

> **We care about what happens when `n` becomes large.**

---

# 4. Categorizing Functions

Big-O can be used to put functions into **categories based on how quickly they grow**.

Common growth rates:

### From fastest → slowest growth

```text
log(n)
   ↓
n
   ↓
n²
   ↓
n² log(n)
   ↓
n³
   ↓
2ⁿ
   ↓
nⁿ
```

Actually, when talking about **algorithm efficiency**, the smaller-growth functions are generally better.

So:

> `log(n)` is generally more efficient than `n`

and:

> `n` is generally more efficient than `n²`

and:

> `n²` is generally more efficient than `2ⁿ`

### ⭐ Key idea

An algorithm **A** is more efficient than algorithm **B** if A's running time has a **lower order of growth**.

---

# 5. Examples of Big-O Categories

### Example 1

`2n + 3`

is:

`O(n)`

### Example 2

`5n`

is:

`O(n)`

Even though the functions are different, they belong to the same **growth category**.

Why?

Because constants don't matter when we're looking at growth rate.

So:

```text
2n + 3 → O(n)

5n → O(n)
```

Both are **linear**.

---

# 6. Simplifying Big-O

When finding Big-O, we usually ignore:

### Constants

```text
5n → O(n)

100n → O(n)
```

### Smaller terms

```text
n² + n + 10 → O(n²)
```

The `n²` term grows much faster than `n` or `10`.

### ⭐ Quick Rule

> **Keep the fastest-growing term and ignore constants.**

Examples:

```text
3n + 7        → O(n)

4n² + 2n + 8  → O(n²)

5n³ + 10n     → O(n³)
```

---

# 7. True or False Review

From the notes:

1. **True**
2. **True**
3. **True**
4. **True**
   `n² × n² = n⁴`
5. **True**
6. **False** — `n⁶` grows faster than `n⁵`
7. **Yes / True** — because the function is within the required **bound**

### ⭐ Remember

If a function grows faster than the proposed upper bound, it **cannot** be Big-O of that function.

For example:

`n⁶` is **not** `O(n⁵)`

because:

`n⁶` grows faster than `n⁵`.

---

# 8. Step Counts

### What is a step?

A **step** is one basic operation performed by an algorithm.

For example:

```text
x = y
```

can count as **1 step**.

Even a more complicated statement can sometimes count as one step if its execution time doesn't depend on the size of the input.

Example:

```text
return a + b + b*c + (a+b-c)/(a+b) + 4
```

can be treated as **1 step**.

### ⭐ Main Idea

When analyzing an algorithm:

> **Count how many times the important operations happen.**

---

# 9. While Loops & Step Counts

This is likely to be important on the quiz.

Consider a loop where:

```text
i = i + 1
```

If `i` increases by **1 each time**, it usually takes about:

`n`

iterations.

### Example

```text
i = 0

while i < n:
    i = i + 1
```

Values of `i`:

```text
0
1
2
3
4
...
n
```

So the loop runs approximately **n times**.

### Complexity:

`O(n)`

---

# 10. Dividing by 2 in a Loop

This is a very important pattern.

Suppose we have:

```text
i = n

while i > 1:
    i = i / 2
```

Every time the loop runs, `i` gets cut in half.

The values look like:

```text
n
n/2
n/4
n/8
n/16
...
1
```

After `k` runs:

```text
n / 2ᵏ = 1
```

Now solve for `k`:

```text
n / 2ᵏ = 1

n = 2ᵏ

k = log₂(n)
```

Therefore:

### ⭐ Complexity:

`O(log₂ n)`

or simply:

`O(log n)`

---

# 11. Easy Way to Remember Loop Patterns

### Adding 1

```text
i = i + 1
```

Usually:

**O(n)**

Because you're moving through the values one at a time.

---

### Multiplying by 2

```text
i = i * 2
```

Usually:

**O(log n)**

Because the value grows exponentially.

---

### Dividing by 2

```text
i = i / 2
```

Usually:

**O(log n)**

Because the number gets cut in half each time.

---

# 12. Quiz Cheat Sheet 🧠

### Asymptotic Notation

```text
O    = Upper Bound
Ω    = Lower Bound
Θ    = Tight Bound
```

### Growth Rates

```text
log(n)  → very efficient

n       → linear

n²      → quadratic

n³      → cubic

2ⁿ      → exponential

nⁿ      → extremely fast growth
```

### Big-O Simplification

> **Ignore constants. Keep the fastest-growing term.**

```text
5n + 10        → O(n)

3n² + 4n + 1   → O(n²)

7n³ + 2n²      → O(n³)
```

### Loop Patterns

```text
i = i + 1  → O(n)

i = i * 2  → O(log n)

i = i / 2  → O(log n)
```

### Dividing by 2

Remember:

```text
n / 2ᵏ = 1

n = 2ᵏ

k = log₂(n)
```

So:

**`i = i / 2` → `O(log n)`**

---

# ⭐ Most Important Things to Know for the Quiz

1. **Big-O = upper bound**
2. **Big-Omega = lower bound**
3. **Big-Theta = tight bound**
4. **Theta is the tight/exact growth category**
5. **Ignore constants when simplifying Big-O**
6. **Keep the fastest-growing term**
7. **`i = i + 1` → usually `O(n)`**
8. **`i = i / 2` → usually `O(log n)`**
9. **For dividing-by-2 loops: `n / 2ᵏ = 1`**
10. **Lower order of growth = generally more efficient**
11. **`n⁶` grows faster than `n⁵`**
12. **Be able to recognize the Big-O, Big-Omega, and Big-Theta figures**
