import subprocess
import matplotlib.pyplot as plt
import numpy as np


# Graph sizes to test
sizes = np.array([
    50,
    100,
    200,
    400,
    800,
    1200,
    1600,
    2000
])


# Number of times to run each graph size
runs_per_size = 10


best_times = []
average_times = []
worst_times = []


for n in sizes:

    runtimes = []

    print(f"\nTesting n = {n}")

    for run in range(runs_per_size):

        result = subprocess.run(
            ["python", "pagerank_test.py", str(n)],
            capture_output=True,
            text=True
        )

        # Check if subprocess failed
        if result.returncode != 0:
            print("Error running PageRank:")
            print(result.stderr)
            continue

        runtime = float(result.stdout.strip())

        runtimes.append(runtime)

        print(
            f"Run {run + 1:2d}: "
            f"{runtime:.6f} seconds"
        )

    # Calculate experimental results
    best = min(runtimes)
    average = sum(runtimes) / len(runtimes)
    worst = max(runtimes)

    best_times.append(best)
    average_times.append(average)
    worst_times.append(worst)

    print(
        f"n = {n:4d} | "
        f"Best = {best:.6f} | "
        f"Average = {average:.6f} | "
        f"Worst = {worst:.6f}"
    )


# Convert lists to NumPy arrays
best_times = np.array(best_times)
average_times = np.array(average_times)
worst_times = np.array(worst_times)


# ----------------------------------------------------
# THEORETICAL BOUNDS
# ----------------------------------------------------

# For this experiment:
#
# PageRank ≈ Θ(I(V + E))
#
# Barabasi-Albert with fixed m:
#
# E = Θ(V)
#
# Therefore:
#
# Lower bound:
# Ω(V)
#
# Upper bound:
# O(max_iter * V)
#
# Since max_iter = 100 is constant:
#
# O(100V) -> O(V)
#
# Both therefore have linear growth.


# Lower-bound growth function
lower_bound = sizes.astype(float)


# Upper-bound growth function
max_iter = 100
upper_bound = max_iter * sizes.astype(float)


# ----------------------------------------------------
# NORMALIZE THE THEORETICAL CURVES
#
# Complexity curves describe GROWTH, not seconds.
# We scale them so they can be visually compared
# with the measured runtimes.
# ----------------------------------------------------

lower_bound_scaled = (
    lower_bound
    * (best_times[-1] / lower_bound[-1])
)

upper_bound_scaled = (
    upper_bound
    * (worst_times[-1] / upper_bound[-1])
)


# ----------------------------------------------------
# GRAPH
# ----------------------------------------------------

plt.figure(figsize=(10, 6))


# Experimental measurements
plt.plot(
    sizes,
    best_times,
    marker="o",
    label="Best Observed Runtime"
)

plt.plot(
    sizes,
    average_times,
    marker="o",
    label="Average Runtime"
)

plt.plot(
    sizes,
    worst_times,
    marker="o",
    label="Worst Observed Runtime"
)


# Theoretical bounds
plt.plot(
    sizes,
    lower_bound_scaled,
    linestyle="--",
    label="Lower Bound Ω(V)"
)

plt.plot(
    sizes,
    upper_bound_scaled,
    linestyle="--",
    label="Upper Bound O(max_iter × V)"
)


plt.xlabel("Number of Nodes (V)")
plt.ylabel("Execution Time (seconds)")

plt.title(
    "PageRank Runtime Analysis\n"
    "Best, Average, Worst, Upper and Lower Bounds"
)

plt.legend()

plt.grid()

plt.tight_layout()

plt.show()
(bigO-env) taraf@WALL-E:~$ cat pagerank_test.py
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
