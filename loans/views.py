from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Loan
from .utils import calculate_emi
from .services import calculate_credit_score
from datetime import date, timedelta


# ---------------- REGISTER CUSTOMER ----------------
@api_view(['POST'])
def register(request):

    salary = request.data["monthly_income"]

    approved_limit = round((36 * salary) / 100000) * 100000

    customer = Customer.objects.create(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        phone_number=request.data["phone_number"],
        monthly_salary=salary,
        approved_limit=approved_limit,
        current_debt=0
    )

    return Response({
        "customer_id": customer.customer_id,
        "name": customer.first_name + " " + customer.last_name,
        "age": request.data["age"],
        "monthly_income": salary,
        "approved_limit": approved_limit,
        "phone_number": customer.phone_number
    })


# ---------------- CHECK ELIGIBILITY ----------------
@api_view(['POST'])
def check_eligibility(request):

    customer = Customer.objects.get(customer_id=request.data["customer_id"])

    score = calculate_credit_score(customer)

    interest = request.data["interest_rate"]

    approve = False
    corrected_rate = interest

    if score > 50:
        approve = True

    elif score > 30:
        corrected_rate = max(interest, 12)
        approve = True

    elif score > 10:
        corrected_rate = max(interest, 16)
        approve = True

    emi = calculate_emi(
        request.data["loan_amount"],
        corrected_rate,
        request.data["tenure"]
    )

    if emi > customer.monthly_salary * 0.5:
        approve = False

    return Response({
        "customer_id": customer.customer_id,
        "approval": approve,
        "interest_rate": interest,
        "corrected_interest_rate": corrected_rate,
        "tenure": request.data["tenure"],
        "monthly_installment": emi
    })


# ---------------- CREATE LOAN ----------------
@api_view(['POST'])
def create_loan(request):

    customer = Customer.objects.get(customer_id=request.data["customer_id"])

    loan_amount = request.data["loan_amount"]
    interest_rate = request.data["interest_rate"]
    tenure = request.data["tenure"]

    score = calculate_credit_score(customer)

    corrected_rate = interest_rate

    if score > 50:
        pass
    elif score > 30:
        corrected_rate = max(interest_rate, 12)
    elif score > 10:
        corrected_rate = max(interest_rate, 16)
    else:
        return Response({
            "loan_id": None,
            "customer_id": customer.customer_id,
            "loan_approved": False,
            "message": "Credit score too low",
            "monthly_installment": None
        })

    emi = calculate_emi(loan_amount, corrected_rate, tenure)

    if emi > customer.monthly_salary * 0.5:
        return Response({
            "loan_id": None,
            "customer_id": customer.customer_id,
            "loan_approved": False,
            "message": "EMI exceeds 50% salary",
            "monthly_installment": emi
        })

    # fix for start_date & end_date
    start_date = date.today()
    end_date = start_date + timedelta(days=30 * tenure)

    loan = Loan.objects.create(
        customer=customer,
        loan_amount=loan_amount,
        interest_rate=corrected_rate,
        tenure=tenure,
        monthly_repayment=emi,
        emis_paid_on_time=0,
        start_date=start_date,
        end_date=end_date
    )

    return Response({
        "loan_id": loan.loan_id,
        "customer_id": customer.customer_id,
        "loan_approved": True,
        "monthly_installment": emi
    })


# ---------------- VIEW SINGLE LOAN ----------------
@api_view(['GET'])
def view_loan(request, loan_id):

    loan = Loan.objects.get(loan_id=loan_id)

    customer = loan.customer

    return Response({

        "loan_id": loan.loan_id,

        "customer": {
            "id": customer.customer_id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "phone_number": customer.phone_number
        },

        "loan_amount": loan.loan_amount,
        "interest_rate": loan.interest_rate,
        "monthly_installment": loan.monthly_repayment,
        "tenure": loan.tenure
    })


# ---------------- VIEW CUSTOMER LOANS ----------------
@api_view(['GET'])
def view_loans(request, customer_id):

    loans = Loan.objects.filter(customer_id=customer_id)

    result = []

    for loan in loans:
        result.append({
            "loan_id": loan.loan_id,
            "loan_amount": loan.loan_amount,
            "interest_rate": loan.interest_rate,
            "monthly_installment": loan.monthly_repayment,
            "repayments_left": loan.tenure - loan.emis_paid_on_time
        })

    return Response(result)