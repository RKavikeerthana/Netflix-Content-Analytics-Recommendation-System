
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("../data/processed/netflix_cleaned.csv")

# 1. Dataset overview
print("Dataset shape:", df.shape)

# 2. Movies vs TV Shows
print("\nContent Type Counts:")
print(df["type"].value_counts())

# 3. Content type percentages
print("\nContent Type Percentages:")
print((df["type"].value_counts(normalize=True) * 100).round(2))

# 4. Top 10 release years
print("\nTop 10 Release Years:")
print(df["release_year"].value_counts().head(10))

# 5. Top 10 countries
countries = (
    df.loc[df["country"] != "Unknown", "country"]
    .str.split(", ")
    .explode()
    .str.strip()
)

print("\nTop 10 Countries:")
print(countries.value_counts().head(10))

# 6. Top 10 genres
genres = df["listed_in"].str.split(", ").explode()

print("\nTop 10 Genres:")
print(genres.value_counts().head(10))

# 7. Movies vs TV Shows chart
sns.countplot(data=df, x="type")
plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# 8. Top genres chart
top_genres = genres.value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_genres.values, y=top_genres.index)
plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
