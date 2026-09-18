beta = 0.88
N = 4
tolerance = 1e-6

# Iteration 0: initialize every node to 1/N
A = B = C = D = 1 / N

iteration = 0

print("ITERATION 0")
print(f"A = {A:.6f}")
print(f"B = {B:.6f}")
print(f"C = {C:.6f}")
print(f"D = {D:.6f}")

while True:

    # -----------------------------
    # Calculate next PageRank values
    # -----------------------------

    # A receives links from B, C, and D.
    # A is dangling, so A/N is also redistributed.
    new_A = beta * (
        B + C + D + (A / N)
    ) + (1 - beta) * (1 / N)

    # B, C, and D have no incoming links.
    # They receive A's dangling contribution
    # plus the random-jump contribution.
    new_B = beta * (A / N) + (1 - beta) * (1 / N)
    new_C = beta * (A / N) + (1 - beta) * (1 / N)
    new_D = beta * (A / N) + (1 - beta) * (1 / N)

    # -----------------------------
    # Convergence condition
    # Σ |r_i^(t+1) - r_i^t|
    # -----------------------------

    error = (
        abs(new_A - A)
        + abs(new_B - B)
        + abs(new_C - C)
        + abs(new_D - D)
    )

    iteration += 1

    # Show the mathematical substitution
    print(f"\nITERATION {iteration}")

    print(
        f"A = 0.88({B:.6f} + {C:.6f} + {D:.6f}"
        f" + {A:.6f}/4) + 0.12(1/4)"
    )
    print(f"A = {new_A:.6f}")

    print(
        f"B = 0.88({A:.6f}/4) + 0.12(1/4)"
    )
    print(f"B = {new_B:.6f}")

    print(f"C = {new_C:.6f}")
    print(f"D = {new_D:.6f}")

    print(f"Convergence Error = {error:.8f}")

    # -----------------------------
    # Check convergence
    # -----------------------------

    if error < tolerance:
        print("\nCONVERGENCE MET")
        break

    # Feed new answers back into equation
    A = new_A
    B = new_B
    C = new_C
    D = new_D


print("\nFINAL PAGERANK")
print(f"A = {new_A:.8f}")
print(f"B = {new_B:.8f}")
print(f"C = {new_C:.8f}")
print(f"D = {new_D:.8f}")
