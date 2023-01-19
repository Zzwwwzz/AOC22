with open("i/1.txt", "r") as f:
    weights = [sum([int(i) for i in nums.split("\n")]) for nums in f.read().split("\n\n")]

print(f"Solution 1: {max(weights)}")
print(f"Solution 2: {sum(sorted(weights)[-3:])}")