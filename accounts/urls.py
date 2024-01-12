from django.contrib.auth.views import LoginView
from django.urls import path

from .forms import LoginForm



urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html', form_class=LoginForm), name='login')
]