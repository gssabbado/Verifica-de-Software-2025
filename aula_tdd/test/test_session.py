from src.domain.model import Movie, Seat, Room, Session  
from datetime import timedelta

def test_create_session():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = Room("1")
    start_time = "17:00"
    session = Session(movie, room, start_time)
    
    assert session.movie.name == "Lilo e Stitch"
    assert session.movie.time == 90
    assert session.movie.genre == "Animacao"    
    assert session.room.name == "1"

def test_calculate_end_time():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = Room("1")
    start_time = "17:00"
    session = Session(movie, room, start_time)
    end_time_session = timedelta(hours=18, minutes=30)
    assert session.get_end_time() == end_time_session
    
def test_seat_session_is_available():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = Room("1")
    start_time = "17:00"
    session = Session(movie, room, start_time)
    seat = Seat("B", 3)

    assert session.room.rows[0][2].is_available

def test_get_all_seats_session():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = Room("1")
    start_time = "17:00"
    session = Session(movie, room, start_time)

    assert session.room.available_seats() == 100

def test_session_overlap_same_room():
    movie = Movie("O Iluminado", 120, "Terror")
    room = Room("1")
    start_time = "18:00"
    session1 = Session(movie, room, start_time)
    
    movie2 = Movie("Lilo e Stitch", 90, "Animacao")
    room2 = Room("1")
    start_time2 = "17:00"
    session2 = Session(movie2, room2, start_time2)
    
    assert session1.room == session2.room
    assert session1.get_start_time() < session2.get_end_time()
    assert session2.get_start_time() < session1.get_end_time()
    
def test_session_overlap_different_room():
    movie = Movie("O Iluminado", 120, "Terror")
    room = Room("2")
    start_time = "18:00"
    session1 = Session(movie, room, start_time)
    
    movie2 = Movie("Lilo e Stitch", 90, "Animacao")
    room2 = Room("1")
    start_time2 = "17:00"
    session2 = Session(movie2, room2, start_time2)
    
    assert session1.get_start_time() < session2.get_end_time()
    assert session2.get_start_time() < session1.get_end_time()

"""    
def test_sequentional_session_overlap():
    movie = Movie("O Iluminado", 120, "Terror")
    room = Room("2")
    start_time = "18:00"
    session1 = Session(movie, room, start_time)
    
    movie2 = Movie("Lilo e Stitch", 90, "Animacao")
    room2 = Room("1")
    start_time2 = "17:00"
    session2 = Session(movie2, room2, start_time2)
    
    assert session1.get_start_time() < session2.get_end_time()
    assert session2.get_start_time() < session1.get_end_time()
"""