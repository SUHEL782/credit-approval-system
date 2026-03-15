from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Credit Approval System API",
        "endpoints": {
            "register": "/api/register",
            "check_eligibility": "/api/check-eligibility",
            "create_loan": "/api/create-loan",
            "view_loan": "/api/view-loan/<loan_id>",
            "view_customer_loans": "/api/view-loans/<customer_id>"
        }
    })


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("loans.urls")),
]
