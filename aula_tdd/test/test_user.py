from src.domain.model import User 

def test_create_user():
    user = User("1", "John Doe", "john@email.com", 18)
    
    assert user
    
def test_unique_id_user():
    user1 = User("1", "John Doe", "john@email.com", 18)
    user2 = User("1", "Mary Doe", "mary@email.com", 19)

    
    assert user1.unique_id(user2)

def test_user_booking_is_empty():
    user = User("1", "John Doe", "john@email.com", 18)
    
    assert len(user.booking) == 0