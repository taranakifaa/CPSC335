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
