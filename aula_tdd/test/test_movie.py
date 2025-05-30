from src.domain.model import Movie 
from datetime import timedelta

def test_create_movie():
    movie1 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    assert movie1.name
    assert movie1.time
    assert movie1.genre
    
def test_formatted_time():
    movie1 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    assert movie1.formatted_time() == "1h30min"

def test_timedelta_duration():
    movie1 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    expected_duration = timedelta(hours=1, minutes=30)
    assert movie1.get_duration() == expected_duration

def test_unique_id_movie():
    movie1 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    movie2 = Movie("1", "O Iluminado", 120, "Terror")
    assert movie1.unique_id(movie2)
    