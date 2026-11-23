
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("../data/processed/netflix_cleaned.csv")

# Group titles by release year and type
yearly_content = (
    df.groupby(["release_year", "type"])
    .size()
    .reset_index(name="title_count")
)

# Focus on 2010 onwards
yearly_content = yearly_content[
    yearly_content["release_year"] >= 2010
]

# Display the 10 years with the most titles
print("Content trends by release year:")
print(
    yearly_content.groupby("release_year")["title_count"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Visualize the trend
plt.figure(figsize=(12, 6))

sns.lineplot(
    data=yearly_content,
    x="release_year",
    y="title_count",
    hue="type",
    marker="o"
)

plt.title("Netflix Titles by Release Year and Type")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
