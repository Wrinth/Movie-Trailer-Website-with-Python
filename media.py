import webbrowser

"""
The parent class for class Movie.
Contain information about video_title and video_duration
"""
class Video():
    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration

"""
The class Movie.
Contain information about movie_title, movie_storyline, movie_duration, poster_image, and trailer_youtube
Functions:
    show_trailer(): Call this function will open the TouTube video in a browser
"""
class Movie(Video):
    def __init__(self, movie_title, movie_storyline, movie_duration, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

