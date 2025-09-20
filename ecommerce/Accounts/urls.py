from django.urls import path
from .views import (
   Register,
   Login,
   Logout,
   Profile_View

)


urlpatterns = [
    path('', Register, name='home'),  # Home page URL
    path('register/', Register, name='register'),  # Explicit 'register' URL name
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', Profile_View, name='profile'),
]