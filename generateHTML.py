import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{main_title}</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet"
	href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="css/style.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script
src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <!-- js to play video -->
    <script src="js/main.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div id="header" class="container-fluid">
        <div class="container">
                <h1>{main_title}</h1>
            <p>{main_comment}</p>
        </div>
    </div>
    <div class="container-fluid">
        {movie_titles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_title_content = '''
<div class="movie-title" data-trailer-youtube-id="{trailer_youtube_id}"
data-toggle="modal" data-target="#trailer">
    <div class="row">
    <div class="col-xs-3">
        <img class="img-responsive" src="{poster_image_url}" width="100%">
    </div>
    <div class="col-xs-9">
        <h2>{movie_title}</h2>
        <p>{movie_comment}</p>
    </div></div>
</div>
'''


def create_movie_titles_content(movies):
    """ Create content for each movie data """
    # The HTML content for this section of the page
    content = ''
    # Iterate over movies, passed from start.py to generate and format
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_title_content.format(
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_title=movie.title,
            movie_comment=movie.storyline
        )
    return content


def open_movies_page(page_title, page_comment, movies):
    """ Generate and open html page """
    # Create or overwrite the output file
    output_file = open("trailer.html", 'w')

    # Replace the movie titles placeholder generated content
    rendered_content = main_page_content.format(
        movie_titles=create_movie_titles_content(movies),
        main_title=page_title,
        main_comment=page_comment
    )
    # Replace the page title placeholder with title
    rendered_page_head = main_page_head.format(
        main_title=page_title
    )
    # Output the file
    output_file.write(rendered_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
