from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
df = pd.read_csv(ROOT / "data" / "student_study_hours.csv")
values = df["Study_Hours"]
out = ROOT / "outputs"
out.mkdir(exist_ok=True)

plt.figure(figsize=(9, 5))
plt.hist(values, bins=8, edgecolor="black")
plt.title("Distribution of Student Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig(out / "study_hours_histogram.png", dpi=160)
plt.close()

print("DISTRIBUTION ANALYSIS — OBSERVATIONS")
print(f"Number of observations: {len(values)}")
print(f"Mean: {values.mean():.2f} hours")
print(f"Median: {values.median():.2f} hours")
print(f"Minimum: {values.min():.1f} hours")
print(f"Maximum: {values.max():.1f} hours")
print("1. Most values are concentrated in the lower-to-middle range.")
print("2. Values range from 1 to 20 hours, showing a wide spread.")
print("3. A few high values extend the right tail, suggesting positive (right) skew.")
print("Note: This is illustrative sample data, not real student data.")
