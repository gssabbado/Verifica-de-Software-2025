from src.domain.model import Session, Room, Movie

class SessionBuilder:
    session: Session

    def __init__(self):
        pass

    def aSession(self):
        movie = Movie("Lilo e Stitch", 90, "Animacao")
        room = Room("1")
        self.session = Session(movie, room, "17:00")
        return self

    def build(self):
        return self.session
    
    