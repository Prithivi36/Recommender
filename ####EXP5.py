import pandas as pd
import matplotlib.pyplot as plt

column_names = ['user_id', 'item_id', 'rating', 'timestamp']
path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
df = pd.read_csv(path, sep='\t', names=column_names)
print(df.head())
movie_titles_path = 'https://media.geeksforgeeks.org/wp-content/uploads/Movie_Id_Titles.csv'
movie_titles = pd.read_csv(movie_titles_path)
data = pd.merge(df, movie_titles, on='item_id')

average_ratings = data.groupby('title')['rating'].mean().sort_values(ascending=False)
rating_counts = data.groupby('title')['rating'].count().sort_values(ascending=False)

ratings = pd.DataFrame(average_ratings)
ratings['num of ratings'] = rating_counts

ratings['num of ratings'].hist(bins=70)
plt.title('Distribution of Number of Ratings')
plt.show()
ratings['rating'].hist(bins=70)
plt.title('Distribution of Average Ratings')
plt.show()


moviemat = data.pivot_table(index='user_id', columns='title', values='rating')
starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)
corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
top_starwars_corr = corr_starwars.sort_values('Correlation', ascending=False).head(10)
print(top_starwars_corr)