from django.urls import path
from . import views

app_name ='account'
urlpatterns=[
    path('register',views.Register,name="register"),
    path('login',views.Login, name="login"),
    path('logout',views.Logout, name="logout"),
    path('editprofile/<int:id>',views.Edit,name="edit")
]