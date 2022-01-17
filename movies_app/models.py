from movies_app import db


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    plot = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    runtime = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.title} ({self.year})"


class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Role(db.Model):
    __tablename__ = "roles"
    role_name = db.Column(db.String(80), nullable=False)
    movie_id = db.Column(db.ForeignKey('movies.id'), primary_key=True)
    actor_id = db.Column(db.ForeignKey('actors.id'), primary_key=True)

    movie = db.relationship('Movie', backref='actors')
    actor = db.relationship('Actor', backref='movies')

    def __repr__(self):
        return self.role_name


class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.name


class MovieGenre(db.Model):
    __tablename__ = "movie_genres"
    movie_id = db.Column(db.ForeignKey('movies.id'), primary_key=True)
    genre_id = db.Column(db.ForeignKey('genres.id'), primary_key=True)

    movie = db.relationship('Movie', backref='genres')
    genre = db.relationship('Genre', backref='movies')

    def __repr__(self):
        return self.genre_name
