import spacy

nlp = spacy.load('en_core_web_md')


class Movie:
    def __init__(self, title, description):
        self.title = title
        self.description = description


def find_next_movie(current_movie, available_movies):
    """Given the title of current movie and a list of potential next movies, returns a recommended next movie."""

    # Create a model of current movie.
    current_model = nlp(current_movie.description)

    # Loop through movie descriptions modelling each one to find highest match.
    # Create variables for the highest similarity and the corresponding movie title.
    highest_similarity = 0
    most_similar_movie = ""

    # Loop through the available movies, modelling each one and comparing similarity
    # score with the existing highest score.
    for movie in available_movies:
        movie_model = nlp(movie.description)
        current_similarity = current_model.similarity(movie_model)

        # Compare the current similarity score against the highest so far.
        # If it's higher, it replaces the highest so far.
        if current_similarity > highest_similarity:
            highest_similarity = current_similarity

            # We also then update the title of the most similar movie to the title
            # of the current movie.
            most_similar_movie = movie.title

    return most_similar_movie


# Create a Movie object to hold the Planet Hulk details.
hulk_movie = Movie("Planet Hulk", "Will he save their world or destroy it? When the"
                                  " Hulk becomes too dangerous for the Earth, the "
                                  "Illuminati trick Hulk into a shuttle and launch "
                                  "him into space to a planet where the Hulk can "
                                  "live in peace. Unfortunately, Hulk land on the "
                                  "planet Sakaar where he is sold into slavery and"
                                  " trained as a gladiator.")

# Read the movie descriptions into a list.
movies_file = open('movies.txt', 'r')
movie_descriptions = []
for movie in movies_file.readlines():

    # Split the line at the delimiter " :".
    movie = movie.split(" :")

    # Create a Movie object and append it to the list.
    movie_descriptions.append(Movie(movie[0], movie[1]))
movies_file.close()

# Try out the function if this file is being run on its own.
if __name__ == "__main__":
    print(find_next_movie(hulk_movie, movie_descriptions))
