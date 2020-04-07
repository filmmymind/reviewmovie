from django.urls import path
from . import views

app_name= 'board'

urlpatterns =[
    path('',views.webboard, name="webboard"),
    path('create', views.createwebboard, name="createwebboard"),
    path('content/<slug:slug>/', views.boarddetail, name="boardcontent"),

    path('webboardreport/<int:id>/delete',views.deletewebboardreport, name="deletewebboardreport"),
    path('webboarddashboard/<int:id>/delete',views.deletewebboarddashboard, name="deletewebboarddashboard"),
]