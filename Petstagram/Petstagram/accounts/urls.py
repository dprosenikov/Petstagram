from django.urls import path

from Petstagram.accounts.views import login_user, logout_user, RegisterView, ProfileDetailsView, LoginView, \
    LoginUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('logout/', logout_user, name='logout user'),
    path('profile/', ProfileDetailsView.as_view(), name='profile')
]
