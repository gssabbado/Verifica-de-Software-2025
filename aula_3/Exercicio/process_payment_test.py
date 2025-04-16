import pytest
from process_payment import PaymentGatewayError, InvalidPaymentDetails, process_payment
from unittest.mock import patch

@patch('process_payment.random.random')
@patch('process_payment.random.randint')
def test_should_accept(mock_random, mock_randint):
    mock_random.return_value = 123456 
    mock_randint.return_value = 0.3  
    processo = process_payment("JohnDoe", 100)
    
    assert processo["status"] == "success"
    assert processo["transaction_id"] == "TXN-123456"
    assert processo["amount_charged"] == 100.0
    assert processo["currency"] == "USD"


def test_should_not_accept_invalid_payment_no_amount():
    with pytest.raises(InvalidPaymentDetails, match=r"Invalid user ID or amount."):
        process_payment("JohnDoe", 0)


def test_should_not_accept_invalid_payment_no_user_id():
    with pytest.raises(InvalidPaymentDetails, match=r"Invalid user ID or amount."):
        process_payment("", 100)

def test_should_not_accept_invalid_payment_invalid_currency():
    with pytest.raises(InvalidPaymentDetails):
        process_payment("JohnDoe", 100, "BRL")


@patch('process_payment.random.random')
@patch('process_payment.random.randint')
def test_should_not_accept_to_many_attempts(mock_random, mock_randint):
    with pytest.raises(PaymentGatewayError):
        mock_random.return_value = 123456 
        mock_randint.return_value = 0.1  
        process_payment("JohnDoe", 100)
    
