
import pandas as pd

df = pd.read_csv("../data/raw/netflix_titles.csv")

# Convert dates using the expected format
df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Count dates that could not be converted
invalid_dates = df[
    df["date_added"].notna()
    & df["date_added_converted"].isna()
]

print("Original missing dates:", df["date_added"].isna().sum())
print("Invalid date formats:", len(invalid_dates))

print("\nExamples of invalid dates:")
print(invalid_dates["date_added"].head(10))

print("\nTotal unconvertible dates:",
      df["date_added_converted"].isna().sum())
