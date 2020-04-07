from django.urls import path
from . import views

app_name = 'report'
urlpatterns=[
    path('report',views.Report, name='report'),
    path('report/<int:id>/delete', views.MemberDelete, name='memberdelete'),
    path('userinformation/<int:id>',views.UserInformation,name="userinformation")

]