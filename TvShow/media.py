"""

"""
import webbrowser

class TvShow():
    """ This class provides a way to store TvShow related informaiton. """

    VALID_RATING = ["G", "PG", "PG-13", "R"]

    def __init__(self, tvshow_title, tvshow_storyline, poster_image, tvshow_season, local_listing, trailer_youtube):
        self.title = tvshow_title
        self.storyline = tvshow_storyline
        self.poster_image_url = poster_image
        self.season = tvshow_season
        self.local_listing_url = local_listing
        self.trailer_youtube_url = trailer_youtube

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    def get_local_listing(self):
        webbrowser.open(self.local_listing_url)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
