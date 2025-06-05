from src.domain.model import Movie

class MovieBuilder:
    movie: Movie

    def __init__(self):
        pass

    def aMovie(self):
        self.movie = Movie("Lilo e Stitch", 90, "Animacao")
        return self

    def build(self):
        return self
    
    def with_duration(self, duration):
        self.movie.time = duration 
        return self