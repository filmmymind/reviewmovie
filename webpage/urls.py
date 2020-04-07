from django.urls import path
from . import views

app_name='movie'

urlpatterns =[
    path('',views.Index, name='home'),
    path('movielist',views.Movielist, name="movielist"),
    path('addmovie',views.Addmovie,name="addmovie"),
    path('moviedetail/<int:id>/',views.Moviedetail, name="moviedetail"),
    path('categorypage/<int:id>/',views.Categorypage,name="categorypage"),
    path('dashboard/<int:id>',views.Dashboard,name="dashboard"),
    path('profile/<int:id>',views.Profile,name="profile"),
    path('Search',views.Search,name="Search"),

    path('deletemovie/<int:id>',views.deletemovie,name="deletemovie"),
    path('indexdeletemovie/<int:id>',views.indexdeletemovie,name="indexdeletemovie"),
    path('reportdeletemovie/<int:id>',views.reportdeletemovie,name="reportdeletemovie"),
]