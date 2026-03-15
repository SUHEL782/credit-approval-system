from django.test import TestCase
from .models import Customer, Loan
from datetime import date


class TestCustomer(TestCase):

    def test_customer_creation(self):

        customer = Customer.objects.create(
            first_name="Rahul",
            last_name="Sharma",
            age=25,
            phone_number="9999999999",
            monthly_salary=50000,
            approved_limit=1800000,
            current_debt=0
        )

        self.assertEqual(customer.first_name, "Rahul")
        self.assertEqual(customer.age, 25)
        self.assertEqual(customer.monthly_salary, 50000)


class TestLoan(TestCase):

    def test_loan_creation(self):

        customer = Customer.objects.create(
            first_name="Rahul",
            last_name="Sharma",
            age=25,
            phone_number="9999999999",
            monthly_salary=50000,
            approved_limit=1800000,
            current_debt=0
        )

        loan = Loan.objects.create(
            loan_id=1,
            customer=customer,
            loan_amount=200000,
            tenure=12,
            interest_rate=10,
            monthly_repayment=17583,
            emis_paid_on_time=0,
            start_date=date.today(),
            end_date=date.today()
        )

        self.assertEqual(loan.customer.first_name, "Rahul")
        self.assertEqual(loan.loan_amount, 200000)
