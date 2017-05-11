import media
import generateHTML

page_title = "Inspirational movies"
page_comment = '''Click or tap, depend on your device, to watch trailers. <br/>
I recommend to watch these whether you are a designer:)'''

first_contact = media.Movie('''Documentary National Geographic - First
                             Contact Lost Tribes of the Amazon -
                             Documentaries 2016''',
                             "A documentaly about isolated indigenous tribe",
                             "http://docuwiki.net/images/4/4e/First-Contact-Lost-Tribe-of-the-Amazon-Cover.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=kXId0he7Qyg")
helvetica = media.Movie("Helvetica",
                        '''A documentary about typography and graphic design,
                        centered on the typeface of the same name. It's the
                        first part of Design Trilogy, directed by Gary
                        Hustwit.''',
                        "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Helvetica-film.JPG/320px-Helvetica-film.JPG",  # NOQA
                        "https://www.youtube.com/watch?v=X80kSDxF4rg")

objectified = media.Movie("Objectified",
                          '''The second part of Design Trilogy, about consumerism,
                          industrial deisgn.''',
                          "https://upload.wikimedia.org/wikipedia/en/7/75/Objectified_cover.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=S9E2D2PaIcI")

urbanized = media.Movie("Urbanized",
                        '''The third part of Design Trilogy, about architecture and
                        urban design.''',
	                "https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Urbanized-film-poster.jpg/320px-Urbanized-film-poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=qHWwxBEfikw")

indie_game = media.Movie("Indie Game",
                         '''A documentrary about days of indie game engineers,
                         Edmund McMillen and Tommy Refenes.''',
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Indie_Game_The_Movie_poster.png",  # NOQA
                         "https://www.youtube.com/watch?v=GhaT78i1x2M")

happy = media.Movie("HAPPY",
                    '''It explores positive psychology, interviewing people over 14
                    countries.''',
                    "https://upload.wikimedia.org/wikipedia/en/5/53/Happy_film.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=JcMQmuvzPmI")

exit_through = media.Movie("Exit Through the Gift Shop",
                    "A documentary about street art.",
                    "https://upload.wikimedia.org/wikipedia/en/5/57/Exit-through-the-gift-shop.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=oHJBdDSTbLw")

life_in = media.Movie(" Life In A Day",
                      '''A movie consisted with clips submitted to Youtube, after
                      questions \"What do you love? What do you fear? What\'s
                      in your pocket?\"''',
                      "https://upload.wikimedia.org/wikipedia/en/6/64/Lifeinaday_2011.jpg",  # NOQA
                      "https://www.youtube.com/watch?time_continue=107&v=bT_UmBHMYzg")  # NOQA

movies = [life_in, first_contact, helvetica, happy, indie_game,
          exit_through, objectified, urbanized]
generateHTML.open_movies_page(page_title, page_comment, movies)
