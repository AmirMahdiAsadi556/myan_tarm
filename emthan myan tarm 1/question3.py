import random
import itertools

numbers = [random.randint(1, 15) for _ in range(20)]
print("Generated numbers:", numbers)

valid_subsets = []
minimal_size = None

for r in range(1, len(numbers) + 1):
    current_subsets = []

    for subset in itertools.combinations(numbers, r):
        subset_sum = sum(subset)
        if 50 <= subset_sum <= 52:
            current_subsets.append(subset)
    
    if current_subsets:
        valid_subsets = current_subsets
        minimal_size = r
        break

if valid_subsets:
    print(f"\nMinimal subset size: {minimal_size}")
    print(f"Found {len(valid_subsets)} subsets with sum 50-52:")
    for subset in valid_subsets:
        print(f"{subset} -> Sum: {sum(subset)}")
else:
    print("\nNo subsets found in the range 50-52.")