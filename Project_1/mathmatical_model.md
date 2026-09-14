``` python
import sys
import time
import networkx as nx
from networkx.exception import NetworkXError


def pagerank(G, alpha=0.85, personalization=None,
             max_iter=100, tol=1.0e-6, nstart=None,
             weight='weight', dangling=None):
    """
    Return the PageRank of the nodes in the graph.

    PageRank computes a ranking of the nodes in the graph G based on
    the structure of the incoming links.
    """

    if len(G) == 0:
        return {}

    if not G.is_directed():
        D = G.to_directed()
    else:
        D = G

    # Create a copy in stochastic form
    W = nx.stochastic_graph(D, weight=weight)

    N = W.number_of_nodes()

    # Choose starting vector
    if nstart is None:
        x = dict.fromkeys(W, 1.0 / N)
    else:
        s = float(sum(nstart.values()))
        x = dict((k, v / s) for k, v in nstart.items())

    # Personalization vector
    if personalization is None:
        p = dict.fromkeys(W, 1.0 / N)

    else:
        missing = set(G) - set(personalization)

        if missing:
            raise NetworkXError(
                "Personalization dictionary must have a value "
                f"for every node. Missing nodes {missing}"
            )

        s = float(sum(personalization.values()))

        p = dict(
            (k, v / s)
            for k, v in personalization.items()
        )

    # Dangling node weights
    if dangling is None:
        dangling_weights = p

    else:
        missing = set(G) - set(dangling)

        if missing:
            raise NetworkXError(
                "Dangling node dictionary must have a value "
                f"for every node. Missing nodes {missing}"
            )

        s = float(sum(dangling.values()))

        dangling_weights = dict(
            (k, v / s)
            for k, v in dangling.items()
        )

    dangling_nodes = [
        n
        for n in W
        if W.out_degree(n, weight=weight) == 0.0
    ]

    # Power iteration
    for _ in range(max_iter):

        xlast = x

        x = dict.fromkeys(
            xlast.keys(),
            0
        )

        danglesum = alpha * sum(
            xlast[n]
            for n in dangling_nodes
        )

        for n in x:

            # Left matrix multiplication
            for nbr in W[n]:

                x[nbr] += (
                    alpha
                    * xlast[n]
                    * W[n][nbr][weight]
                )

            x[n] += (
                danglesum * dangling_weights[n]
                + (1.0 - alpha) * p[n]
            )

        # Check convergence
        err = sum(
            abs(x[n] - xlast[n])
            for n in x
        )

        if err < N * tol:
            return x

    raise NetworkXError(
        "pagerank: power iteration failed to converge "
        f"in {max_iter} iterations."
    )


if __name__ == "__main__":

    # Make sure a graph size was provided
    if len(sys.argv) != 2:

        print(
            "Usage: python pagerank_test.py <number_of_nodes>",
            file=sys.stderr
        )

        sys.exit(1)

    # Read graph size from command line
    n = int(sys.argv[1])

    # Need at least 2 nodes for this test
    if n < 2:

        print(
            "Number of nodes must be at least 2.",
            file=sys.stderr
        )

        sys.exit(1)

    # Barabasi-Albert requires:
    # 1 <= m < n
    m = min(10, n - 1)

    # Generate graph
    G = nx.barabasi_albert_graph(
        n,
        m,
        seed=42
    )

    # Start timer
    start = time.perf_counter()

    # Run PageRank
    pagerank(
        G,
        alpha=0.4
    )

    # Stop timer
    end = time.perf_counter()

    # IMPORTANT:
    # Print ONLY the runtime so benchmark.py
    # can convert this directly into a float.
    print(end - start)
```

## Math Model - 

| Symbol            | Meaning                              | Simple interpretation               |
| ----------------- | ------------------------------------ | ----------------------------------- |
| \(v\)             | The page we're calculating           | "What is **this page's** rank?"     |
| \(w\)             | A page linking to \(v\)              | A page **giving rank** to \(v\)     |
| \(t\)             | Current iteration                    | Which round we're on                |
| \(t-1\)           | Previous iteration                   | The last round                      |
| \(\pi_v^{(t)}\)   | PageRank of \(v\) at iteration \(t\) | **New rank of \(v\)**               |
| \(\pi_w^{(t-1)}\) | Previous PageRank of page \(w\)      | How much rank \(w\) had last round  |
| \(d_w\)           | Out-degree of \(w\)                  | Number of pages \(w\) links to      |
| \(E\)             | Set of edges/links                   | All links in the graph              |
| \((w,v)\in E\)    | There is a link \(w\rightarrow v\)   | \(w\) points to \(v\)               |
| \(\sum\)          | Sum                                  | Add all incoming contributions      |
| \(\epsilon\)      | Reset/teleport probability           | Chance of randomly jumping          |
| \(1-\epsilon\)    | Follow-link probability              | Chance of actually following a link |
| \(N\)             | Total number of pages                | Size of the graph                   |

