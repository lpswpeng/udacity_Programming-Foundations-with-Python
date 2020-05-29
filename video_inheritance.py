"""

"""
import webbrowser

class Video():
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube):
        self.title = video_title
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_info(self):
        print("Video Title: " + self.title)
        print("Video Storyline: " + self.storyline)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class Movie(Video):
    def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)
        #self.title = movie_title
        #self.storyline = movie_storyline
        self.duration = movie_duration
        #self.poster_image_url = poster_image
        #self.trailer_youtube_url = trailer_youtube


class TvShow(Video):
    def __init__(self, tvshow_title, tvshow_storyline, poster_image, tvshow_season, local_listing, trailer_youtube):
        Video.__init__(self, tvshow_title, tvshow_storyline, poster_image, trailer_youtube)
        #self.title = tvshow_title
        #self.storyline = tvshow_storyline
        #self.poster_image_url = poster_image
        self.season = tvshow_season
        self.local_listing_url = local_listing
        #self.trailer_youtube_url = trailer_youtube

    def get_local_listing(self):
        webbrowser.open(self.local_listing_url)

if __name__ == "__main__":
    avatar = ("Avatar",
              "2h 42min",
              "A marine on an alien planet",
              "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
              "https://www.youtube.com/watch?v=_V1lLSS9lCc")

    seinfeld = ("Seinfeld",
                "About comedian Seinfeld's life with a handful of friends and acquaintances",
                "https://upload.wikimedia.org/wikipedia/en/c/ce/Seinfeld1%262.jpg",
                "1 - 9",
                "https://en.wikipedia.org/wiki/List_of_Seinfeld_episodes#Episodes",
                "https://www.youtube.com/watch?v=SOsbYJ4CfTA")

    avatar_movie = Movie(*avatar)
    #avatar_movie.show_trailer()
    #avatar_movie.show_info()

    seinfeld_tvshow = TvShow(*seinfeld)
    seinfeld_tvshow.show_trailer()
    seinfeld_tvshow.show_info()
