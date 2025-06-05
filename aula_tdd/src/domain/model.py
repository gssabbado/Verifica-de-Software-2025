from dataclasses import dataclass, field
from enum import Enum
from src.domain.errors import DuplicateRoomName, DuplicateIDMovie, DuplicateIDSession, DuplicateIDUser
from datetime import timedelta

class SeatStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"

@dataclass
class Seat:
    row: str
    number: int
    status: SeatStatus = SeatStatus.AVAILABLE

    @property
    def is_available(self):
        return self.status == SeatStatus.AVAILABLE
    
    def reserve(self):
        if self.status == SeatStatus.AVAILABLE:
            self.status = SeatStatus.RESERVED
            return True
        return False
    
    def confirm(self):
        if self.status == SeatStatus.RESERVED:
            self.status = SeatStatus.OCCUPIED
            return True
        return False
    
    def release(self):
        self.status = SeatStatus.AVAILABLE

    
@dataclass
class Room:
    name: str
    rows: list[list[Seat]]

    def __init__(self, name, seats=None):
        self.name = name
        self.rows = []
        if seats is None:
            self.create_list_of_seats()
            return
        i = 65
        for row in seats:
            row_seats = []
            row_name = chr(i)
            for j in range(row):
                seat = Seat(row=row_name, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)
            i += 1

    def create_list_of_seats(self):
        for i in range(10):
            row = chr(i + 65)
            row_seats = []
            for j in range(10):
                seat = Seat(row=row, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)

    def capacity(self):
        seats = 0
        for row in self.rows:
            seats += len(row)
        return seats
    
    def available_seats(self):
        available_seats = 0
        for row in self.rows:
            for seat in row:
                if seat.is_available:
                    available_seats += 1
        return available_seats
    
@dataclass
class Theater:
    rooms: list[Room] = field(default_factory=list)

    def add(self, room):
        if self.duplicate_room_name(room):
            raise DuplicateRoomName()
        self.rooms.append(room)

    def remove(self, room):
        self.rooms.remove(room)

    def duplicate_room_name(self, room):
        return [theater_room for theater_room in self.rooms if theater_room.name == room.name]
    
@dataclass
class Movie:
    name: str
    time: int
    genre: str
    
    def __init__(self, name, time, genre):
        self.name = name
        self.time = time
        self.genre = genre
        
    def formatted_time(self):
        minutes = self.time % 60
        hour = self.time // 60
        if minutes > 0 and hour > 0:
            length = f"{hour}h{minutes}min"
            return length
        elif hour == 0:
            length = f"{minutes}min"
            return length
        else:
            length = f"{hour}h"
            return length 
        
    
    def get_duration(self):
        hour = self.time//60
        minute = self.time % 60
        delta = timedelta(hours=hour, minutes=minute)
        return delta
    
    def unique_id(self, other_movie):
        if self.id == other_movie.id:
            return DuplicateIDMovie
        return True


@dataclass
class Session:
    movie: Movie
    room: Room
    start_time: str
    
    def __init__(self, movie, room, start_time):
        self.movie = movie
        self.room = room
        self.start_time = start_time
        
    def get_end_time(self):
        hour = self.movie.time // 60
        minute = self.movie.time % 60
        duration = self.start_time.split(":")
        start_time_hour = int(duration[0]) 
        start_time_minute = int(duration[1])
        end_time = timedelta(hours=start_time_hour + hour, minutes=start_time_minute + minute)
        return end_time
    
    def get_start_time(self):
        start_time = self.start_time.split(":")
        start_time_hour = int(start_time[0]) 
        start_time_minute = int(start_time[1])
        time = timedelta(hours=start_time_hour, minutes=start_time_minute)
        return time
    
    def get_seat_session(self, seat):
        row = ord(seat.row) - 65
        column = seat.number
        
        return 



@dataclass
class User:
    name: str
    email: str
    age: int
    booking: list[Session]
    
    def __init__(self, name, email, age, booking=None):
        self.name = name
        self.email = email
        self.age = age
        self.booking = []    
