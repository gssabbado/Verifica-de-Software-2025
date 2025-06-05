from src.domain.model import User 

def test_create_user():
    user = User("John Doe", "john@email.com", 18)
    assert user
    
def test_user_booking_is_empty():
    user = User("John Doe", "john@email.com", 18)
    assert len(user.booking) == 0