def checkMovies(flight_length, movie_lengths):
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        matching_second_movie_length = flight_length - first_movie_length
        if matching_second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    # We never found a match, so return False
    return False


movie_lengths = [20, 40, 50, 120, 30, 25]
flight_length = 45

print(checkMovies(flight_length, movie_lengths))
