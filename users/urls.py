from django.urls import path

from users import views

app_name='users'

urlpatterns=[
    path('', views.SignupUserView.as_view(), name='user-signup')
]