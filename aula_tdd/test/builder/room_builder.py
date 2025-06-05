from src.domain.model import Room, SeatStatus

class RoomBuilder:
    room: Room

    def __init__(self):
        pass

    def aRoom(self):
        self.room = Room("1")
        return self

    def build(self):
        return self.room
    
    def with_some_seats_unavailable(self):
        unavailable_seats = [("A", 1), ("A", 2), ("B", 4), ("C", 10)]
        
        for row_label, number in unavailable_seats:
            row_index = ord(row_label) - 65
            col_index = number - 1

            if row_index < len(self.room.rows) and col_index < len(self.room.rows[row_index]):
                self.room.rows[row_index][col_index].status = SeatStatus.RESERVED
        
        return self