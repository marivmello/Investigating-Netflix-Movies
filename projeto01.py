## Project: Investigating Netflix Movies and Guest Stars in The Office

# Importing
import pandas as pd
import matplotlib.pyplot as plt
netflix_df = pd.read_csv('netflix_data.csv')
colors = pd.read_csv('color_data.csv')
print(netflix_df[:5])

# Filtering
netflix_df_movies_only = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre',
                                                    'release_year', 'duration']]
print(netflix_movies_col_subset[:5])

# Scatter Plot
plt.scatter(netflix_movies_col_subset['release_year'], netflix_movies_col_subset['duration'])
plt.title('Movie Duration by Year of Release')
plt.show()

# Digging deeper
short_movies = netflix_movies_col_subset[netflix_movies_col_subset['duration']< 60]
print(short_movies[:20])

# Marking Films
colors = []
for lab, row in netflix_movies_col_subset.iterrows():
    if row['genre'] == 'Children':
        colors.append('red')
    elif row['genre'] == 'Documentaries':
        colors.append('blue')
    elif row['genre'] == 'Stand-Up':
        colors.append('green')
    else:
        colors.append('black')
print(colors[:10])

# Plotting with color
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

plt.scatter([netflix_movies_col_subset['release_year']],
            [netflix_movies_col_subset['duration']], c= colors)
plt.title('Movie duration by year of release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')

plt.show()

# The final Question
are_movies_getting_shorter = 'no'
print('Are movies getting shorter? ' + are_movies_getting_shorter.capitalize())
