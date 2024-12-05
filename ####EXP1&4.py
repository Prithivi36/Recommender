import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df= pd.read_csv("BB.csv")
print(df.isnull().sum())
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['description'].fillna(''))
cosine_sim = cosine_similarity(count_matrix, count_matrix)
def recommend(product_name):
    i = df[df['product'] == product_name].index[0]
    sim = list(enumerate(cosine_sim[i]))
    sim = sorted(sim, key=lambda x: x[1], reverse=True)
    sim = sim[1:11]
    product_indices = [i[0] for i in sim]
    return df['product'].iloc[product_indices]
product_name = "Tea - Stress Relief"
recommendations = recommend(product_name)
print(recommendations)