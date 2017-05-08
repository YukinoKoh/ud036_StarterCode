#  Upper caps class name
import webbrowser


class Movie():
    """ This defines Movie class """
    VALID_RATING = ['a', 'b', 'c']

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ Defines Movie instance variable """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens youtube url in a browser """
        webbrowser.open(self.trailer_youtube_url)
