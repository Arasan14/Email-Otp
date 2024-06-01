from django.urls import path
from . views import RegisterEmail, VerifyOtp

urlpatterns = [
    path("Reg/", RegisterEmail.as_view(), name="Register"),
    path('Very/', VerifyOtp.as_view(), name= "verify")
]
