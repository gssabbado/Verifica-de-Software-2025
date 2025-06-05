from src.domain.model import Movie, Seat, Room, Session, User, Booking
from datetime import timedelta, datetime
from test.builder.room_builder import RoomBuilder

def test_create_session():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = Room("1")
    start_time = "17:00"
    session = Session(movie, room, start_time)
    
    assert session.movie.name == "Lilo e Stitch"
    assert session.movie.time == 90
    assert session.movie.genre == "Animacao"    
    assert session.room.name == "1"
    assert len(session.bookings) == 0

def test_calculate_end_time():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = Room("1")
    start_time = "17:00"
    session = Session(movie, room, start_time)
    end_time_session = timedelta(hours=18, minutes=30)
    assert session.get_end_time() == end_time_session
    
def test_seat_session_is_available():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = RoomBuilder().aRoom().build()
    session = Session(movie, room, "17:00")
    seat = Seat("B", 3)

    seat_in_session = session.get_seat_session(seat)

    assert seat_in_session is not None
    assert seat_in_session.is_available

def test_get_all_seats_session():
    movie = Movie("Lilo e Stitch", 90, "Animacao")
    room = RoomBuilder().aRoom().with_some_seats_unavailable().build()
    start_time = "17:00"
    session = Session(movie, room, start_time)

    assert session.room.available_seats() <= 100

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