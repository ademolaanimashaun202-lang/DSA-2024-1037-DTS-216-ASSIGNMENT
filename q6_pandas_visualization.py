"""
DTS 216 - Question 6: String Manipulation & Visualization
a. Use Pandas string functions to:
   - Convert all names to lowercase.
   - Extract domain names from email addresses.
b. Plot:
   - Line plot of student marks over time.
   - Histogram of marks distribution.
   - Scatter plot comparing math vs science scores.
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # non-interactive backend for saving figures
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Sample dataset
# ---------------------------------------------------------------
data = {
    "Name": ["Chinedu OKORO", "Amaka Johnson", "Bello Yusuf", "Grace Adeyemi", "Musa Ibrahim"],
    "Email": ["chinedu.okoro@gmail.com", "amaka.johnson@yahoo.com",
              "bello.yusuf@unn.edu.ng", "grace.adeyemi@outlook.com",
              "musa.ibrahim@gmail.com"],
    "Math": [78, 65, 90, 55, 82],
    "Science": [74, 70, 85, 60, 79],
    "Test1": [60, 55, 80, 45, 70],
    "Test2": [70, 60, 85, 50, 75],
    "Test3": [75, 68, 90, 58, 80],
}
df = pd.DataFrame(data)
print("=== Original DataFrame ===")
print(df[["Name", "Email"]])

# ---------------------------------------------------------------
# (a) Pandas string functions
# ---------------------------------------------------------------
print("\n=== (a) Names converted to lowercase ===")
df["Name_lower"] = df["Name"].str.lower()
print(df[["Name", "Name_lower"]])

print("\n=== (a) Domain names extracted from emails ===")
df["Email_domain"] = df["Email"].str.split("@").str[1]
print(df[["Email", "Email_domain"]])

# ---------------------------------------------------------------
# (b) Visualizations
# ---------------------------------------------------------------
# Line plot: marks over time (Test1 -> Test2 -> Test3) for each student
plt.figure(figsize=(8, 5))
for i in range(len(df)):
    plt.plot(["Test 1", "Test 2", "Test 3"],
              df.loc[i, ["Test1", "Test2", "Test3"]],
              marker="o", label=df.loc[i, "Name"])
plt.title("Student Marks Over Time")
plt.xlabel("Test")
plt.ylabel("Marks")
plt.legend()
plt.tight_layout()
plt.savefig("line_plot_marks_over_time.png", dpi=150)
plt.close()

# Histogram: distribution of Math marks
plt.figure(figsize=(8, 5))
plt.hist(df["Math"], bins=5, color="steelblue", edgecolor="black")
plt.title("Histogram of Math Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_marks_distribution.png", dpi=150)
plt.close()

# Scatter plot: Math vs Science
plt.figure(figsize=(8, 5))
plt.scatter(df["Math"], df["Science"], color="darkorange")
plt.title("Scatter Plot: Math vs Science Scores")
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.tight_layout()
plt.savefig("scatter_math_vs_science.png", dpi=150)
plt.close()

print("\nAll plots saved: line_plot_marks_over_time.png, "
      "histogram_marks_distribution.png, scatter_math_vs_science.png")
