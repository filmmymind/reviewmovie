from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class PostQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(description__icontains=query)|
                         Q(slug__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs
class PostManager(models.Manager):
    def gey_queryset(self):
        return PostQuerySet(self.model, using=self.db)
    def search(self, query=None):
        return self.gey_queryset().search(query=query)


# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Reviewmovie(models.Model):
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="300")
    moviename = models.CharField(max_length = 255)
    review = models.TextField()
    movie_image = models.ImageField(height_field='image_height')
    score = models.FloatField(default=0)
    movie_trailer = models.CharField(max_length = 255,blank=True)
    review_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User,default = None,on_delete = models.CASCADE)
    categorys = models.ManyToManyField(Category)
    director = models.CharField(max_length=2000)
    actor = models.CharField(max_length=2000)
    objects = PostManager()

    def __str__(self):
        return self.moviename

    def datepublished(self):
        return self.review_date.strftime('%B %d %Y')

    def rating(self):
        rating = Ratingmovie.objects.filter(movie=self)
        sum = 0
        for rate in rating:
            sum += rate.score
        return sum

    def rating_avg(self):
        rating = Ratingmovie.objects.filter(movie=self)
        sum = 0
        for rate in rating:
            sum += rate.score
        if len(rating) > 0:
            return sum / len(rating)
        else:
            return 0

class Ratingmovie(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    movie = models.ForeignKey(Reviewmovie, on_delete = models.CASCADE)
    score = models.FloatField(blank=True,null=True)
    def __str__(self):
        return self.movie.moviename


class Comment(models.Model):
    comment = models.TextField()
    movie = models.ForeignKey(Reviewmovie, default = None, on_delete=models.CASCADE)
    author = models.ForeignKey(User, default = None , on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('self',null=True, related_name="replies", on_delete=models.CASCADE)
