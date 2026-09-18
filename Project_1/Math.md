| Symbol             | Meaning                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------- |
| \(r_j\)            | PageRank score of the **target page \(j\)**                                              |
| \(r_i\)            | PageRank score of a **page \(i\) that links to \(j\)**                                   |
| \(d_i\)            | **Out-degree of page \(i\)** — number of outgoing hyperlinks from page \(i\)             |
| \(i\rightarrow j\) | Page \(i\) contains a hyperlink **pointing to page \(j\)**                               |
| \(\sum\)           | Adds the PageRank contributions from **all pages linking to \(j\)**                      |
| \(\beta\)          | **Damping factor** — probability of following a hyperlink; here, \(\beta=0.88\)          |
| \(1-\beta\)        | Probability of making a **random jump** instead of following a hyperlink; here, \(0.12\) |
| \(N\)              | Total number of **pages/nodes in the modeled graph**                                     |
