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
