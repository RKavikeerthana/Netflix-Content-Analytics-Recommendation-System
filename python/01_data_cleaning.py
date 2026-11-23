
import pandas as pd
import numpy as np

# 1. Load the original dataset
df = pd.read_csv("../data/raw/netflix_titles.csv")

print("Original dataset shape:", df.shape)

# 2. Remove duplicate records
df = df.drop_duplicates()
# Remove the incorrectly arranged row
df = df[df["type"].isin(["Movie", "TV Show"])]
print("After removing duplicates:", df.shape)

# 3. Check the type column
print("\nContent types:")
print(df["type"].value_counts(dropna=False))

# 4. Check rating values
valid_ratings = [
    "G", "PG", "PG-13", "R", "NC-17", "NR", "UR",
    "TV-G", "TV-PG", "TV-14", "TV-MA",
    "TV-Y", "TV-Y7", "TV-Y7-FV"
]

# Find suspicious ratings before cleaning
bad_ratings = df[
    df["rating"].notna()
    & ~df["rating"].isin(valid_ratings)
]

print("\nSuspicious rating values:")
if bad_ratings.empty:
    print("No suspicious ratings found.")
else:
    print(
        bad_ratings[
            ["show_id", "title", "rating", "duration"]
        ].to_string(index=False)
    )

# 5. Correct ratings only when they are clearly durations
# Do not delete records or guess missing ratings.
duration_pattern = r"^\s*\d+\s*(min|mins|minute|minutes)\s*$"

wrong_rating = (
    df["rating"].notna()
    & df["rating"].astype(str).str.match(
        duration_pattern, case=False
    )
)

# Move a duration into duration only if that field is empty
duration_empty = (
    df["duration"].isna()
    | df["duration"].astype(str).str.strip().eq("")
)

can_repair = wrong_rating & duration_empty

df.loc[can_repair, "duration"] = df.loc[can_repair, "rating"]
df.loc[can_repair, "rating"] = np.nan

print("\nRows repaired:", int(can_repair.sum()))

# 6. Fill missing text values
text_columns = [
    "director",
    "cast",
    "country",
    "rating",
    "duration",
    "listed_in",
    "description"
]

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

# 7. Clean the type column
df["type"] = df["type"].fillna("Unknown").astype(str).str.strip()

# 8. Convert date_added to datetime
df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)

# 9. Check the cleaned dataset
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFinal dataset shape:", df.shape)

print("\nFinal content types:")
print(df["type"].value_counts(dropna=False))

print("\nFinal rating values:")
print(df["rating"].value_counts(dropna=False))

# 10. Save the cleaned dataset
output_path = "../data/processed/netflix_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File:", output_path)
