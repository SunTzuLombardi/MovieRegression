import requests

querystring = {"i": "tt4154796", "r": "json"}

api_url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
headers = {
    'x-rapidapi-key': "67a5bb0038msh1da1e5df30bcf9bp1bd063jsn465b7d5edac7",
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
}


class Movie:
    def __init__(self, mid, year, rated, released, runtime, genre, director, writer, actors, plot, language,
                 country, awards, poster, ratings, metascore, imdbrating, imdbvotes, type, dvd, boxoffice, production,
                 website, title=None, myrating = 0):
        self.mid = mid
        self.title = title
        self.year = year
        self.rated = rated
        self.released = released
        self.runtime = runtime
        self.genre = genre
        self.director = director
        self.writer = writer
        self.actors = actors
        self.plot = plot
        self.language = language
        self.country = country
        self.awards = awards
        self.poster = poster
        self.ratings = ratings
        self.metascore = metascore
        self.imdbrating = imdbrating
        self.imdbvotes = imdbvotes
        self.type = type
        self.dvd = dvd
        self.boxoffice = boxoffice
        self.production = production
        self.website = website
        self.myrating = myrating

        def __str__(self):
            return f'Movie title is {self.title} and year is {self.year}'

        def __repr__(self):
            return f'Movie(title={self.title}, year={self.year})'


def get_json(qparams):
    """
    ':returns json
    'Returns json text from a URL
    """
    response = None
    try:
        response = requests.request("GET", api_url, headers=headers, params=qparams)
        return response.json()
    finally:
        if response != None:
            response.close()


def search_by_id(movieid):
    """:returns json text
    """
    query = {"i": movieid, "r": "json"}
    return json_to_movie(get_json(query))


def search_by_title(movietitle):
    movies = []
    query = {"s": movietitle, "page": "1", "r": "json"}
    results = get_json(query)
    for movie in results['Search']:
        try:
            movies.append(json_to_movie(movie))
        except:
            pass
    return movies


def json_to_movie(json):
    movie = Movie(json.get('imdbID'), json.get('Year'), json.get('Rated'), json.get('Released'),
                  json.get('Runtime'), json.get('Genre'), json.get('Director'), json.get('Writer'), json.get('Actors'),
                  json.get('Plot'), json.get('Language'), json.get('Country'), json.get('Awards'), json.get('Poster'),
                  json.get('Ratings'), json.get('Metascore'), json.get('imdbRating'), json.get('imdbVotes'),
                  json.get('Type'), json.get('DVD'), json.get('BoxOffice'), json.get('Production'),
                  json.get('Website'), json.get('Title'),  myrating=0
                  )
    return movie
