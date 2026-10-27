import pytest
from loan import Loan

def test_amount_below_minimum():
    with pytest.raises(Exception):
        Loan(amount=Loan.MIN_LOAN_AMOUNT - 1, years=5, interest_rate=0.05)

def test_amount_above_maximum():
    with pytest.raises(Exception):
        Loan(amount=Loan.MAX_LOAN_AMOUNT + 1, years=5, interest_rate=0.05)

def test_years_below_minimum():
    with pytest.raises(Exception):
        Loan(amount=10000, years=Loan.MIN_YEARS - 1, interest_rate=0.05)

def test_years_above_maximum():
    with pytest.raises(Exception):
        Loan(amount=10000, years=Loan.MAX_YEARS + 1, interest_rate=0.05)

def test_interest_rate_equal_to_min():
    with pytest.raises(Exception):
        Loan(amount=10000, years=5, interest_rate=Loan.MIN_INTEREST_RATE)

def test_interest_rate_equal_to_max():
    with pytest.raises(Exception):
        Loan(amount=10000, years=5, interest_rate=Loan.MAX_INTEREST_RATE)

def test_valid_loan_initialization():
    loan = Loan(amount=10000, years=5, interest_rate=0.05)
    assert loan.loan_amount == 10000
    assert loan.years == 5
    assert loan.interest_rate == 0.05
    assert loan.monthly_payment > 0
    assert loan.remaining_balance == 10000
    assert loan.months_remaining == 60

def test_invalid_payment_below_monthly():
    loan = Loan(amount=10000, years=5, interest_rate=0.05)
    with pytest.raises(Exception):
        loan.make_payment(loan.monthly_payment - 10)

def test_invalid_payment_above_balance():
    loan = Loan(amount=10000, years=5, interest_rate=0.05)
    with pytest.raises(Exception):
        loan.make_payment(loan.remaining_balance + 100)

def test_valid_payment_equal_to_monthly():
    loan = Loan(amount=10000, years=5, interest_rate=0.05)
    initial_balance = loan.remaining_balance
    initial_months = loan.months_remaining
    loan.make_payment(loan.monthly_payment)
    assert loan.remaining_balance < initial_balance
    assert loan.months_remaining == initial_months - 1

def test_valid_payment_equal_to_balance():
    loan = Loan(amount=1000, years=1, interest_rate=0.05)
    loan.make_payment(loan.remaining_balance)
    assert loan.remaining_balance == 0
    assert loan.months_remaining == 0
