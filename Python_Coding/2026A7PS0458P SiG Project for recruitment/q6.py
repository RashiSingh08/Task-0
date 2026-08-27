import os
import matplotlib.pyplot as plt
import pandas as pd


def main():
  os.makedirs("plots", exist_ok=True)
  df = pd.read_csv("data/processed_student_performance.csv")

  # 
  plt.figure(figsize=(8, 5))
  plt.bar(df["Student"], df["Final_Score"], color="steelblue", edgecolor="black")
  plt.xlabel("Student Name")
  plt.ylabel("Final Score")
  plt.title("Student Final Scores")
  plt.xticks(rotation=45)
  plt.tight_layout()
  plt.savefig("plots/final_scores.png")
  plt.close()

  # 2. Scatter 'em
  plt.figure(figsize=(8, 5))
  plt.scatter(
      df["Hours_Studied"],
      df["Final_Score"],
      color="forestgreen",
      alpha=0.8,
      edgecolors="k",
  )
  plt.xlabel("Hours_Studied")
  plt.ylabel("Final Score")
  plt.title("Hours_Studied vs. Final Score")
  plt.grid(True, linestyle="--", alpha=0.5)
  plt.tight_layout()
  plt.savefig("plots/study_vs_score.png")
  plt.close()

  # 3. Histogram: Distribution of Final Scores
  plt.figure(figsize=(8, 5))
  plt.hist(
      df["Final_Score"],
      bins=5,
      color="coral",
      edgecolor="black",
      alpha=0.75,
  )
  plt.xlabel("Final Score Range")
  plt.ylabel("Number of Students")
  plt.title("Distribution of Final Scores")
  plt.tight_layout()
  plt.savefig("plots/score_distribution.png")
  plt.close()

  # Custom Plot: Attendance vs Final Score colored by Improvement
  plt.figure(figsize=(8, 5))
  scatter = plt.scatter(
      df["Attendance"],
      df["Final_Score"],
      c=df["Improvement"],
      cmap="coolwarm",
      s=100,
      edgecolors="k",
  )
  cbar = plt.colorbar(scatter)
  cbar.set_label("Score Improvement")
  plt.xlabel("Attendance (%)")
  plt.ylabel("Final Score")
  plt.title("Attendance vs Final Score (Coloring = Improvement)")
  plt.grid(True, linestyle="--", alpha=0.5)
  plt.tight_layout()
  plt.savefig("plots/custom_plot.png")
  plt.close()

#This one was more of copying code after somehow understanding it then coding myself lol...
if __name__ == "__main__":
  main()