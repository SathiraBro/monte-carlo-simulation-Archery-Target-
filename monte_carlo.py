import random
import statistics
import csv
import math

# Monte Carlo simulation to estimate the value of Pi using archery analogy
def simulate_archery(total_arrows):
    hits = 0

    for i in range(total_arrows):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            hits += 1

    probability = hits / total_arrows
    estimated_pi = 4 * probability

    return hits, probability, estimated_pi


sample_sizes = [1000, 10000, 100000, 1000000]

# Save results to CSV file
with open("monte_carlo_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "N",
        "Repetition",
        "Hits",
        "Hit Probability",
        "Estimated Pi",
        "Actual Pi"
    ])
    for n in sample_sizes:
        for repetition in range(1, 11):
            hits, probability, pi = simulate_archery(n)

            writer.writerow([
                n,
                repetition,
                hits,
                probability,
                pi,
                math.pi
            ])

print("Results saved successfully.")   


# Print results to console 
for n in sample_sizes:
    pi_results = []
    print("\nSample size:", n)


    for repetition in range(1, 11):
        hits, probability, pi = simulate_archery(n)
        pi_results.append(pi)

        print(
            "Run:", repetition,
            "Hits:", hits,
            "Estimated Pi:", pi
        )
    
    mean_pi = statistics.mean(pi_results)

    print("\nMean Pi:", mean_pi)