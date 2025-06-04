from src.domain.model import Movie, Seat, Room, Session  
from datetime import timedelta

def test_create_session():
    movie = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat = Seat(row='A', number=1)
    room = Room("1")
    start_time = "17:00"
    id = "1"
    session = Session(movie, seat, room, start_time, id)
    
    assert session.id == "1"
    assert session.movie.id == "1"
    assert session.movie.name == "Lilo e Stitch"
    assert session.movie.time == 90
    assert session.movie.genre == "Animacao"
    
    assert session.seat.row == "A"
    assert session.seat.number == 1
    
    assert session.room.name == "1"

def test_unique_id_session():
    movie = Movie("2", "O Iluminado", 120, "Terror")
    seat = Seat(row='B', number=2)
    room = Room("3")
    start_time = "19:00"
    id = "2"
    session1 = Session(movie, seat, room, start_time, id)
    
    movie2 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat2 = Seat(row='A', number=1)
    room2 = Room("1")
    start_time2 = "17:00"
    id2 = "1"
    session2 = Session(movie2, seat2, room2, start_time2, id2)
    
    assert session1.unique_id(session2)

def test_calculate_end_time():
    movie = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat = Seat(row='A', number=1)
    room = Room("1")
    start_time = "17:00"
    id = "1"
    session = Session(movie, seat, room, start_time, id)
    
    end_time_session = timedelta(hours=18, minutes=30)
    
    assert session.get_end_time() == end_time_session
    
def test_seat_session_is_available():
    movie = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat = Seat(row='A', number=1)
    room = Room("1")
    start_time = "17:00"
    id = "1"
    session = Session(movie, seat, room, start_time, id)
    
    assert session.seat.is_available == True

def test_get_all_seats_session():
    movie = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat = Seat(row='A', number=1)
    room = Room("1")
    start_time = "17:00"
    id = "1"
    session = Session(movie, seat, room, start_time, id)

    assert session.room.available_seats() == 100

def test_session_overlap_same_room():
    movie = Movie("2", "O Iluminado", 120, "Terror")
    seat = Seat(row='B', number=2)
    room = Room("1")
    start_time = "18:00"
    id = "2"
    session1 = Session(movie, seat, room, start_time, id)
    
    movie2 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat2 = Seat(row='A', number=1)
    room2 = Room("1")
    start_time2 = "17:00"
    id2 = "1"
    session2 = Session(movie2, seat2, room2, start_time2, id2)
    
    assert session1.room == session2.room
    assert session1.get_start_time() < session2.get_end_time()
    assert session2.get_start_time() < session1.get_end_time()
    
def test_session_overlap_different_room():
    movie = Movie("2", "O Iluminado", 120, "Terror")
    seat = Seat(row='B', number=2)
    room = Room("2")
    start_time = "18:00"
    id = "2"
    session1 = Session(movie, seat, room, start_time, id)
    
    movie2 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat2 = Seat(row='A', number=1)
    room2 = Room("1")
    start_time2 = "17:00"
    id2 = "1"
    session2 = Session(movie2, seat2, room2, start_time2, id2)
    
    assert session1.get_start_time() < session2.get_end_time()
    assert session2.get_start_time() < session1.get_end_time()
    
def test_sequentional_session_overlap():
    movie = Movie("2", "O Iluminado", 120, "Terror")
    seat = Seat(row='B', number=2)
    room = Room("2")
    start_time = "18:00"
    id = "1"
    session1 = Session(movie, seat, room, start_time, id)
    
    movie2 = Movie("1", "Lilo e Stitch", 90, "Animacao")
    seat2 = Seat(row='A', number=1)
    room2 = Room("1")
    start_time2 = "17:00"
    id2 = "1"
    session2 = Session(movie2, seat2, room2, start_time2, id2)
    
    assert session1.id == session2.id
    assert session1.get_start_time() < session2.get_end_time()
    assert session2.get_start_time() < session1.get_end_time()

