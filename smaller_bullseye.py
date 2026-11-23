import random
import math

def simulate_bullseye(total_arrows):
    hits = 0
    radius = 0.5

    for i in range(total_arrows):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= radius**2:
            hits += 1

    probability = hits / total_arrows
    estimated_pi = 4 * probability / radius**2

    return hits, probability, estimated_pi


total_arrows = 100000

hits, probability, estimated_pi = simulate_bullseye(total_arrows)

print("Smaller Bullseye Simulation")
print("-------------------------")
print("Target radius:", 0.5)
print("Total arrows:", total_arrows)
print("Hits:", hits)
print("Estimated hit probability:", probability)
print("Estimated Pi:", estimated_pi)
print("Actual Pi:", math.pi)
