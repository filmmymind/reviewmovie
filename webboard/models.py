from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here
class boardpost(models.Model):
    Title = models.CharField(max_length = 255, null=False, blank=False)
    Image = models.ImageField(null = True, blank = True)
    Content = RichTextUploadingField(blank = False, null = False)
    Slug = AutoSlugField(populate_from='Content',null=False)
    Tag = models.CharField(max_length = 200)
    Post_Date = models.DateTimeField(auto_now_add = True)
    ShortContent = models.CharField(max_length = 255,null=True,blank=True)
    Author = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
class Boardcomment(models.Model):
    comment = RichTextUploadingField(blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    board = models.ForeignKey(boardpost,on_delete=models.CASCADE, default=None)
    reply = models.ForeignKey('self',null=True,related_name='replies',on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)