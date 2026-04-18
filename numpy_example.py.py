import numpy as np

# Data array
data = np.array([23, 45, 12, 67, 34, 89, 15])

# Calculate statistics
mean_val = np.mean(data)
median_val = np.median(data)
std_val = np.std(data)

# Display results nicely
print("Data:", data)
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")