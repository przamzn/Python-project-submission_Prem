# Python-project-submission_Prem

The provided code is a Python script that serves as a basic movie recommendation system based on user preferences. Here's an overview of the project:

1. Web Scraping IMDb Data:
The script begins by importing the necessary libraries: requests, BeautifulSoup, and pandas.

It defines a function scrape_movies_by_genre(genre) that scrapes movie data from IMDb based on the selected genre. It constructs the IMDb URL for the specified genre and extracts information such as movie name, release year, runtime, and IMDb rating for each movie on the page.

The scraped data is stored in a pandas DataFrame.

2. Filtering Movies:
The script defines a function filter_movies(movie_df, year, imdb_rating) to filter movies based on the user's input criteria. The user can provide a specific year and a minimum IMDb rating. The function filters the movie DataFrame based on these criteria.

3. User Input and Interaction:
The script then presents a list of movie genres for the user to choose from. The user can select a genre from the list or type 'quit' to exit the script.
After selecting a genre, the script scrapes movie data from IMDb for that genre. If no movies are found for the selected genre, the script displays a message and exits.

4. User Preferences:
The user is prompted to provide additional preferences:
A specific release year (from the list of years available in the scraped data) or 'any' for a random movie.
A minimum IMDb rating or 'any' for a random movie.

5. Movie Recommendations:
Based on the user's input criteria, the script filters the movie data using the filter_movies function. If movies match the user's criteria, their names are displayed. If no movies match the criteria, the script informs the user and asks them to try different inputs.

6. Conclusion:
The script allows users to explore and filter movies from IMDb based on genre, year, and IMDb rating preferences. It offers movie recommendations that meet the specified criteria, making it a basic but functional movie recommendation system. Users can interact with the script until they find movies that match their preferences.

