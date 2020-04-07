from django.contrib import admin
from .models import boardpost,Boardcomment

class boardpost_display(admin.ModelAdmin):
    list_display = ('id','Title','Author','Post_Date')

class boardcomment_display(admin.ModelAdmin):
    list_display = ('id','board','author','reply')
# Register your models here.
admin.site.register(boardpost,boardpost_display)
admin.site.register(Boardcomment,boardcomment_display)