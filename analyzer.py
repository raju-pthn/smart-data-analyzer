import pandas as pd
import sys

def analyze_file(file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    summary = {}

    summary["Total Rows"] = len(df)
    summary["Total Columns"] = len(df.columns)
    summary["Duplicate Rows"] = df.duplicated().sum()

    missing = df.isnull().sum()
    summary["Missing Values"] = missing.to_dict()

    numeric_stats = df.describe()

    with open("data_summary.txt", "w") as f:
        f.write("DATA ANALYSIS REPORT\n")
        f.write("====================\n\n")
        for k, v in summary.items():
            f.write(f"{k}: {v}\n")

    print("Analysis completed successfully.")
    print("Summary saved as: data_summary.txt")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <file_path>")
    else:
        analyze_file(sys.argv[1])
