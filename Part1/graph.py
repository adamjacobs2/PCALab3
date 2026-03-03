import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# PART B: STRONG SCALING DATA (200x200)
# ==========================================


threads_b = [1, 2, 4, 8, 16]
times_b = [0.02226862 , 0.01684834, 0.01256594, 0.01954635, 0.02149954]  

# ==========================================
# PART C: WEAK SCALING DATA
# ==========================================

# Order: 100x100, 200x200, 400x400, 800x800, 1600x1600
baseline_1_thread = [0.00309336, 0.02013800, 0.16376167, 1.41104031, 13.56628901] 

# 2. Parallel: Threads/Size variation
# Order: 2/200, 4/400, 8/800, 16/1600
parallel_multi_thread = [0.01157178, 0.02782149, 0.33469499, 0.70956491]    

# ------------------------------------------
# Plotting Part B: Strong Scaling
# ------------------------------------------
plt.figure(figsize=(10, 6))
t1_b = times_b[0]
labels_b = ["1"] + [f"{t}\n({t1_b/times_b[i]:.2f}x)" for i, t in enumerate(threads_b) if i > 0]

plt.bar(labels_b, times_b, color='skyblue', edgecolor='navy')
plt.xlabel("Number of Threads (Speedup)")
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