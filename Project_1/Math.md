| Symbol    | Meaning                                                                       |
| --------- | ----------------------------------------------------------------------------- |
| **rⱼ**    | PageRank score of the **target page j**                                       |
| **rᵢ**    | PageRank score of **page i that links to page j**                             |
| **dᵢ**    | **Out-degree of page i** — number of outgoing hyperlinks from page i          |
| **i → j** | Page i contains a hyperlink **pointing to page j**                            |
| **Σ**     | Adds the PageRank contributions from **all pages linking to j**               |
| **β**     | **Damping factor** — probability of following a hyperlink; here, **β = 0.88** |
| **1 − β** | Probability of making a **random jump**; here, **1 − β = 0.12**               |
| **N**     | Total number of **pages/nodes in the modeled graph**                          |

# PageRank: Iterative Procedure

Given a graph with **N nodes**, PageRank is calculated using an iterative process.

## 1. Initialize PageRank

Each node begins with an equal PageRank value:

**Initial PageRank = 1 / N**

Example with 4 nodes:

**A = B = C = D = 1/4 = 0.25**

---

## 2. Calculate the New PageRank

For each node, calculate its new PageRank using:

**rⱼᵗ⁺¹ = Σᵢ→ⱼ (rᵢᵗ / dᵢ)**

### Symbol Definitions

| Symbol | Meaning |
|---|---|
| **rⱼᵗ⁺¹** | New PageRank of target node **j** |
| **rᵢᵗ** | Current PageRank of node **i** |
| **dᵢ** | Number of outgoing links from node **i** |
| **i → j** | Node **i** has a link pointing to node **j** |
| **Σ** | Add the contributions from all nodes pointing to **j** |
| **t** | Current iteration |
| **t + 1** | Next iteration |

---

## 3. Repeat the Calculation

The newly calculated PageRank values become the inputs for the next iteration.

**Iteration 0 → Iteration 1 → Iteration 2 → ...**

Example:

| Iteration | A | B | C | D |
|---|---:|---:|---:|---:|
| **t = 0** | 0.2500 | 0.2500 | 0.2500 | 0.2500 |
| **t = 1** | New A | New B | New C | New D |
| **t = 2** | New A | New B | New C | New D |
| **...** | ... | ... | ... | ... |

---

## 4. Check for Convergence

After each iteration, compare the new PageRank values with the previous values:

**Σᵢ |rᵢᵗ⁺¹ − rᵢᵗ| < ε**

### What Does This Mean?

1. Find how much each node's PageRank changed.
2. Take the absolute value of each change.
3. Add all of the changes together.
4. Compare the result with the convergence tolerance **ε**.

If:

**Total Change < ε**

→ **PageRank has converged — STOP.**

If:

**Total Change ≥ ε**

→ **PageRank has not converged — REPEAT.**

---

## PageRank Process

**Initialize PageRank**

↓

**Calculate New PageRank**

↓

**Compare New vs. Previous Values**

↓

**Σᵢ |rᵢᵗ⁺¹ − rᵢᵗ| < ε ?**

→ **NO:** Calculate another iteration

→ **YES:** PageRank has converged
