from django.test import TestCase
from .models import Customer

class CustomerTest(TestCase):

    def test_customer_creation(self):

        customer = Customer.objects.create(
            first_name="Rahul",
            last_name="Sharma",
            phone_number="9999999999",
            monthly_salary=50000,
            approved_limit=1800000,
            current_debt=0
        )

        self.assertEqual(customer.first_name, "Rahul")