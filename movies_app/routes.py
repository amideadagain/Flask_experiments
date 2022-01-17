from flask import render_template, url_for, redirect

from movies_app import app
from movies_app.models import Movie


@app.route("/movies", methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return render_template('movies.html', title='Movies', movies=movies)
