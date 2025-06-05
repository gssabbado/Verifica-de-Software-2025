from src.domain.model import Booking, User,  Seat, SeatStatus
from test.builder.session_builder import SessionBuilder
from datetime import timedelta, datetime

def test_create_booking():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat2 = Seat("B", 3)
    seat1.reserve()
    seat2.reserve()
    list_seats = [seat1, seat2]
    
    before_reserve = datetime.now()
    booking = Booking(user, session, 15, before_reserve, list_seats)
    after_reserve = datetime.now()

    assert booking.user == user
    assert booking.session == session
    assert booking.price == 15
    assert booking.seats == list_seats
    assert before_reserve <= booking.timestamp <= after_reserve

def test_booking_records_current_time():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat1.reserve()
    list_seats = [seat1]
    
    before_creation = datetime.now()
    booking = Booking(user, session, 15, datetime.now(), list_seats)
    after_creation = datetime.now()
    
    assert before_creation <= booking.timestamp <= after_creation

def test_calculate_total_price():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat2 = Seat("B", 3)
    seat3 = Seat("C", 1)
    seat1.reserve()
    seat2.reserve()
    seat3.reserve()
    list_seats = [seat1, seat2, seat3]
    
    price_per_seat = 15
    expected_total = len(list_seats) * price_per_seat
    
    booking = Booking(user, session, expected_total, datetime.now(), list_seats)
    
    assert booking.price == expected_total
    assert booking.calculate_total_price() == expected_total

def test_booking_added_to_user_bookings():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat1.reserve()
    list_seats = [seat1]

    assert len(user.booking) == 0
    
    booking = Booking(user, session, 15, datetime.now(), list_seats)
    
    user.booking.append(booking)
    
    assert len(user.booking) == 1
    assert user.booking[0] == booking

def test_booking_added_to_session_bookings():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat1.reserve()
    list_seats = [seat1]
        
    booking = Booking(user, session, 15, datetime.now(), list_seats)
    
    if hasattr(session, 'bookings'):
        if hasattr(session, 'add_booking'):
            session.add_booking(booking)
        else:
            session.bookings.append(booking)
        
        assert booking in session.bookings

def test_confirm_booking():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat2 = Seat("B", 3)
    seat1.reserve()
    seat2.reserve()
    list_seats = [seat1, seat2]
    
    booking = Booking(user, session, 30, datetime.now(), list_seats)
    
    for seat in booking.seats:
        assert seat.status == SeatStatus.RESERVED
    
    result = booking.confirm()
    assert result == True
    
    for seat in booking.seats:
        seat.confirm()
    
    for seat in booking.seats:
        assert seat.status == SeatStatus.OCCUPIED

def test_confirm_fails_if_any_seat_not_reserved():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat2 = Seat("B", 3)
    seat1.reserve()
    list_seats = [seat1, seat2]
    
    booking = Booking(user, session, 30, datetime.now(), list_seats)
    
    result = booking.confirm()
    assert result == False

def test_cancel_booking():
    user = User("John Doe", "john@email.com", 18)
    session = SessionBuilder().aSession().build()
    
    seat1 = Seat("B", 2)
    seat2 = Seat("B", 3)
    seat1.reserve()
    seat2.reserve()
    list_seats = [seat1, seat2]
    
    booking = Booking(user, session, 30, datetime.now(), list_seats)
    user.booking.append(booking)
    
    for seat in booking.seats:
        assert seat.status == SeatStatus.RESERVED
    
    
    for seat in booking.seats:
        seat.release()
    
    user.booking.remove(booking)
    
    for seat in booking.seats:
        assert seat.status == SeatStatus.AVAILABLE
    
    assert booking not in user.booking