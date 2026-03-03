import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PART B: STRONG SCALING DATA (200x200)
# ==========================================
# Enter your "total time" results here for 1, 2, 4, 8, 16 threads
threads_b = [1, 2, 4, 8, 16]
times_b = [0.01685549, 0.00826442, 0.00480723, 0.02179815, 0.00899833]  

# ==========================================
# PART C: WEAK SCALING DATA
# ==========================================
# 1. Baseline: 1 thread for each matrix size
# Order: 100x100, 200x200, 400x400, 800x800, 1600x1600
baseline_1_thread = [0.00221024, 0.01691866, 0.22015491, 1.19720043, 8.98249211] # REPLACE WITH YOUR DATA

# 2. Parallel: Threads/Size variation
# Order: 2/200, 4/400, 8/800, 16/1600
parallel_multi_thread = [0.00876162, 0.10838224, 0.23047732, 1.26450440]    

# ------------------------------------------
# Plotting Part B: Strong Scaling
# ------------------------------------------
plt.figure(figsize=(10, 6))
t1_b = times_b[0]
labels_b = ["1"] + [f"{t}\n({t1_b/times_b[i]:.2f}x)" for i, t in enumerate(threads_b) if i > 0]

plt.bar(labels_b, times_b, color='skyblue', edgecolor='navy')
plt.xlabel("Number of Threads (Speedup in Parens)")
plt.ylabel("Total Time (sec)")
plt.title("Strong Scaling: Constant Matrix Size (200x200)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("strong_scaling.png")

# ------------------------------------------
# Plotting Part C: Weak Scaling
# ------------------------------------------
plt.figure(figsize=(12, 7))
x_labels_c = ["1/100"]
# Mapping the labels for the multi-bar entries
sizes = [200, 400, 800, 1600]
threads_c = [2, 4, 8, 16]

for i in range(len(parallel_multi_thread)):
    speedup = baseline_1_thread[i+1] / parallel_multi_thread[i]
    x_labels_c.append(f"{threads_c[i]}/{sizes[i]}\n({speedup:.2f}x)")

x = np.arange(len(x_labels_c))
width = 0.35

plt.bar(x[0], baseline_1_thread[0], width, color='green', label='1 Thread')


for i in range(1, len(x_labels_c)):
    plt.bar(x[i] - width/2, baseline_1_thread[i], width, color='green')
    # Red bar for P threads at that size
    plt.bar(x[i] + width/2, parallel_multi_thread[i-1], width, color='red')

# Custom legend handling to avoid duplicates
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='green', lw=4, label='1 Thread'),
                   Line2D([0], [0], color='red', lw=4, label='P Threads')]

plt.xticks(x, x_labels_c)
plt.ylabel("Total Time (sec)")
plt.title("Weak Scaling: Varying Threads and Matrix Size")
plt.legend(handles=legend_elements)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig("weak_scaling.png")

print("Graphs generated: strong_scaling.png and weak_scaling.png")
plt.show()