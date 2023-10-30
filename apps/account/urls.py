from django.urls import path
from .views import UserRegistrationAPIView, LoginView, LogoutView
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),
    # path('login/', ObtainAuthToken.as_view())
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view())
]