
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------
# 1. Load the cleaned Netflix dataset
# -----------------------------------------

df = pd.read_csv(
    "../data/processed/netflix_cleaned.csv"
)

print("Netflix Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)


# -----------------------------------------
# 2. Create output folder if it doesn't exist
# -----------------------------------------

output_folder = "../data/processed"
os.makedirs(output_folder, exist_ok=True)


# -----------------------------------------
# 3. Set chart style
# -----------------------------------------

sns.set_theme(style="whitegrid")


# -----------------------------------------
# 4. Chart 1: Movies vs TV Shows
# -----------------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="type"
)

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "movies_vs_tv_shows.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# -----------------------------------------
# 5. Chart 2: Top 10 Release Years
# -----------------------------------------

top_years = (
    df["release_year"]
    .dropna()
    .astype(int)
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 5))

top_years.plot(kind="barh")

plt.title("Top 10 Release Years by Number of Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Release Year")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "top_release_years.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# -----------------------------------------
# 6. Chart 3: Top 10 Content Ratings
# -----------------------------------------

ratings = df["rating"].dropna().astype(str)

top_ratings = (
    ratings[ratings.str.lower() != "unknown"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=top_ratings.values,
    y=top_ratings.index
)

plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
plt.tight_layout()

plt.savefig(
    os.path.join(output_folder, "top_content_ratings.png"),
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# -----------------------------------------
# 7. Print Content Type Summary
# -----------------------------------------

print("\nContent Type Summary:")
print(df["type"].value_counts())


# -----------------------------------------
# 8. Print Dataset Information
# -----------------------------------------

print("\nDataset Information:")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])


# -----------------------------------------
# 9. Print Saved Chart Locations
# -----------------------------------------

print("\nCharts saved successfully!")

print("1. ../data/processed/movies_vs_tv_shows.png")
print("2. ../data/processed/top_release_years.png")
print("3. ../data/processed/top_content_ratings.png")
