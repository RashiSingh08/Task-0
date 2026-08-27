"""Q5: Pandas tabular analysis on student performance dataset."""

import os
import pandas as pd

#This is the first time I am using pandas, to tell the truth. So, ended up spending wayy too much time
# on this and 6th one...
def main():
  # Load CSV into DataFrame
  df = pd.read_csv("data/student_performance.csv")

  print("First 5 rows:")
  print(df.head())

  print("\nShape (Rows, Cols):", df.shape)

  # Display column names
  print("\nColumns:", df.columns.tolist())

  # Check missing values
  print("\nMissing Values:")
  print(df.isnull().sum())


  print("\nAverage Final Score:", df["Final_Score"].mean())


  top_idx = df["Final_Score"].idxmax()
  print(
      f"\nHighest Scorer: {df.loc[top_idx, 'Student']} ({df.loc[top_idx, 'Final_Score']})"
  )

  df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

  print("\nStudents with Attendance >= 80%:")
  print(df[df["Attendance"] >= 80])

  df_sorted = df.sort_values(by="Final_Score", ascending=False)

 #This was bone grinding. Like, some were there in numpy arrays too but some of these were pretty new...
  os.makedirs("data", exist_ok=True)
  df_sorted.to_csv("data/processed_student_performance.csv", index=False)
  print(
      "\nSaved processed output to 'data/processed_student_performance.csv'."
  )


if __name__ == "__main__":
  main()