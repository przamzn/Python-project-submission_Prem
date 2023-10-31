import requests as r
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape movie data from IMDb based on genre
def scrape_movies_by_genre(genre):
    imdb_url = f'https://www.imdb.com/search/title/?genres={genre}&explore=genres&title_type=feature&ref_=ft_movie_0'
    response = r.get(imdb_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        movies = soup.find_all("div", class_='lister-item mode-advanced')
        movie_data = []

        for movie in movies:
            name = movie.find('h3', class_="lister-item-header").a.get_text()
            try:
                year = int(''.join(filter(str.isdigit, movie.find('h3', class_="lister-item-header")
                                         .find(class_="lister-item-year text-muted unbold").get_text())))
            except:
                year = None

            try:
                run_time = int(''.join(filter(str.isdigit, movie.find_all('p')[0].find_all('span')[2].get_text().strip())))
            except:
                run_time = 0

            try:
                rating = float(movie.find('div', class_='inline-block ratings-imdb-rating').get_text())
            except:
                rating = None

            movie_data.append({'Name': name, 'Year': year, 'IMDbRating': rating})

        return pd.DataFrame(movie_data)
    else:
        print("Failed to retrieve data from IMDb.")
        return pd.DataFrame()

# Function to filter movies by year and IMDb rating
def filter_movies(movie_df, year, imdb_rating):
    filtered_df = movie_df

    if year.lower() != 'any':
        filtered_df = filtered_df[filtered_df['Year'] == int(year)]

    if imdb_rating.lower() != 'any':
        imdb_rating = float(imdb_rating)
        filtered_df = filtered_df[filtered_df['IMDbRating'] >= imdb_rating]

    return filtered_df

# Get user input for genre
gen_list = ['action', 'adventure', 'animation', 'biography', 'comedy', 'crime', 'documentary', 'drama', 'family',
            'fantasy', 'film-noir', 'history', 'horror', 'music', 'musical', 'mystery', 'romance', 'sci-fi', 'short',
            'sport', 'thriller', 'war', 'western']

while True:
    print("Please select a genre from the list or type 'quit':\n", '\n'.join(gen_list))
    genre = input().lower()
    if genre in gen_list:
        break
    elif genre == 'quit':
        exit()
    else:
        print("Please provide a genre from the list or type 'quit'. Thank you.")

# Scrape movie data based on the selected genre
movie_data = scrape_movies_by_genre(genre)

if movie_data.empty:
    print("No movies found for the selected genre.")
    exit()

# Filter movies based on user input for year and IMDb rating
while True:
    user_year = input(f"Please select a year from the list {movie_data['Year'].unique()} or type 'any' for a random movie:\n")
    user_imdb_rating = input("Please provide the minimum IMDb rating or type 'any' for a random movie:\n")

    filtered_movies = filter_movies(movie_data, user_year, user_imdb_rating)

    if filtered_movies.empty:
        print("No movies found based on the provided criteria. Please try different inputs.")
    else:
        print("\n".join(filtered_movies['Name']))
        break
