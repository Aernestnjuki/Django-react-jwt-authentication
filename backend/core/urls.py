from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('token/', views.Obtain_Access_And_Refresh_tokens.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('register/', views.SignIn_User.as_view()),
    path('dashboard/', views.DashboardView.as_view())
]
