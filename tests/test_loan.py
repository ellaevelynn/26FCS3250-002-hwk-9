'''
CS 3250 - Software Dev. Methods and Tools
Instructor: Thyago Mota
Student: Isabella Eaton
Description: Homework 09 - White-box (Unit) Testing
'''

import pytest
from src.loan import Loan

def test_case_1_amount_below_min():
    with pytest.raises(Exception):
        Loan(Loan.MIN_LOAN_AMOUNT - 1, 5, 0.05)

def test_case_2_amount_above_max():
    with pytest.raises(Exception):
        Loan(Loan.MAX_LOAN_AMOUNT + 1, 5, 0.05)

def test_case_3_years_below_min():
    with pytest.raises(Exception):
        Loan(100000, Loan.MIN_YEARS - 1, 0.05)

def test_case_4_years_above_max():
    with pytest.raises(Exception):
        Loan(100000, Loan.MAX_YEARS + 1, 0.05)

def test_case_5_interest_rate_equal_min():
    with pytest.raises(Exception):
        Loan(100000, 5, Loan.MIN_INTEREST_RATE)

def test_case_6_interest_rate_equal_max():
    with pytest.raises(Exception):
        Loan(100000, 5, Loan.MAX_INTEREST_RATE)

def test_case_7_valid_loan_initialization():
    loan = Loan(120000, 10, 0.05)
    assert loan.loan_amount == 120000
    assert loan.years == 10
    assert loan.interest_rate == 0.05
    assert loan.monthly_payment > 0
    assert loan.remaining_balance == 120000
    assert loan.months_remaining == 120

def test_case_8_invalid_payment_below_monthly():
    loan = Loan(120000, 10, 0.05)
    with pytest.raises(Exception):
        loan.make_payment(loan.monthly_payment - 10)

def test_case_9_invalid_payment_above_balance():
    loan = Loan(120000, 10, 0.05)
    with pytest.raises(Exception):
        loan.make_payment(loan.remaining_balance + 1000)

def test_case_10_valid_payment_equal_monthly():
    loan = Loan(120000, 10, 0.05)
    initial_balance = loan.remaining_balance
    initial_months = loan.months_remaining
    loan.make_payment(loan.monthly_payment)
    assert loan.remaining_balance < initial_balance
    assert loan.months_remaining == initial_months - 1

def test_case_11_valid_payment_equal_balance():
    loan = Loan(120000, 1, 0.05)
    loan.make_payment(loan.remaining_balance)
    assert loan.remaining_balance == 0
    assert loan.months_remaining == 0
