import fresh_tomatoes
import media

"""
List of my favorite movies
You can add new favorite movie following this path:
    movie_name = media.Movie("movie_name",
                             "movie_storyline",
                             "movie_duration",
                             "poster_image_url",
                             "youtube_trailer_url")
"""
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "1h 21m",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc") # NOQA
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "2h 42m",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY") # NOQA
forrest_gump = media.Movie("Forrest Gump",
                           "The story of a man and his epic journey through life",
                           "2h 22m",
                           "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg", # NOQA
                           "https://www.youtube.com/watch?v=uPIEn0M8su0") # NOQA
school_of_rock = media.Movie("School of Rock",
                             "Overly enthusiastic guitarist Dewey Finn (Jack \
                              Black) gets thrown out of his bar band and finds \
                              himself in desperate need of work.",
                             "1h 49m",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", # NOQA
                             "https://www.youtube.com/watch?v=3PsUJFEBC74") # NOQA
ratatouille = media.Movie("Ratatouille",
                          "Remy (Patton Oswalt), a resident of Paris, \
                           appreciates good food and has quite a sophisticated palate.", 
                          "1h 55m",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", # NOQA
                          "https://www.youtube.com/watch?v=1yKqLNnxGZw") # NOQA

"""
PLace my favorite movies into a the movies list
"""
movies = [toy_story,avatar,forrest_gump,school_of_rock,ratatouille]

"""
Generate my website using the movies list in a browser
"""
fresh_tomatoes.open_movies_page(movies)
