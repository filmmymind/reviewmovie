from django.contrib import admin
from . import models
# Register your models here.
class Review_display(admin.ModelAdmin):
    list_display = ('id','moviename','review_date','author')

class Category_display(admin.ModelAdmin):
    list_display =('id','category')
class Comment_display(admin.ModelAdmin):
    list_display =('movie','author')
class Rating_display(admin.ModelAdmin):
    list_display=('movie','score','user')
admin.site.register(models.Reviewmovie,Review_display)
admin.site.register(models.Category,Category_display)
admin.site.register(models.Comment,Comment_display)
admin.site.register(models.Ratingmovie,Rating_display)