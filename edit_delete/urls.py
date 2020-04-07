from django.urls import path
from . import views

app_name = 'edit_delete'
urlpatterns =[
    path('deletemoviecomment/<int:id>',views.Deletemoviecomment,name="deletemoviecomment"),
    path('deletemoviereply/<int:id>',views.Deletemoviereply,name="deletemoviereply"),
    path('deletewebboard/<int:id>',views.Deletewebboard,name="deletewebboard"),
    path('deletewebboardcomment/<int:id>',views.Deletewebboardcomment,name="deletewebboardcomment"),
    path('editmoviereply/<int:id>',views.EditmovieReply,name="editmoviereply"),
    path('editmoviecomment/<int:id>',views.EditmovieComment,name="editmoviecomment"),
    path('editwebboard/<int:id>',views.EditWebboard,name="editwebboard"),
    path('editwebboardcomment/<int:id>',views.EditWebboardComment,name="editwebboardcomment"),
    path('editwebboardreply/<int:id>',views.EditWebboardReply,name="editwebboardreply"),
    path('editstatus/<int:id>',views.EditStatus,name="setstatus"),

    path('editmovie/<int:id>',views.Editmovie,name="editmovie")
]