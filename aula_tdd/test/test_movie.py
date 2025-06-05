from src.domain.model import Movie 
from datetime import timedelta

def test_create_movie():
    movie1 = Movie("Lilo e Stitch", 90, "Animacao")
    assert movie1.name == "Lilo e Stitch"
    assert movie1.time == 90
    assert movie1.genre == "Animacao"
    
def test_formatted_time():
    movie1 = Movie("Lilo e Stitch", 90, "Animacao")
    assert movie1.formatted_time() == "1h30min"

def test_formatted_time_only_hours():
    movie1 = Movie("Lilo e Stitch", 120, "Animacao")
    assert movie1.formatted_time() == "2h"


def test_timedelta_duration():
    movie1 = Movie("Lilo e Stitch", 90, "Animacao")
    expected_duration = timedelta(hours=1, minutes=30)
    assert movie1.get_duration() == expected_duration
    