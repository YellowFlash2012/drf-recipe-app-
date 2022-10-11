from django.urls import path

from users import views

app_name='users'

urlpatterns=[
    path('', views.SignupUserView.as_view(), name='user-signup'),
    
    path('token/', views.CreateTokenView.as_view(), name='token'),
    
    path('me/', views.UserProfileView.as_view(), name='user-profile'),
]