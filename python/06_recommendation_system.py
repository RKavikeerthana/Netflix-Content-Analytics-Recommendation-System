
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Load dataset
df = pd.read_csv("../data/processed/netflix_cleaned.csv")

# 2. Handle missing values
for column in ["title", "listed_in", "description", "type"]:
    df[column] = df[column].fillna("").astype(str)

# 3. Give genres more importance than descriptions
df["content"] = (
    (df["listed_in"] + " ") * 3
    + df["description"]
    + " "
    + df["type"]
)

# 4. Convert text into numerical features
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["content"])

# 5. Calculate similarity
similarity_matrix = cosine_similarity(tfidf_matrix)


# 6. Recommendation function
def recommend_titles(title, number=5):

    matches = df[
        df["title"].str.casefold() == title.strip().casefold()
    ]

    if matches.empty:
        print("Title not found in the Netflix dataset.")
        return

    index = matches.index[0]
    selected_title = df.iloc[index]["title"]

    scores = list(enumerate(similarity_matrix[index]))
    scores.sort(key=lambda item: item[1], reverse=True)

    recommendations = []

    for i, score in scores:
        if i == index:
            continue

        if df.iloc[i]["title"].casefold() == selected_title.casefold():
            continue

        item = df.iloc[i]

        recommendations.append({
            "Selected Title": selected_title,
            "Recommended Title": item["title"],
            "Type": item["type"],
            "Genre": item["listed_in"],
            "Similarity": round(float(score), 3)
        })

        if len(recommendations) == number:
            break

    # 7. Save recommendations to CSV
    output_file = "../data/processed/recommendations.csv"

    recommendations_df = pd.DataFrame(recommendations)
    recommendations_df.to_csv(output_file, index=False)

    # 8. Display recommendations
    print(f"\nRecommendations for: {selected_title}")
    print("-" * 50)

    for rank, item in enumerate(recommendations, start=1):
        print(f"{rank}. {item['Recommended Title']}")
        print(f"   Type: {item['Type']}")
        print(f"   Genre: {item['Genre']}")
        print(f"   Similarity: {item['Similarity']}")
        print()

    print(f"CSV file saved successfully: {output_file}")


# 9. Get user input
print("NETFLIX CONTENT RECOMMENDATION SYSTEM")
print("=" * 40)

user_title = input("Enter a Netflix title: ")
recommend_titles(user_title)
