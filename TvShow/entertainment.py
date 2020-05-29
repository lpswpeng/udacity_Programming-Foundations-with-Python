
"""
"""
import fresh_tomatoes
import media

breaking_bad = media.TvShow("Breaking Bad",
                            "A stage-three chemistry teacher produce and sell crystallized methamphetamine.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bd/Breaking_Bad_season_four_DVD.jpg",
                            "1 - 5",
                            "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes",
                            "https://www.youtube.com/watch?v=HhesaQXLuRY")


seinfeld = media.TvShow("Seinfeld",
                        "About comedian Seinfeld's life with a handful of friends and acquaintances",
                        "https://upload.wikimedia.org/wikipedia/en/c/ce/Seinfeld1%262.jpg",
                        "1 - 9",
                        "https://en.wikipedia.org/wiki/List_of_Seinfeld_episodes#Episodes",
                        "https://www.youtube.com/watch?v=SOsbYJ4CfTA")


tvshow = [breaking_bad, seinfeld]

fresh_tomatoes.open_movies_page(tvshow)

#print(media.Movie.VALID_RATING)
#print(media.Movie.__doc__)
