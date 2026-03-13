from .models import Loan
from datetime import datetime


def calculate_credit_score(customer):

    loans = Loan.objects.filter(customer=customer)

    if not loans.exists():
        return 100

    score = 100

    # loan count penalty
    score -= loans.count() * 5

    # current year loans
    current_year = datetime.now().year
    current_loans = loans.filter(start_date__year=current_year).count()

    score -= current_loans * 5

    total_volume = sum(l.loan_amount for l in loans)

    if total_volume > customer.approved_limit:
        score = 0

    return max(min(score, 100), 0)